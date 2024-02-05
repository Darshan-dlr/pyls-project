# pyls-project

## Overview

The **pyls** project is a Python command-line tool, similar to the 'ls' command, allowing users to view information about a file system. The data is currently stored in the [sample_json.json](https://github.com/Darshan-dlr/pyls-project/blob/main/pyls/sample_json.json) file. pyls offers functionalities such as listing files in a table format, sorting files, and filtering based on specific criteria.

## Project Structure

The project follows a structured layout to maintain code organization and modularity.

```
pyls-project/
│
├── .gitignore
├── Readme.md
├── pyproject.toml
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
│  

```


## Usage

### Prerequisites

- Python 3.7 or later
- setuptools 65.6.3 or later
- pytest 5.2.1 or later

### Clone the repository:

   ```
   git clone https://github.com/Darshan-dlr/pyls-project.git
   cd pyls-project
   ```


### Running the Tool

- To display file system names:
`python -m pyls -a --filter file`

- To display file system detailed information:
`python -m pyls -l -a -r -t -H --filter dir`

_Adjust the command options based on your preferences._

- For detialed info of arguments use 
`python -m pyls -h`

### Installing the tool

* After cloning the repository and navigating into the pyls-project directory, use the following command to install:

`pip install .`


* Now we can directly use the command like:

`pyls -a --filter file`

`pyls -l -a -r -t -H --filter dir`



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
- Included validation for the json file that will be utilised.
- Use `python -m pyls -d` to display the file tree structure.
- Additonal combination which works 

      1. pyls -a --filter=<dir/file>
      2. pyls -l -a
