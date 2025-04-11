# To-Do Application

---

## Live Deployed Links
- **Frontend**: [https://todo-frontend-kv7x.onrender.com/](https://todo-frontend-kv7x.onrender.com/)
- **Backend**: [https://todo-backendd-hdpm.onrender.com/](https://todo-backendd-hdpm.onrender.com/)

---

## API Endpoints
RESTful API endpoints for managing managing backend:

| Method | Endpoint                                      | Description                |
|--------|----------------------------------------------|----------------------------|
| GET    | `/api/v1/todo/`                            | Fetch all tasks            |
| POST   | `/api/v1/todo/create/`                     | Create a new task          |
| PUT    | `/api/v1/todo/<id>/` (e.g., `/api/v1/todo/2/`) | Update a task by ID        |
| DELETE | `/api/v1/todo/<id>/` (e.g., `/api/v1/todo/2/`) | Delete a task by ID        |
| POST    | `/api-token-auth`                             | Get user token              |

- **Base URL**: `https://todo-backendd-hdpm.onrender.com/`
- **Request Payload**: For POST and PUT, send `{ "title": "task name", "completed": false }`.
- **Response Format**: JSON, e.g., `{ "id": 1, "title": "Buy groceries", "completed": false }`.


## NOTE:
 debug = True is turned ON 