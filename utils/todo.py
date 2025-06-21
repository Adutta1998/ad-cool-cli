import json
from random import randint
import os
from rich.table import Table
from rich.console import Console


def show_todos():
    try:
        with open("todos.json", "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No todos found.")
        return
    if not todos:
        print("No todos found.")
    else:
        table = Table(title="Todos")
        table.add_column("Title", style="cyan", no_wrap=True)
        table.add_column("Number", style="magenta")
        table.add_column("Is Done?")
        for todo in todos:
            table.add_row(todo["title"], str(todo["number"]), "✅" if todo["done"] else "❌")
        console = Console()
        console.print(table)


def add_todo(todo_title: str):
    todo = {"title": todo_title, "done": False, "number": randint(1, 1000)}
    try:
        with open("todos.json", "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        todos = []
    todos.append(todo)
    try:
        with open("todos.json", "w") as file:
            json.dump(todos, file)
        print(f"Todo '{todo_title}' added with number {todo['number']}.")
    except Exception as e:
        print(f"Error saving todo: {e}")


def remove_todo(todo_number: int):
    try:
        with open("todos.json", "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No todos found.")
        return
    numbers = [todo["number"] for todo in todos]
    if todo_number not in numbers:
        print(f"No todo found with number {todo_number}. Possible values: {numbers}")
        return
    todos = [todo for todo in todos if todo["number"] != todo_number]
    try:
        with open("todos.json", "w") as file:
            json.dump(todos, file)
        print(f"Todo with number {todo_number} removed.")
    except Exception as e:
        print(f"Error saving todo: {e}")

def mark_todo_done(todo_number: int):
    try:
        with open("todos.json", "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No todos found.")
        return
    numbers = [todo["number"] for todo in todos]
    if todo_number not in numbers:
        print(f"No todo found with number {todo_number}. Possible values: {numbers}")
        return
    for todo in todos:
        if todo["number"] == todo_number:
            todo["done"] = True
            break
    try:
        with open("todos.json", "w") as file:
            json.dump(todos, file)
        print(f"Todo with number {todo_number} marked as done.")
    except Exception as e:
        print(f"Error saving todo: {e}")
