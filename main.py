from utils.weather import get_weather
from utils.random_quote import get_random_quote
from utils.todo import show_todos, add_todo, remove_todo, mark_todo_done
import typer

app = typer.Typer()
todo_app = typer.Typer(name="todos")


@app.command(name="get-weather", help="Get weather information for a place.")
def get_weather_command(place: str):
    """Fetch and display weather information for the given place."""
    try:
        weather_info = get_weather(place)
    except Exception as e:
        typer.echo(f"Error: {e}")


@app.command(name="test", help="Show a random quote.")
def test_command():
    """Display a random quote."""
    try:
        get_random_quote()
    except Exception as e:
        typer.echo(f"Error: {e}")

@todo_app.command(name="show", help="Show all todos.")
def todos_command():
    """Display all todos."""
    try:
        show_todos()
    except Exception as e:
        typer.echo(f"Error: {e}")

@todo_app.command(name="add", help="Add a new todo.")
def todos_command(todo_title: str):
    """Add a new todo with the given title."""
    try:
        add_todo(todo_title)
    except Exception as e:
        typer.echo(f"Error: {e}")

@todo_app.command(name="remove", help="Remove a todo by its number.")
def todos_command(todo_number: int):
    """Remove a todo by its number."""
    try:
        remove_todo(todo_number)
    except Exception as e:
        typer.echo(f"Error: {e}")

@todo_app.command(name="done", help="Mark a todo as done by its number.")
def todos_command(todo_number: int):
    """Mark a todo as done by its number."""
    try:
        mark_todo_done(todo_number)
    except Exception as e:
        typer.echo(f"Error: {e}")


app.add_typer(todo_app, name="todos", help="Manage your todos")

if __name__ == "__main__":
    app()
