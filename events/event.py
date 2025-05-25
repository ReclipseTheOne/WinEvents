from abc import ABC


class Event(ABC):
    """Abstract base class for all events that holds context and type."""

    def __init__(self, event_type, context=None):
        """
        Initialize an event with type and optional context.

        Args:
            event_type (str): The type of the event
            context (dict, optional): Additional context data for the event
        """
        self.type = event_type
        self.context = context or {}

    def __str__(self):
        return f"{self.__class__.__name__}(type='{self.type}', context={self.context})"

    def __repr__(self):
        return self.__str__()
