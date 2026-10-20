
from pathlib import Path
from urllib.request import Request, urlopen

USERNAME = "mirianukeje"
BURGUNDY = "6E263F"

GRAPH_URL = (
    f"https://ghchart.rshah.org/{BURGUNDY}/{USERNAME}"
)


def download_contribution_graph():
    repository = Path(__file__).resolve().parent.parent
    output_file = repository / "contribution-heatmap.svg"

    request = Request(
        GRAPH_URL,
        headers={"User-Agent": "Mirian-GitHub-Profile"},
    )

    try:
        with urlopen(request, timeout=30) as response:
            image_data = response.read()

        if b"<svg" not in image_data[:1000].lower():
            raise ValueError(
                "The server did not return an SVG image."
            )

        output_file.write_bytes(image_data)

        print("Contribution heatmap created successfully!")
        print(f"Saved to: {output_file}")

    except Exception as error:
        print("Could not download the contribution graph.")
        print(f"Details: {error}")


if __name__ == "__main__":
    download_contribution_graph()
