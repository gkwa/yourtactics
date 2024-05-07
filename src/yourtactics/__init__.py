import pathlib

from . import main2

__project_name__ = "yourtactics"


def main() -> int:
    templates = [
        {
            "template": "go/Makefile.j2",
            "path": "dailycould/{{ cookiecutter.project_slug }}/Makefile",
        },
        {
            "template": "go/Makefile2.j2",
            "path": "allnew/{{ cookiecutter.project_slug }}/Makefile",
        },
        {
            "template": "go/Makefile2.j2",
            "path": "itsvermont/{{ cookiecutter.project_slug }}/Makefile",
        },
        {
            "template": "cookiecutter/cookiecutter.json",
            "path": "dailycould/cookiecutter.json",
        },
        {
            "template": "cookiecutter/cookiecutter.json",
            "path": "allnew/cookiecutter.json",
        },
        {
            "template": "cookiecutter/cookiecutter.json",
            "path": "itsvermont/cookiecutter.json",
        },
        {
            "template": "go/goreleaser/goreleaser.yaml.j2",
            "path": "dailycould/{{ cookiecutter.project_slug }}/.goreleaser.yaml",
        },
        {
            "template": "go/goreleaser/goreleaser.yaml.j2",
            "path": "allnew/{{ cookiecutter.project_slug }}/.goreleaser.yaml",
        },
        {
            "template": "go/goreleaser/goreleaser.yaml.j2",
            "path": "itsvermont/{{ cookiecutter.project_slug }}.goreleaser.yaml",
        },
    ]

    for item in templates:
        out = main2.render_template(item["template"])
        path = pathlib.Path(item["path"])
        path.write_text(out)

    return 0
