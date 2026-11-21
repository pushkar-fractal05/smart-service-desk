class ServiceRequest:

    def __init__(self, request_id, employee_name,
                 issue, priority):

        self.request_id = request_id
        self.employee_name = employee_name
        self.issue = issue
        self.priority = priority
        self.status = "OPEN"

    