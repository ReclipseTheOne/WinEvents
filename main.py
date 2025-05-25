import os
import importlib
from events import CreateFolderEvent
from watchers.file_system_watcher import run_simple_fs_watcher

import log
from rites.logger import Logger
LOGGER = log.p_logger("Main")

LISTENERS = []

def load_listeners():
    listeners_dir = "listeners"
    for filename in os.listdir(listeners_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            mod_name = f"{listeners_dir}.{filename[:-3]}"
            mod = importlib.import_module(mod_name)
            LOGGER.info(f"Loading listener module: {mod_name}")
            for attr in dir(mod):
                fn = getattr(mod, attr)
                if callable(fn) and getattr(fn, "_is_listener", False):
                    LISTENERS.append(fn)


def dispatch(event):
    for listener in LISTENERS:
        listener(event)


def listener(fn):
    fn._is_listener = True
    return fn


if __name__ == "__main__":
    load_listeners()
    run_simple_fs_watcher(dispatch)