from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from itertools import repeat
import logging
from datetime import datetime
from pathlib import Path

import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException
from rich import inspect
from rich.logging import RichHandler
from rich.default_styles import DEFAULT_STYLES


class RichColorHandler(RichHandler):
    def render(self, *, record, traceback, message_renderable):
        path = Path(record.pathname).name
        level = self.get_level_text(record)
        time_format = None if self.formatter is None else self.formatter.datefmt
        log_time = datetime.fromtimestamp(record.created)

        level_key = f"logging.level.{str(level).lower().strip()}"
        level_style = DEFAULT_STYLES[level_key]
        message_renderable.stylize(level_style)

        log_renderable = self._log_render(
            self.console,
            [message_renderable] if not traceback else [message_renderable, traceback],
            log_time=log_time,
            time_format=time_format,
            level=level,
            path=path,
            line_no=record.lineno,
            link_path=record.pathname if self.enable_link_path else None,
        )
        return log_renderable


logging.basicConfig(
    format="%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="[%X]",
    handlers=[RichColorHandler()],
)

ip_list = ['10.1.9.0/24', '10.1.10.0/27', '10.1.11.0/26', '10.1.12.0/24']

logging.debug(f"<<< Received output 192.168.100.1 {ip_list}")
logging.info(f">>> Connecting  192.168.100.1 {ip_list}")
logging.warning(f"Error connecting 192.168.100.1 {ip_list}")
logging.error(f"Error 192.168.100.1 {ip_list}")
logging.critical(f"Critical error 192.168.100.1 {ip_list}")
