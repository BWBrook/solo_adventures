from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from tools.check_branches import check_adventure, main, mermaid, parse_adventure


class BranchChecks(unittest.TestCase):
    def test_navigation_phrases_and_multiple_targets(self):
        adventure = parse_adventure("""### 1
Go to 2, 3, or 4. Go back to 5. RETURN TO 6. Continue from 7.
Start at 8. Begin from 9. Going to 10. The path goes to 11.
Follow the trail to 12. Go to 13/14. Go to 15 and 16.
Roll 20 dice at tier 3; entries 40-49 explain difficulty.
""")
        self.assertEqual(adventure.entries[1], set(range(2, 17)))

    def test_appendix_and_fenced_examples_do_not_add_routes(self):
        adventure = parse_adventure("""### 1
Go to 2.
#### Local detail
Return to 1.
```markdown
### 777
Go to 800.
```
### 2
The end.
## Conversion Notes
At tier 3, go to 99.
### Tier 4
Start at 100.
""")
        self.assertEqual(adventure.entries, {1: {1, 2}, 2: set()})
        self.assertEqual(check_adventure(adventure, {"terminals": [2]}), [])

    def test_non_numeric_level_three_heading_ends_entry(self):
        adventure = parse_adventure("### 1\nGo to 2.\n### Route overview\nGo to 888.\n### 2\nEnd.")
        self.assertEqual(adventure.entries, {1: {2}, 2: set()})

    def test_duplicate_dangling_and_dead_end(self):
        adventure = parse_adventure("### 1\nGo to 2.\n### 1\nGo to 8.\n### 2\nNothing.")
        errors = check_adventure(adventure, {})
        self.assertIn("duplicate entry 1 at line 3", errors)
        self.assertIn("entry 1 links to missing entry 8", errors)
        self.assertIn("entry 2 is an undeclared dead end", errors)

    def test_disconnected_cycle_is_unreachable_despite_incoming_links(self):
        adventure = parse_adventure("### 1\nGo to 2.\n### 2\nEnd.\n### 3\nGo to 4.\n### 4\nGo to 3.")
        self.assertEqual(check_adventure(adventure, {"terminals": [2]}), ["unreachable from 1: 3, 4"])

    def test_source_coverage_accepts_explicit_omissions(self):
        adventure = parse_adventure("### 1\nGo to 3.\n### 3\nEnd.")
        contract = {"terminals": [3], "source_entries": [1, 2, 3], "omitted_entries": [2]}
        self.assertEqual(check_adventure(adventure, contract), [])
        contract["omitted_entries"] = [1, 8]
        errors = check_adventure(adventure, contract)
        self.assertIn("entry 1 is both present and declared omitted", errors)
        self.assertIn("source entry 2 is neither present nor declared omitted", errors)
        self.assertIn("entry 8 is outside the declared source coverage", errors)

    def test_missing_start_and_misdeclared_terminals(self):
        adventure = parse_adventure("### 2\nGo to 3.\n### 3\nEnd.")
        errors = check_adventure(adventure, {"terminals": [2, 3, 4]})
        self.assertIn("start entry 1 is missing", errors)
        self.assertIn("declared terminal 4 is missing", errors)
        self.assertIn("declared terminal 2 has outgoing links", errors)

    def test_mermaid_includes_all_nodes_edges_and_terminal(self):
        adventure = parse_adventure("### 1\nGo to 2 or 3.\n### 2\nReturn to 1.\n### 3\nEnd.")
        graph = mermaid([("example.md", adventure, {"terminals": [3]})])
        self.assertIn('m0_3["3 (end)"]', graph)
        self.assertEqual({line.strip() for line in graph.splitlines() if " --> " in line},
                         {"m0_1 --> m0_2", "m0_1 --> m0_3", "m0_2 --> m0_1"})

    def test_cli_failure_status_and_graph_output(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "docs/branch-contracts.json").write_text(json.dumps({"modules": [
                {"path": "example.md", "start": 1, "terminals": [2]}
            ]}))
            module = root / "example.md"
            module.write_text("### 1\nGo to 99.\n### 2\nEnd.")
            with patch("tools.check_branches.ROOT", root):
                with redirect_stderr(io.StringIO()) as errors, redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(main(["--mermaid"]), 1)
                self.assertIn("missing entry 99", errors.getvalue())
                self.assertEqual(output.getvalue(), "")
                module.write_text("### 1\nGo to 2.\n### 2\nEnd.")
                with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(main(["example.md", "--mermaid"]), 0)
                self.assertTrue(output.getvalue().startswith("flowchart TD\n"))


if __name__ == "__main__":
    unittest.main()
