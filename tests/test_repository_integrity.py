from pathlib import Path
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def local_links(text):
    for match in re.findall(r'''\[[^\]]*\]\(([^)]+)\)|(?:src|href)=["']([^"']+)''', text):
        target = next(value for value in match if value)
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        yield unquote(parsed.path)


def test_all_markdown_links_resolve():
    for path in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        for target in local_links(text):
            resolved = (path.parent / target).resolve()
            assert resolved.exists(), f"Broken local link in {path.relative_to(ROOT)}: {target}"


def test_notebooks_are_valid_json():
    for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["nbformat"] == 4
        assert len(data.get("cells", [])) >= 3
