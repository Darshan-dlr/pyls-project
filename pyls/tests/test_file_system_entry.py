import pytest
from pyls.models.file_system_entry import FileSystemEntry

def test_invalid_json_data_missing_field(invalid_json_data_missing_field):
    with pytest.raises(ValueError, match="Validation error during creation from JSON: Error: Missing mandatory fields."):
        FileSystemEntry.from_json(invalid_json_data_missing_field)

def test_invalid_json_data_invalid_type(invalid_json_data_invalid_type):
    with pytest.raises(ValueError, match="Validation error during creation from JSON: Error: Incorrect data types."):
        FileSystemEntry.from_json(invalid_json_data_invalid_type)
#
def test_invalid_json_data_contents_unexpected_field(invalid_json_data_contents_unexpected_field):
    with pytest.raises(ValueError, match="Validation error during creation from JSON: Error in content entry: Error: Unexpected fields found: invalid_field"):
        FileSystemEntry.from_json(invalid_json_data_contents_unexpected_field)

def test_valid_json_data(valid_json_data):
    try:
        instance = FileSystemEntry.from_json(valid_json_data)
        assert instance.name == "example"
        assert instance.size == 100
        assert instance.time_modified == 123456789
        assert instance.permissions == "rw-r--r--"
        assert len(instance.contents) == 1
        assert instance.contents[0].name == "file1"
        assert instance.contents[0].size == 50
        assert instance.contents[0].time_modified == 123456788
        assert instance.contents[0].permissions == "rw-r--r--"
    except ValueError:
        pytest.fail("Unexpected ValueError")
