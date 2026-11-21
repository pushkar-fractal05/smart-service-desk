from domain.service_request import ServiceRequest
from domain.exceptions import DuplicateRequestError, RequestNotFoundError


class RequestService:
    """Coordinates service-request use cases; it does not perform file I/O."""

    def __init__(self, repository):
        # The repository is supplied from outside (dependency injection).
        self.repository = repository
        self.requests = self.repository.load_all()

    def create_request(self, request_id, employee_name, issue, priority):
        if any(r.request_id == request_id.strip() for r in self.requests):
            raise DuplicateRequestError(
                f"Request ID {request_id.strip()} already exists."
            )

        request = ServiceRequest(request_id, employee_name, issue, priority)
        self.requests.append(request)
        self.repository.save_all(self.requests)
        return request

    def view_requests(self):
        return list(self.requests)

    def search_request(self, request_id):
        for request in self.requests:
            if request.request_id == request_id.strip():
                return request
        raise RequestNotFoundError(f"Request {request_id.strip()} not found.")

    def resolve_request(self, request_id):
        request = self.search_request(request_id)
        request.resolve()
        self.repository.save_all(self.requests)
        return request