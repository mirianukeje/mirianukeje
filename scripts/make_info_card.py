
from pathlib import Path
import html

BURGUNDY = "#6E263F"
CREAM = "#FFFCF4"
GOLD = "#DDBB72"
PINK = "#F4D9DF"

WIDTH = 600
HEIGHT = 480


def make_svg():
    lines = [
        ("$ whoami", GOLD),
        ("mirian-ukeje", CREAM),
        ("", CREAM),
        ("$ role", GOLD),
        ("Software Development Student", CREAM),
        ("Frontend Developer | UI/UX Designer", PINK),
        ("", CREAM),
        ("$ currently_learning", GOLD),
        ("JavaScript  /  React  /  Node.js", CREAM),
        ("SQL  /  APIs  /  Full-stack development", CREAM),
        ("", CREAM),
        ("$ tools", GOLD),
        ("HTML  CSS  JavaScript  Python  SQL", CREAM),
        ("Git  GitHub  VS Code  Figma", CREAM),
        ("", CREAM),
        ("$ interests", GOLD),
        ("Thoughtful design. Useful software.", CREAM),
        ("Accessible and responsive experiences.", CREAM),
        ("", CREAM),
        ("$ status", GOLD),
        ("Always learning, always building.", PINK),
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}">',
        "<title>Mirian's developer information card</title>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" '
        f'rx="12" fill="{BURGUNDY}"/>',

        f'<rect x="1" y="1" width="{WIDTH - 2}" '
        f'height="{HEIGHT - 2}" rx="12" '
        f'fill="none" stroke="{GOLD}" stroke-opacity="0.7"/>',

        f'<circle cx="25" cy="24" r="5" fill="{PINK}"/>',
        f'<circle cx="43" cy="24" r="5" fill="{GOLD}"/>',
        f'<circle cx="61" cy="24" r="5" fill="{CREAM}"/>',

        f'<text x="85" y="28" fill="{CREAM}" '
        f'font-family="monospace" font-size="12">'
        f'mirian@developer-profile</text>',

        f'<line x1="20" y1="45" x2="580" y2="45" '
        f'stroke="{GOLD}" stroke-opacity="0.6"/>',
    ]

    start_y = 72
    line_height = 18

    for index, (line, color) in enumerate(lines):
        y = start_y + index * line_height
        safe_line = html.escape(line)
        delay = index * 0.16

        parts.append(
            f'<text x="25" y="{y}" fill="{color}" '
            f'font-family="monospace" font-size="12" '
            f'opacity="0">'
            f'{safe_line}'
            f'<animate attributeName="opacity" '
            f'from="0" to="1" dur="0.25s" '
            f'begin="{delay:.2f}s" fill="freeze"/>'
            f'</text>'
        )

    parts.extend([
        f'<line x1="20" y1="438" x2="580" y2="438" '
        f'stroke="{GOLD}" stroke-opacity="0.6"/>',

        f'<text x="25" y="460" fill="{GOLD}" '
        f'font-family="monospace" font-size="11">'
        f'building with curiosity + creativity</text>',

        "</svg>",
    ])

    return "\n".join(parts)


if __name__ == "__main__":
    repository = Path(__file__).resolve().parent.parent
    output_file = repository / "developer-info.svg"

    output_file.write_text(make_svg(), encoding="utf-8")
    print(f"Info card created successfully: {output_file}")
