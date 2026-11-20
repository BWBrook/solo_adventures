#!/usr/bin/env python3
"""Check numbered adventure routes against docs/branch-contracts.json."""

import argparse
from dataclasses import dataclass, field
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
HEADING = re.compile(r"^ {0,3}(#{1,3})\s+(.*?)\s*$")
NUMBER = re.compile(r"[0-9]+")
NAVIGATION = re.compile(
    r"\b(?:go to|going to|goes to|go back to|return to|continue from|"
    r"start at|begin from|trail to)\s+"
    r"([0-9]+(?:\s*(?:,\s*(?:(?:and|or)\s+)?|/|(?:and|or)\s+)\s*[0-9]+)*)\b",
    re.IGNORECASE,
)


@dataclass
class Adventure:
    entries: dict[int, set[int]] = field(default_factory=dict)
    lines: dict[int, int] = field(default_factory=dict)
    duplicates: list[tuple[int, int]] = field(default_factory=list)


def parse_adventure(text: str) -> Adventure:
    adventure = Adventure()
    active = None
    fence = None
    for line_number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            continue
        if marker:
            fence = marker[1]
            continue
        heading = HEADING.match(line)
        if heading:
            active = None
            if len(heading[1]) == 3 and NUMBER.fullmatch(heading[2]):
                active = int(heading[2])
                if active in adventure.entries:
                    adventure.duplicates.append((active, line_number))
                else:
                    adventure.entries[active] = set()
                    adventure.lines[active] = line_number
            continue
        if active is not None:
            for match in NAVIGATION.finditer(line):
                adventure.entries[active].update(map(int, NUMBER.findall(match[1])))
    return adventure


def check_adventure(adventure: Adventure, contract: dict) -> list[str]:
    errors = [f"duplicate entry {entry} at line {line}" for entry, line in adventure.duplicates]
    observed = set(adventure.entries)
    start = contract.get("start", 1)
    terminals = set(contract.get("terminals", []))
    for entry, targets in adventure.entries.items():
        for target in sorted(targets - observed):
            errors.append(f"entry {entry} links to missing entry {target}")
        if not targets and entry not in terminals:
            errors.append(f"entry {entry} is an undeclared dead end")
    for terminal in sorted(terminals - observed):
        errors.append(f"declared terminal {terminal} is missing")
    for terminal in sorted(terminals & observed):
        if adventure.entries[terminal]:
            errors.append(f"declared terminal {terminal} has outgoing links")
    if start not in observed:
        errors.append(f"start entry {start} is missing")
    reached = set()
    pending = [start]
    while pending:
        entry = pending.pop()
        if entry in observed and entry not in reached:
            reached.add(entry)
            pending.extend(adventure.entries[entry] - reached)
    if observed - reached:
        errors.append(f"unreachable from {start}: {', '.join(map(str, sorted(observed - reached)))}")
    if "source_entries" in contract:
        source = set(contract["source_entries"])
        omitted = set(contract.get("omitted_entries", []))
        for entry in sorted(observed & omitted):
            errors.append(f"entry {entry} is both present and declared omitted")
        for entry in sorted(source - observed - omitted):
            errors.append(f"source entry {entry} is neither present nor declared omitted")
        for entry in sorted((observed | omitted) - source):
            errors.append(f"entry {entry} is outside the declared source coverage")
    return errors


def mermaid(modules: list[tuple[str, Adventure, dict]]) -> str:
    lines = ["flowchart TD"]
    for index, (path, adventure, contract) in enumerate(modules):
        prefix = f"m{index}_"
        lines.append(f"  subgraph {prefix}module[{json.dumps(path)}]")
        terminals = set(contract.get("terminals", []))
        for entry in sorted(adventure.entries):
            label = str(entry) + (" (end)" if entry in terminals else "")
            lines.append(f'    {prefix}{entry}["{label}"]')
        for entry, targets in sorted(adventure.entries.items()):
            lines.extend(f"    {prefix}{entry} --> {prefix}{target}" for target in sorted(targets))
        lines.append("  end")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="One module path from the manifest; default: all modules")
    parser.add_argument("--mermaid", action="store_true", help="Print the complete route graph on success")
    args = parser.parse_args(argv)
    try:
        manifest = json.loads((ROOT / "docs/branch-contracts.json").read_text())
        contracts = manifest["modules"]
        if args.path:
            selected = {Path(args.path).resolve(), (ROOT / args.path).resolve()}
            contracts = [c for c in contracts if (ROOT / c["path"]).resolve() in selected]
            if not contracts:
                parser.error(f"module is not in the manifest: {args.path}")
        if not contracts:
            raise ValueError("manifest has no modules")
        modules = []
        failed = False
        for contract in contracts:
            path = contract["path"]
            adventure = parse_adventure((ROOT / path).read_text())
            errors = check_adventure(adventure, contract)
            modules.append((path, adventure, contract))
            if errors:
                failed = True
                for error in errors:
                    print(f"{path}: {error}", file=sys.stderr)
            else:
                edges = sum(map(len, adventure.entries.values()))
                print(f"{path}: OK ({len(adventure.entries)} entries, {edges} links)", file=sys.stderr)
        if failed:
            return 1
        if args.mermaid:
            print(mermaid(modules))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"check_branches: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
