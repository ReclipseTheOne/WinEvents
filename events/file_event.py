from .event import Event


class FileEvent(Event):
    """Base class for file system events."""

    def __init__(self, event_type, path, context=None):
        """
        Initialize a file event.

        Args:
            event_type (str): The type of the file event
            path (str): The file system path involved in the event
            context (dict, optional): Additional context data for the event
        """
        super().__init__(event_type, context)
        self.path = path

    def __str__(self):
        return f"{self.__class__.__name__}(type='{self.type}', path='{self.path}', context={self.context})"
