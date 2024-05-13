import pathlib

import jinja2

from .templates_data import data


def get_template_path(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / "templates"
    return TEMPLATES_PATH / template_name


def get_template(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / "templates"
    loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_PATH)
    env = jinja2.Environment(loader=loader, keep_trailing_newline=True)
    return env.get_template(template_name)


def render_template(template_name, data=None):
    template = get_template(template_name)
    return template.render(data=data)


def get_templates(name: str):
    return data.get(name, {}).get("templates", [])


def get_all_templates():
    return data.keys()
