from ..file_event import FileEvent


class CreateFolderEvent(FileEvent):
    """Event representing the creation of a folder."""

    def __init__(self, path, context=None):
        """
        Initialize a create folder event.

        Args:
            path (str): The path of the created folder
            context (dict, optional): Additional context data for the event
        """
        super().__init__("create_folder", path, context)
