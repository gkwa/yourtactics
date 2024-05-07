import pathlib

from . import args as argsmod
from . import logging as mylog
from . import templates

__project_name__ = "yourtactics"


def main() -> int:
    args = argsmod.parse_args()

    mylog.configure_logging(args.verbose)

    data = templates.get_templates_data(args.templates)
    if data is None:
        return 1

    for project, project_data in data.items():
        for item in project_data["templates"]:
            path = pathlib.Path(project) / item["path"]
            path.parent.mkdir(parents=True, exist_ok=True)

            rendered = templates.render_template(item["template"])
            path.write_text(rendered)

    return 0
