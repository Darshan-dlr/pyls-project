# pyls-project

## Overview

The **pyls** project is a Python command-line tool, similar to the 'ls' command, allowing users to view information about a file system. The data is currently stored in the [sample_json.json](https://github.com/Darshan-dlr/pyls-project/blob/main/sample_json.json) file. pyls offers functionalities such as listing files in a table format, sorting files, and filtering based on specific criteria.

## Project Structure

The project follows a structured layout to maintain code organization and modularity.

```
pyls-project/
│
├── .gitignore
├── Readme.md
│
├── pyls/
│   ├── core/
│   │   └── display.py
│   │
│   ├── utils/
│   │   └── formatting.py
│   │
│   ├── models/
│   │   └── file_system_entry.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_display.py
│   │   ├── test_formatting.py
│   │   └── test_file_system_entry.py
│   │
│   ├── __init__.py
│   ├── __main__.py
│   └── sample_json.json



```


## Usage

### Prerequisites

- Python 3.7 or later
- Pytest 5.2.1 or later

### Clone the repository:

   ```bash
   git clone <repository-url>
   cd project_root
   ```


### Running the Tool
To use the File System Viewer, run the main.py script with appropriate command-line arguments.

` python main.py [-h] [-l] [-r] [-t] [-H] [-a] [--filter {file,dir}] `


### Options
- -h, --help: Show help message and exit.
- -l, --list-info: List detailed file info in table format.
- -r, --reverse: Print files in reverse order.
- -t, --sort-by-date: Sort files by date.
- -H, --human-readable: Show human-readable size format.
- -a, --all: Show hidden files.
- --filter {file,dir}: Filter files or directories.
- -d --display-tree: Show the tree structure.

### Bonus
- use `python -m pyls -d` to display the file tree structure
- additonal combination which works 
   - `pyls -a --filter=<dir/file>`
   - `pyls -l -a`