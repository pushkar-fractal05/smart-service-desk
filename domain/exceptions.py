class DuplicateRequestError(Exception):
    """Raised when a request ID is already in use."""


class RequestNotFoundError(Exception):
    """Raised when a requested service request does not exist."""


class InvalidPriorityError(Exception):
    """Raised when a priority is not LOW, MEDIUM, or HIGH."""


class RequestAlreadyResolvedError(Exception):
    """Raised when an attempt is made to resolve an already resolved request."""


class PersistenceError(Exception):
    """Raised when stored request data cannot be read or written safely."""