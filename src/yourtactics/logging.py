import logging


def configure_logging(verbose):
    format = "%(levelname)s:%(filename)s:%(lineno)d:%(message)s"
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format=format)
