import pathlib

from . import args as argsmod
from . import logging as logmod
from . import templates

__project_name__ = "yourtactics"


def main() -> int:
    args = argsmod.parse_args()

    logmod.configure_logging(args.verbose)

    for project in templates.get_all_templates():
        for item in templates.get_templates(project):
            path = pathlib.Path(project) / item["path"]
            path.parent.mkdir(parents=True, exist_ok=True)

            template_path = templates.get_template_path(item["template"])
            logmod.logging.debug(f"Reading template: {template_path}")
            logmod.logging.debug(f"Writing to: {path.resolve()}")

            rendered = templates.render_template(item["template"])
            path.write_text(rendered)

    return 0
