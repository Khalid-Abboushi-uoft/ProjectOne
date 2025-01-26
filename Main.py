class GameEvent:
    """
    Represents a single event in the game.
    Attributes:
        command (str): The user command that triggered the event.
        current_location (str): The current location in the game.
        next_location (str): The next location in the game.
    """

    def __init__(self, command: str, current_location: str, next_location: str):
        """
        Initializes a GameEvent object with the given command and locations.
        """
        self.command = command
        self.current_location = current_location
        self.next_location = next_location

    def __str__(self):
        """
        Returns a string representation of the GameEvent.
        """
        return f"Command: {self.command}, From: {self.current_location}, To: {self.next_location}"


class EventLogger:
    """
    Logs all game events and tracks the event history.
    Attributes:
        events (list[GameEvent]): A list of logged GameEvent objects.
    """

    def __init__(self):
        """
        Initializes an EventLogger with an empty event log.
        """
        self.events = []

    def log_event(self, command: str, current_location: str, next_location: str):
        """
        Logs a new game event.
        """
        event = GameEvent(command, current_location, next_location)
        self.events.append(event)

    def get_event_history(self):
        """
        Returns the full history of logged events.
        """
        return self.events

    def print_event_history(self):
        """
        Prints all logged events in a readable format.
        """
        for event in self.events:
            print(event)
