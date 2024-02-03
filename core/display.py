from typing import Optional, List

from models.file_system_entry import FileSystemEntry
from utils.formatting import format_size, format_timestamp


def should_include_item(item: FileSystemEntry, show_hidden: bool = False, content_filter: Optional[str] = None) -> bool:
    """
        Based on the conditions of show_hidden and content_filter, decide if an item should be included.

    Args:
        item (FileSystemEntry): File node from the data class.
        show_hidden (bool): Whether to show the hidden files or not.
        content_filter (Optional[str]): Filter the contents based on whether to show files or directories.

    Returns:
        bool: True if the item should be included, False otherwise.
    """
    return (show_hidden or not item.name.startswith('.')) and (content_filter is None or (content_filter == 'file' and not item.contents) or (content_filter == 'dir' and item.contents))


def sort_files(files: List[FileSystemEntry], reverse_order: bool = False, sort_by_date: bool = False) -> List[FileSystemEntry]:
    """
        Sort files based on specified conditions.

    Args:
        files (List[FileSystemEntry]): List of file nodes.
        reverse_order (bool): Whether to reverse the order of the list.
        sort_by_date (bool): Whether to consider time-modified for sorting.

    Returns:
        List[FileSystemEntry]: Sorted list of file nodes.
    """
    return sorted(files, key=lambda x: x.time_modified if sort_by_date else x.name, reverse=reverse_order)


def display_detailed_file_list(node: FileSystemEntry, show_hidden: bool = False, reverse_order: bool = False, sort_by_date: bool = False, human_readable: bool = False, content_filter: Optional[str] = None) -> None:
    """
        Print file details in table format for the provided root node, performing optional operations.

    Args:
        node (FileSystemEntry): File node from the data class.
        show_hidden (bool): Whether to show the hidden files.
        reverse_order (bool): Whether to reverse the order of the list.
        sort_by_date (bool): Whether to consider time-modified for sorting.
        human_readable (bool): Whether to convert the file size to human-readable format or not.
        content_filter (Optional[str]): Whether to print only the files or the directories under the node.
    """
    files = [item for item in node.contents if should_include_item(item, show_hidden, content_filter)]
    sorted_files = sort_files(files, reverse_order, sort_by_date)
    for file_node in sorted_files:
        print(f" {file_node.permissions}  {format_size(file_node.size, human_readable):>5}  {format_timestamp(file_node.time_modified)}  {file_node.name} ")


def display_files_names(node: FileSystemEntry, show_hidden: bool = False, content_filter: Optional[str] = None) -> None:
    """
        Prints only the name of the files and directories based on the content_filter value which exists under the passed root node.

    Args: 
        node (FileSystemEntry): File node from the data class.
        show_hidden (bool): Whether to show the hidden files or not.
        content_filter (Optional[str]): Filter the contents based on whether to show files or directories.
    """
    print(*[item.name for item in node.contents if should_include_item(item, show_hidden, content_filter)])
