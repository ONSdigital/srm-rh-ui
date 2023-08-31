import logging
import sys

from structlog import configure
from structlog.processors import JSONRenderer, TimeStamper, format_exc_info
from structlog.stdlib import LoggerFactory, add_log_level, filter_by_level
from structlog.contextvars import merge_contextvars


def logger_initial_config(log_level="INFO", logger_format="%(message)s", logger_date_format="%Y-%m-%dT%H:%M%s") -> None:
    def add_service(_logger: logging.Logger, _method_name: str, event_dict: dict) -> dict:
        """
        Add the service name to the event dict.
        This adds `service: 'rh-ui'` to all log lines.
        """
        event_dict["service"] = "rh-ui"
        return event_dict

    logging.basicConfig(stream=sys.stdout, level=log_level, format=logger_format)

    def add_severity_level(_logger: logging.Logger, method_name: str, event_dict: dict) -> dict:
        """
        Add the log level to the event dict.
        """
        if method_name == "warn":
            # The stdlib has an alias, we always want "warning" in full
            method_name = "warning"

        event_dict["severity"] = method_name
        return event_dict

    def parse_exception(_, __, event_dict: dict):
        exception = event_dict.get("exception")
        if exception:
            event_dict["exception"] = exception.replace('"', "'").split("\n")
        return event_dict

    renderer_processor = JSONRenderer(indent=None)

    processors = [
        merge_contextvars,
        add_severity_level,
        add_log_level,
        filter_by_level,
        add_service,
        format_exc_info,
        TimeStamper(fmt=logger_date_format, utc=True, key="created_at"),
        parse_exception,
        renderer_processor,
    ]
    configure(
        logger_factory=LoggerFactory(),
        processors=processors,  # type: ignore
        cache_logger_on_first_use=True,
    )
