# py-ad-cli

A command-line tool for weather, quotes, and todo management.

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI:

```bash
python main.py [COMMAND]
```

### Weather

Get weather information for a place:

```bash
python main.py get-weather "City Name"
```

### Random Quote

Show a random quote:

```bash
python main.py test
```

### Todos

Manage your todos with the `todos` subcommands:

- Show all todos:
  ```bash
  python main.py todos show
  ```
- Add a new todo:
  ```bash
  python main.py todos add "Your todo title"
  ```
- Remove a todo by its number:
  ```bash
  python main.py todos remove <todo_number>
  ```
- Mark a todo as done:
  ```bash
  python main.py todos done <todo_number>
  ```

## Notes

- Todos are stored in `todos.json` in the current directory.
- If you encounter errors, ensure the required files exist and are readable.

## License

MIT
