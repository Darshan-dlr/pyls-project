import argparse
import json

from core.display import display_detailed_file_list, display_files_names
from models.file_system_entry import FileSystemEntry 


def main():
    parser = argparse.ArgumentParser(description="pyls",
                                    epilog="Use this scirpt to view file system information.",
                                    usage="python script.py [-h] [-l] [-r] [-t] [-H] [-a]",
                                    )
    parser.add_argument("-a", "--all", action="store_true", help="Show hidden files")
    parser.add_argument("-l", "--list-info", action="store_true", help="List detailed file info in table format")
    parser.add_argument("-r", "--reverse", action="store_true", help="Print files in reverse order")
    parser.add_argument("-t", "--sort-by-date", action="store_true", help="Sort files by date")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Show human-readable size format")
    parser.add_argument("--filter", choices=['file', 'dir'], help="Filter files or directories")

    args = parser.parse_args()

    with open('sample_json.json', 'r') as file:
        json_data = json.load(file)

    try:
        file_tree = FileSystemEntry.from_json(json_data)
    except ValueError as e:
        raise ValueError(f"Validation error: {str(e)}")

    # print(file_tree.display_file_tree_structure()) # to check the file tree structure

    if args.list_info:
        display_detailed_file_list(file_tree, args.all, reverse_order=args.reverse, 
                                   sort_by_date=args.sort_by_date, human_readable=args.human_readable,
                                   content_filter=args.filter)
    else:
        display_files_names(file_tree, args.all, content_filter=args.filter)

if __name__ == "__main__":
    main()
