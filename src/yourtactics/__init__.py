import pathlib

from . import main2

__project_name__ = "yourtactics"


def main() -> int:
    out = main2.render_template("go/Makefile.j2")
    path = pathlib.Path("dailycould/{{ cookiecutter.project_slug }}/Makefile")
    path.write_text(out)

    out = main2.render_template("go/Makefile2.j2")
    path = pathlib.Path("allnew/{{ cookiecutter.project_slug }}/Makefile")
    path.write_text(out)

    return 0
