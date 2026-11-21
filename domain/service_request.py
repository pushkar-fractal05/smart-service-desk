from domain.exceptions import InvalidPriorityError, RequestAlreadyResolvedError


class ServiceRequest:
    ALLOWED_PRIORITIES = {"LOW", "MEDIUM", "HIGH"}
    ALLOWED_STATUSES = {"OPEN", "RESOLVED"}

    def __init__(self, request_id, employee_name, issue, priority, status="OPEN"):
        self.request_id = request_id.strip()
        self.employee_name = employee_name.strip()
        self.issue = issue.strip()
        self.priority = priority.strip().upper()
        self.status = status.strip().upper()

        if self.priority not in self.ALLOWED_PRIORITIES:
            raise InvalidPriorityError("Priority must be LOW, MEDIUM or HIGH.")

        if self.status not in self.ALLOWED_STATUSES:
            raise ValueError("Status must be OPEN or RESOLVED.")

        if not self.request_id or not self.employee_name or not self.issue:
            raise ValueError("Request ID, employee name and issue cannot be empty.")

    def resolve(self):
        """Apply the domain rule: an OPEN request can become RESOLVED."""
        if self.status == "RESOLVED":
            raise RequestAlreadyResolvedError(
                f"Request {self.request_id} is already RESOLVED."
            )
        self.status = "RESOLVED"

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "issue": self.issue,
            "priority": self.priority,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            request_id=data["request_id"],
            employee_name=data["employee_name"],
            issue=data["issue"],
            priority=data["priority"],
            status=data.get("status", "OPEN"),
        )

    def __str__(self):
        return (
            f"{self.request_id} | {self.employee_name} | {self.issue} | "
            f"{self.priority} | {self.status}"
        )