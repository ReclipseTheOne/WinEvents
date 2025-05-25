from main import listener
from events import CreateFolderEvent

import log

@listener
def exampleListener(event):
    LOGGER = log.s_logger("Example Listener")
    if isinstance(event, CreateFolderEvent):
       # Code
