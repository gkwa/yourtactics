import logging
import pathlib
import urllib.parse

import jinja2
import requests
import yaml


def load_templates_data(file_path):
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError as e:
        logging.error(f"Error loading templates data: {e}")
        return None


def fetch_templates_data(templates_url):
    try:
        response = requests.get(templates_url)
        data = yaml.safe_load(response.text)
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching templates data: {e}")
        return None


def get_templates_data(templates: str):
    templates_basename = pathlib.Path(urllib.parse.urlparse(templates).path).name
    local_file = pathlib.Path(f"./{templates_basename}")
    if local_file.is_file():
        logging.debug(f"Loading templates from local file: {local_file}")
        return load_templates_data(local_file)

    parsed_url = urllib.parse.urlparse(templates)
    if not parsed_url.scheme:
        logging.debug(f"Loading templates from local file: {templates}")
        return load_templates_data(templates)
    elif parsed_url.scheme == "https":
        logging.debug(f"Fetching templates from URL: {templates}")
        return fetch_templates_data(templates)
    elif parsed_url.scheme == "file":
        file_path = pathlib.Path(parsed_url.path)
        if file_path.is_absolute():
            file_path = file_path.relative_to("/")
        logging.debug(f"Loading templates from file: {file_path}")
        return load_templates_data(file_path)
    else:
        logging.error(f"Unsupported scheme '{parsed_url.scheme}' in templates URL")
        return None


def get_template(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / "templates"
    loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_PATH)
    env = jinja2.Environment(loader=loader, keep_trailing_newline=True)
    return env.get_template(template_name)


def render_template(template_name, data=None):
    template = get_template(template_name)
    return template.render(data=data)
