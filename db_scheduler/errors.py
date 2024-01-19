class DBTimerException(Exception):
    """
    The base exception for all DB Timer errors.
    """

class DatabaseConnectionException(DBTimerException):
    """
    Raised when a connection to the database fails.
    """

class DatabaseShutdownException(DBTimerException):
    """
    Raised when an issue occurs trying to shutdown the database.
    """

class TimerException(Exception):
    """
    Raised when an error occurs with creating, starting or deleting a Timer.
    """
