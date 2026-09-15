import datetime as dt
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("lint_knowledge.py")
SPEC = importlib.util.spec_from_file_location("lint_knowledge", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class KnowledgeLintTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "ideas" / "demo").mkdir(parents=True)
        (self.root / "raw").mkdir()
        (self.root / "INDEX.md").write_text(self.doc("# Index", "ideas/demo/idea.md"), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def doc(self, title="# Demo", extra=""):
        future = (dt.date.today() + dt.timedelta(days=30)).isoformat()
        return (
            f"{title}\n\nOwner: Product Lead\nLast updated: 2026-08-23\n"
            f"Source: source\nConfidence: High\nRelated decisions: none\n"
            f"Next review date: {future}\n\n{extra}\n"
        )

    def codes(self):
        return {issue.code for issue in MODULE.run(self.root)}

    def test_valid_fixture(self):
        (self.root / "ideas" / "demo" / "idea.md").write_text(self.doc(), encoding="utf-8")
        self.assertFalse({"missing-metadata", "broken-link", "missing-index"} & self.codes())

    def test_missing_metadata_and_broken_link(self):
        (self.root / "ideas" / "demo" / "idea.md").write_text("# Demo\n[bad](missing.md)\n", encoding="utf-8")
        self.assertTrue({"missing-metadata", "broken-link"} <= self.codes())

    def test_duplicate_title(self):
        (self.root / "ideas" / "demo" / "idea.md").write_text(self.doc(), encoding="utf-8")
        (self.root / "ideas" / "demo" / "copy.md").write_text(self.doc(), encoding="utf-8")
        self.assertIn("duplicate-title", self.codes())

    def test_invalid_raw_record(self):
        (self.root / "ideas" / "demo" / "idea.md").write_text(self.doc(), encoding="utf-8")
        (self.root / "raw" / "wrong.md").write_text("source_id: bad\nsource_type: ai-generated\n", encoding="utf-8")
        self.assertTrue({"invalid-source-id", "ai-as-raw-source"} <= self.codes())

    def test_outputs_cannot_be_source(self):
        bad = self.doc().replace("Source: source", "Source: outputs/answer.md")
        (self.root / "ideas" / "demo" / "idea.md").write_text(bad, encoding="utf-8")
        self.assertIn("derived-as-source", self.codes())

    def test_duplicate_url_and_invalid_enum(self):
        (self.root / "ideas" / "demo" / "idea.md").write_text(self.doc(), encoding="utf-8")
        base = (
            'title: "x"\nsource_url_or_path: "https://example.com/x"\n'
            'publisher_or_author: "x"\npublished_or_event_date: unknown\naccessed_date: 2026-08-23\n'
            'source_class: Z\nsource_type: official\nprojects:\n  - demo\n'
            'storage_permission: metadata-and-short-excerpt\naccess_status: verified\nsummary: "x"\n'
            'quoted_or_referenced_location: "x"\nsupersedes: null\n'
        )
        for number in (1, 2):
            source_id = f"SRC-20260823-demo-{number:02d}"
            (self.root / "raw" / f"{source_id}.md").write_text(f"source_id: {source_id}\n{base}", encoding="utf-8")
        self.assertTrue({"duplicate-source-url", "invalid-raw-enum"} <= self.codes())


if __name__ == "__main__":
    unittest.main()
