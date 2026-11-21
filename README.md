# Smart Service Desk Management System

## Problem statement
A company receives IT support requests from employees. This Python CLI application lets support staff create, view, search and resolve requests, while retaining request data between runs in a JSON file.

## Implemented features
- Create a request with Request ID, employee name, issue description and priority.
- Automatically set a new request's status to `OPEN`.
- Prevent duplicate Request IDs.
- View all requests.
- Search using Request ID and display all details.
- Resolve an `OPEN` request; prevent resolving an already `RESOLVED` request.
- Persist and reload requests using `data/requests.json`.
- Handle missing/empty JSON storage and expected user input errors.

## Concepts used
- **OOP:** `ServiceRequest` has attributes and behavior, including `resolve()`.
- **Exceptions:** custom exceptions represent duplicate IDs, missing requests, invalid priorities, already-resolved requests and persistence problems.
- **File handling:** `FileRepository` reads and writes JSON.
- **SRP:** domain, application, infrastructure and presentation code have separate responsibilities.
- **DIP (basic):** `RequestService` receives its repository as a constructor dependency rather than creating or opening a file itself.
- **DDD (basic):** `ServiceRequest` is the domain model; `RequestService` coordinates use cases; `FileRepository` is infrastructure.
- **Git:** work is developed on `development`, then merged into `main`.

## Folder structure
```text
smart-service-desk/
├── domain/
│   ├── __init__.py
│   ├── service_request.py
│   └── exceptions.py
├── application/
│   ├── __init__.py
│   └── request_service.py
├── infrastructure/
│   ├── __init__.py
│   └── file_repository.py
├── data/
│   └── requests.json
├── main.py
├── README.md
└── .gitignore
```

## Run the application
1. Open a terminal in the project root (`smart-service-desk`).
2. Run:
   ```bash
   python main.py
   ```
   On some systems, use `python3 main.py`.

No third-party packages are required.

## Branch and merge explanation
All implementation work is done on the `development` branch. After testing, switch to `main`, merge `development`, and push `main`. The development branch and its commits remain available as evidence of incremental work.

## Important design notes
- The domain model owns the `OPEN` to `RESOLVED` rule through `ServiceRequest.resolve()`.
- The domain model does not open or write JSON files.
- `FileRepository` is the only component responsible for JSON persistence.
- `main.py` handles menu input/output and delegates use cases to `RequestService`.