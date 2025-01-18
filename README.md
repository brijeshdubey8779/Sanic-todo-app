# Sanic To-Do Application 📝 This is a simple

## To-Do Application built using the \[Sanic Framework\](https://sanic.dev/en/). The application demonstrates how to use Sanic for asynchronous request handling in Python.

## Features 🚀

- Add a new task.
- Retrieve all .
- Delete a task.

---

## Getting Started

🛠️ Follow these steps to set up and run the project locally.

### Prerequisites 📋

- Python 3.7 or higher installed.
- Basic knowledge of Python and HTTP requests.

### Setup Instructions ⚙️

1. Clone the repository

   ```bash git clone https://github.com/your-username/sanic-todo-app.git
   cd sanic-todo-app
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv     # Create virtual environment

   source venv/bin/activate    # Activate on Linux/Mac

   venv\Scripts\activate     # Activate on Windows
   ```

3. Install dependencies

   ```bash
   pip install sanic
   ```

4. Run the application

   ```bash
   python app.python
   ```

5. Access the application

   Open your browser or use Postman to access the following endpoints:

   - Add Task: \`POST http://localhost:8000/add\`

   - Get All Tasks: \`GET http://localhost:8000/tasks\`

   - Delete Task: \`DELETE http://localhost:8000/delete/\`

---

## Endpoints 🛣️

### 1\. Add a Task

POST `add\`

Body:

```json
{ "task": "Your task here" }
```

Response:

```json
{ "message": "Task added!", "task": { "id": 1, "task": "Your task here" } }
```

### 2\. Get All Tasks

GET `tasks`

Response:

```json
{ "tasks": [{ "id": 1, "task": "Your task here" }] }
```

### 3\. Delete a Task

DELETE `delete/`

Response:

```json
{ "message": "Task with id deleted!" }
```
