#!/usr/bin/env python3
"""Check the generated website using only the Python standard library."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit


ORIGIN = "https://jungholeestat.github.io"
REQUIRED_PAGES = (
    "index.html",
    "research/index.html",
    "talks/index.html",
    "publications/index.html",
    "news/index.html",
    "404.html",
)


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.references = []
        self.images_without_alt = 0
        self.headings = 0
        self.has_title = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "name" in attrs:
            self.ids.add(attrs["name"])
        if tag == "title":
            self.has_title = True
        if tag == "h1":
            self.headings += 1
        if tag == "img" and "alt" not in attrs:
            self.images_without_alt += 1
        key = "href" if tag in ("a", "link") else "src"
        if tag in ("a", "link", "img", "script", "iframe", "source"):
            if attrs.get(key):
                self.references.append(attrs[key])
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            match = re.search(r"url\s*=\s*(.+)", attrs.get("content", ""), re.I)
            if match:
                self.references.append(match.group(1).strip("\"' "))


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    errors = []
    pages = {}
    for name in REQUIRED_PAGES:
        if not (root / name).is_file():
            errors.append(f"Missing page: {name}")

    for path in sorted(root.rglob("*.html")):
        source = path.read_text(encoding="utf-8")
        page = Page(source)
        pages[path] = page
        name = path.relative_to(root).as_posix()
        if "{{" in source or "{%" in source:
            errors.append(f"Unrendered Liquid in {name}")
        if not page.has_title or page.headings != 1:
            errors.append(f"Expected a title and one h1 in {name}")
        if page.images_without_alt:
            errors.append(f"Image missing alt text in {name}")

    reference_count = 0
    for path, page in pages.items():
        name = path.relative_to(root).as_posix()
        page_url = ORIGIN + "/" + name.removesuffix("index.html")
        for reference in page.references:
            target = urlsplit(urljoin(page_url, reference))
            if target.scheme not in ("http", "https") or target.netloc != urlsplit(ORIGIN).netloc:
                continue
            reference_count += 1
            target_path = (root / unquote(target.path).lstrip("/")).resolve()
            if not target_path.is_relative_to(root):
                errors.append(f"Link outside site in {name}: {reference}")
                continue
            if target_path.is_dir():
                target_path /= "index.html"
            if not target_path.is_file():
                errors.append(f"Broken internal link in {name}: {reference}")
            elif target.fragment and target_path in pages:
                if unquote(target.fragment) not in pages[target_path].ids:
                    errors.append(f"Missing anchor in {name}: {reference}")

    about = root / "index.html"
    if about.is_file() and "↗" in about.read_text(encoding="utf-8"):
        errors.append("About page still contains an external-link arrow")
    for name in ("Gemfile", "Gemfile.lock", "package.json", "package-lock.json", "bin", "README.md", "node_modules"):
        if (root / name).exists():
            errors.append(f"Build includes source-only file or directory: {name}")

    if errors:
        print("Site checks failed:\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Checked {len(pages)} HTML pages and {reference_count} internal references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
