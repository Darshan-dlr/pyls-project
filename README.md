# pyls-project

## Overview

The **pyls** project is a Python command-line tool, similar to the 'ls' command, allowing users to view information about a file system. The data is currently stored in the 'sample_json.json' file. **pyls** offers functionalities such as listing files in a table format, sorting files, and filtering based on specific criteria.

## Project Structure

The project follows a structured layout to maintain code organization and modularity.

```
project_root/
│
├── main.py
├── .gitignore
├── Readme.md
├── sample_json.json
│
├── core/
│ └── display.py
│
├── utils/
│ ├── formatting.py
│
├── models/
│ └── file_system_entry.py
│
└── tests/
├── test_file_system_entry.py
```


## Usage

### Prerequisites

- Python 3.7 or later

### Clone the repository:

   ```bash
   git clone https://github.com/Darshan-dlr/pyls-project.git
   cd project_root
   ```


### Running the Tool
To use the File System Viewer, run the main.py script with appropriate command-line arguments.

` python main.py [-h] [-l] [-r] [-t] [-H] [-a] [--filter {file,dir}] `


### Options
- -h, --help: Show help message and exit.
- -l, --list: List files in a table format.
- -r, --reverse: Print files in reverse order.
- -t, --sort-by-date: Sort files by date.
- -H, --human-readable: Show human-readable size format.
- -a, --all: Show hidden files.
- --filter {file,dir}: Filter files or directories.
