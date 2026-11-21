from pathlib import Path

from application.request_service import RequestService
from infrastructure.file_repository import FileRepository
from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError,
    InvalidPriorityError,
    RequestAlreadyResolvedError,
    PersistenceError,
)


def display_request_details(request):
    print("\nRequest Details")
    print(f"Request ID       : {request.request_id}")
    print(f"Employee Name    : {request.employee_name}")
    print(f"Issue Description: {request.issue}")
    print(f"Priority         : {request.priority}")
    print(f"Status           : {request.status}")


def create_request(service):
    print("\n--- Create Service Request ---")
    request_id = input("Enter Request ID: ").strip()
    employee_name = input("Enter Employee Name: ").strip()
    issue = input("Enter Issue: ").strip()
    priority = input("Enter Priority (LOW/MEDIUM/HIGH): ").strip()

    try:
        request = service.create_request(
            request_id, employee_name, issue, priority
        )
        print("\nService Request created successfully.")
        print(request)
    except (DuplicateRequestError, InvalidPriorityError, ValueError) as exc:
        print(f"Error: {exc}")


def view_all_requests(service):
    print("\n--- All Service Requests ---")
    requests = service.view_requests()
    if not requests:
        print("No service requests found.")
        return
    for request in requests:
        print(request)


def search_request(service):
    print("\n--- Search Request ---")
    request_id = input("Enter Request ID: ").strip()
    try:
        display_request_details(service.search_request(request_id))
    except RequestNotFoundError as exc:
        print(exc)


def resolve_request(service):
    print("\n--- Resolve Request ---")
    request_id = input("Enter Request ID: ").strip()
    try:
        request = service.resolve_request(request_id)
        print(f"Request {request.request_id} has been RESOLVED successfully.")
    except (RequestNotFoundError, RequestAlreadyResolvedError) as exc:
        print(exc)


def show_menu():
    print("\n========== SMART SERVICE DESK SYSTEM ==========")
    print("1. Create Service Request")
    print("2. View All Requests")
    print("3. Search Request")
    print("4. Resolve Request")
    print("5. Exit")


def main():
    project_root = Path(__file__).resolve().parent
    repository = FileRepository(project_root / "data" / "requests.json")
    try:
        service = RequestService(repository)
    except PersistenceError as exc:
        print(f"Unable to load saved requests: {exc}")
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_request(service)
        elif choice == "2":
            view_all_requests(service)
        elif choice == "3":
            search_request(service)
        elif choice == "4":
            resolve_request(service)
        elif choice == "5":
            print("Exiting Smart Service Desk. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()