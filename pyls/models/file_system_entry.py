from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FileSystemEntry:
    """
        Represents a file system entry.

    Attributes:
    - name: The name of the entry.
    - size: The size of the entry.
    - time_modified: The modification time of the entry.
    - permissions: The permissions of the entry.
    - contents: Optional list of FileSystemEntry instances representing contents.
    """
    name: str
    size: int
    time_modified: int
    permissions: str
    contents: Optional[List['FileSystemEntry']] = field(default_factory=list)

    @classmethod
    def from_json(cls, json_data):
        """
            Create an instance of FileSystemEntry from JSON data.

        Args:
        - json_data: JSON data representing the FileSystemEntry.

        Returns:
        - An instance of FileSystemEntry.
        """
        is_valid, validation_result = cls._validate_dataclass(json_data)
        if not is_valid:
            raise ValueError(f"Validation error during creation from JSON: {validation_result}")

        instance = cls(
            json_data['name'],
            json_data['size'],
            json_data['time_modified'],
            json_data['permissions'],
            [cls.from_json(item) for item in json_data.get('contents', [])] if 'contents' in json_data else None
        )
        return instance

    @classmethod
    def _validate_dataclass(cls, json_data):
        """
            Validate JSON data for FileSystemEntry.

        Args:
        - json_data: JSON data representing the FileSystemEntry.

        Returns:
        - Tuple: (is_valid: bool, validation_result: str)
        """
        mandatory_fields = {'name', 'size', 'time_modified', 'permissions'}
        if not all(field in json_data for field in mandatory_fields):
            return False, "Error: Missing mandatory fields."

        if not (isinstance(json_data['name'], str) and isinstance(json_data['size'], int) and
                isinstance(json_data['time_modified'], int) and isinstance(json_data['permissions'], str)):
            return False, "Error: Incorrect data types."

        expected_fields = {'name', 'size', 'time_modified', 'permissions', 'contents'}
        actual_fields = set(json_data.keys())
        unexpected_fields = actual_fields - expected_fields
        if unexpected_fields:
            return False, f"Error: Unexpected fields found: {', '.join(unexpected_fields)}"

        # Check optional 'contents' field data and validate each content entry
        if 'contents' in json_data and json_data['contents'] is not None:
            if not isinstance(json_data['contents'], list):
                return False, "Error: 'contents' should be a list."

            for content_data in json_data['contents']:
                is_valid_content, content_validation_result = cls._validate_dataclass(content_data)
                if not is_valid_content:
                    return False, f"Error in content entry: {content_validation_result}"

                unexpected_content_fields = set(content_data.keys()) - expected_fields
                if unexpected_content_fields:
                    return False, f"Error: Unexpected fields found in content entry: {', '.join(unexpected_content_fields)}"

        return True, "Dataclass validation successful"


    def display_file_tree_structure(self, indent: int = 0) -> None:
        """
            Display the file tree structure starting from this FileSystemEntry with proper formatting.

        Args:
            indent (int): Indentation level for proper tree structure.
        """
        print(f"{' ' * indent}{self.name}")
        for content in self.contents:
            if content.contents:
                content.display_file_tree_structure(indent + 4)
            else:
                print(f"{' ' * (indent + 4)}|-- {content.name}")