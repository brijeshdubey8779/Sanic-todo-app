` # Sanic To-Do Application 📝  This is a simple **To-Do application** built using the [Sanic Framework](https://sanic.dev/en/). The application demonstrates how to use Sanic for asynchronous request handling in Python.  ---  ## Features 🚀 - Add a new task. - Retrieve all tasks. - Delete a task.  ---  ## Getting Started 🛠️  Follow these steps to set up and run the project locally.  ### Prerequisites 📋 - Python 3.7 or higher installed. - Basic knowledge of Python and HTTP requests.  ### Setup Instructions ⚙️  1. **Clone the repository**      ```bash    git clone https://github.com/your-username/sanic-todo-app.git    cd sanic-todo-app `

2.  **Create and activate a virtual environment**

    bash

    CopyEdit

    `python -m venv venv  # Create virtual environment source venv/bin/activate  # Activate on Linux/Mac venv\Scripts\activate     # Activate on Windows`

3.  **Install dependencies**

    bash

    CopyEdit

    `pip install sanic`

4.  **Run the application**

    bash

    CopyEdit

    `python app.py`

5.  **Access the application**  
    Open your browser or use Postman to access the following endpoints:

    - **Add Task**: `POST http://localhost:8000/add`
    - **Get All Tasks**: `GET http://localhost:8000/tasks`
    - **Delete Task**: `DELETE http://localhost:8000/delete/<task_id>`

---

## Endpoints 🛣️

### 1\. Add a Task

**POST** `/add`

- **Body**:

  json

  CopyEdit

  `{   "task": "Your task here" }`

- **Response**:

  json

  CopyEdit

  `{   "message": "Task added!",   "task": {     "id": 1,     "task": "Your task here"   } }`

### 2\. Get All Tasks

**GET** `/tasks`

- **Response**:

  json

  CopyEdit

  `{   "tasks": [     {       "id": 1,       "task": "Your task here"     }   ] }`

### 3\. Delete a Task

**DELETE** `/delete/<task_id>`

- **Response**:

  json

  CopyEdit

  `{   "message": "Task with id <task_id> deleted!" }`

---

## References 📖

- Sanic Documentation
- Official Guide to Setting Up Sanic
