@"
# TaskFlow — A Database-Driven Task Management System (CLI)

TaskFlow is a persistent, database-backed task management application built in Python.  
It provides full CRUD operations, task analysis, date-based filtering, and a clean modular architecture designed to reflect real backend engineering patterns.

TaskFlow stores all tasks in SQLite, ensuring data is permanent, structured, and safely queryable.

## Features

### Persistent Storage (SQLite)
All tasks are stored in a SQLite database with fields:
- id
- title
- description
- priority
- status
- deadline
- created_at
- updated_at

Timestamps are saved in a consistent format (YYYY-MM-DD HH:MM:SS) to avoid parsing conflicts.

### Full CRUD Operations
TaskFlow supports:
- Create new tasks
- Read tasks (all, by ID, by filters)
- Update any field (title, description, priority, status, deadline)
- Delete tasks

All updates automatically refresh the updated_at timestamp.

### Smart Date Handling
TaskFlow automatically converts deadline strings into real date objects using defensive logic:
- Converts only if value is a string
- Avoids double-parsing
- Ensures safe comparisons (date == date, date > date)

This powers:
- due today
- future tasks
- overdue tasks

### Task Analyzer
A dedicated analyser module provides:
- Search by keyword
- Count tasks by status
- Count tasks by priority
- Group tasks by update time
- Completion statistics
- Sort by priority
- Task summary
- Sort by status

### Clean CLI Interface
The CLI provides:
- A main menu
- Submenus for CRUD
- Submenus for analysis
- Clear messages for empty results
- Consistent formatting

### Summary (json)
- the summary will be saved automatically ,on the moment you enter analysis menu
- you can review summary with tool provided such (review summary, review based on date)

### Modular Architecture
TaskFlow is structured like a real backend system:

```
TaskFlow/
│
├── DATA/
│   ├── database.py        # DB connection + schema
│   ├── loader.py          # Load all tasks from DB for analysis
│   ├── module.py          # Task class for structured task objects
│   └── summary_json.py    # Save/load summaries with timestamp keys
│
├── OPERATIONS/
│   ├── add_tasks.py          
│   ├── delete_task.py
│   ├── update_tasks.py
│   └── helper/            # Shared search + utility functions
│
├── LOGIC/
│   ├── analyser.py        # Analysis logic 
│   └── analyser_helper.py # Extra analysis functions
│
├── UTILS/
│   └── tools.py           # Fast search + utility functions
│
└── main.py                # CLI entry point
```



This separation mirrors real backend service layers:
- DATA → database layer
- OPERATIONS → controllers
- LOGIC → business logic
- UTILS → helpers
- main.py → router / interface

## Installation

git clone https://github.com/yourusername/TaskFlow.git
cd TaskFlow
python main.py

Requires Python 3.10+.

## Usage

Run the program:

python main.py

You can:
- Add tasks
- Edit tasks
- Mark tasks as completed
- Delete tasks
- Search tasks
- View tasks due today
- View future tasks
- Analyze your productivity

## Key Engineering Concepts Demonstrated

TaskFlow showcases:
- SQLite integration
- CRUD architecture
- Defensive coding 
- Timestamp normalization
- Modular project structure
- CLI UX design
- Data analysis patterns
- Real backend thinking

## Future Improvements 
- Tag system
- Sorting options
- Export to CSV
- Priority-based reminders
- CLI color formatting

## License
MIT License.
Copyright (c) 2026 RaijinCode

"@ | Out-File -FilePath README.md -Encoding UTF8
