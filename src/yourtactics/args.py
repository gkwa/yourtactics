import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--templates",
        default="https://raw.githubusercontent.com/taylormonacelli/yourtactics/master/templates.yaml",
        help="URL or file path to the templates templates (supports https:// and file:// schemes)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    return parser.parse_args()
