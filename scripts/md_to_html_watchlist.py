from pathlib import Path
import sys
import re

'''
This script generates a html movie list for a year based on a markdown
file provided as input. 

The expected markdown format is:
- 01/01 - Contact (1997, Robert Zemeckis)
- 06/01 - Radio On (1979, Christopher Petit)
- 17/01 - Nosferatu (2024, Robert Eggers)
- 20/01 - Puzzle (2018, Marc Turtletaub)
'''

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<head>
  <title>Movie Watchlist {year}</title>
</head>

<body>
    <h1>Movie Watchlist {year}</h1>

    <ul>
{items}
    </ul>
</body>
</html>
"""

def parse_markdown(md_path: Path):
    items = []
    year = None

    for line in md_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if line.startswith("- "):
            items.append(line[2:].strip())

    return items

def main(md_file: Path, out_dir: Path):

    # Extract year from filename
    filename = md_file.name
    m = re.search(r"(19|20)\d{2}", filename)
    if m:
        year = m.group(0)
    
    if not year:
        raise ValueError("Could not determine year from filename")

    items = parse_markdown(md_file)

    li_html = "\n".join(f"      <li>{item}</li>" for item in items)

    html = HTML_TEMPLATE.format(
        year=year,
        items=li_html
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(html, encoding='utf-8')

    print(f"Generated {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: md_to_html_watchlist.py <input.md> <output_dir>")
        sys.exit(1)

    main(Path(sys.argv[1]), Path(sys.argv[2]))