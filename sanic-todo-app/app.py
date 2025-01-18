from sanic import Sanic
from sanic.response import json

app = Sanic("ToDoApp")

tasks = []

@app.post("/add")
async def add_task(request):
    task = request.json.get("task")
    if not task:
        return json({"error": "Task is required!"}, status=400)
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "task": task})
    return json({"message": "Task added!", "task": {"id": task_id, "task": task}})

# Route to get all tasks
@app.get("/tasks")
async def get_tasks(request):
    return json({"tasks": tasks})

# Route to delete a task
@app.delete("/delete/<task_id:int>")
async def delete_task(request, task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return json({"message": f"Task with id {task_id} deleted!"})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
