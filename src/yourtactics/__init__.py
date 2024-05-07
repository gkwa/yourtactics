import pathlib

from . import logging as mylog
from . import main2
from .args import parse_args
from .templates import get_templates_data

__project_name__ = "yourtactics"


def main() -> int:
    args = parse_args()

    mylog.configure_logging(args.verbose)

    data = get_templates_data(args.templates)
    if data is None:
        return 1

    for project, project_data in data.items():
        for item in project_data["templates"]:
            out = main2.render_template(item["template"])
            path = pathlib.Path(project) / item["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(out)

    return 0
