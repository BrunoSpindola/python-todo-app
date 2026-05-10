# Python To-Do App

A command-line task manager built in Python, focused on software engineering fundamentals: file-based data persistence, input validation, and structured error handling.

---

## Features

- Add, list, edit, and complete tasks via CLI
- Persistent storage using local file I/O — tasks survive between sessions
- Input validation with structured error handling
- Clean command loop with exit control

---

## How to Run

```bash
git clone https://github.com/BrunoSpindola/python-todo-app.git
cd python-todo-app
python cli.py
```

---

## Usage

```
Type a command: add, show, edit, complete or exit

> add Buy groceries
> show
> edit 1
> complete 1
> exit
```

---

## Technologies

- Python 3
- File I/O (text file persistence)
- Standard library only — no external dependencies

---

## Roadmap

- [ ] Migrate storage to SQLite database
- [ ] Add priority levels and due dates
- [ ] Build a minimal web interface

---

## About

Part of an active software engineering portfolio.
Project developed during Python Developer Bootcamp (Udemy), extended with additional error handling and validation logic.

**Author:** [Bruno Spindola](https://github.com/BrunoSpindola) · [LinkedIn](https://linkedin.com/in/brunospindola)
