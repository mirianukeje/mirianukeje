
from pathlib import Path
import html

BURGUNDY = "#6E263F"
CREAM = "#FFFCF4"
GOLD = "#DDBB72"
PINK = "#F4D9DF"

WIDTH = 600
HEIGHT = 480
FONT_SIZE = 14
LINE_HEIGHT = 17
START_X = 160
START_Y = 75


def make_flower():
    return [
        "                   .-._",
        "              .-.'     `-.",
        "            .'   .-'''-.   `.",
        "           /   .'  .-.  `.   \\",
        "          ;   /   (   )   \\   ;",
        "          |  ;  .-`---'-.  ;  |",
        "          ;  | /  .---.  \\ |  ;",
        "           \\  ; | (   ) | ;  /",
        "            `.\\  `-._.-'  /.'",
        "              `-.  ___ .-'",
        "                 `-._.-'",
        "                    |",
        "             _..---/ \\---.._",
        "          .-'      /   \\      `-.",
        "         /        /     \\        \\",
        "        /   .----'       `----.   \\",
        "        \\  /                   \\  /",
        "         \\/                     \\/",
        "                    |",
        "                    |",
        "                   / \\",
        "                  /   \\",
        "                 /     \\",
        "                /       \\",
        "               /_________\\",
    ]


def make_svg():
    lines = make_flower()

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}">',
        "<title>Mirian's animated ASCII flower</title>",

        f'<rect width="{WIDTH}" height="{HEIGHT}" '
        f'rx="12" fill="{BURGUNDY}"/>',

        f'<text x="24" y="30" fill="{GOLD}" '
        f'font-family="monospace" font-size="13">'
        f'mirian@github:~$ grow</text>',

        f'<line x1="24" y1="43" x2="576" y2="43" '
        f'stroke="{GOLD}" stroke-opacity="0.6"/>',
    ]

    for index, line in enumerate(lines):
        baseline = START_Y + index * LINE_HEIGHT
        clip_id = f"flower-line-{index}"
        reveal_width = len(line) * 8.5
        begin = index * 0.12

        parts.append(
            f'<clipPath id="{clip_id}" '
            f'clipPathUnits="userSpaceOnUse">'
            f'<rect x="{START_X}" y="{baseline - FONT_SIZE}" '
            f'width="0" height="{LINE_HEIGHT + 2}">'
            f'<animate attributeName="width" '
            f'from="0" to="{reveal_width}" '
            f'dur="0.5s" begin="{begin:.2f}s" '
            f'fill="freeze"/>'
            f'</rect></clipPath>'
        )

        if index < 11:
            color = PINK
        elif index < 18:
            color = GOLD
        else:
            color = CREAM

        parts.append(
            f'<text x="{START_X}" y="{baseline}" '
            f'xml:space="preserve" '
            f'font-family="monospace" '
            f'font-size="{FONT_SIZE}" '
            f'fill="{color}" '
            f'clip-path="url(#{clip_id})">'
            f'{html.escape(line)}</text>'
        )

    parts.extend([
        f'<line x1="24" y1="443" x2="576" y2="443" '
        f'stroke="{GOLD}" stroke-opacity="0.6"/>',

        f'<text x="24" y="463" fill="{CREAM}" '
        f'font-family="monospace" font-size="11">'
        f'[ creating beyond the surface ]</text>',

        f'<text x="576" y="463" fill="{GOLD}" '
        f'font-family="monospace" font-size="11" '
        f'text-anchor="end">M.U.</text>',

        "</svg>",
    ])

    return "\n".join(parts)


if __name__ == "__main__":
    repository = Path(__file__).resolve().parent.parent
    output_file = repository / "ascii-portrait.svg"

    output_file.write_text(make_svg(), encoding="utf-8")
    print(f"Flower created successfully: {output_file}")
