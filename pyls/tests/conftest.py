import pytest

from pyls.models.file_system_entry import FileSystemEntry


@pytest.fixture
def invalid_json_data_missing_field():
    return {"size": 100, "time_modified": 123456789, "permissions": "rw-r--r--"}

@pytest.fixture
def invalid_json_data_invalid_type():
    return {"name": "example", "size": "invalid", "time_modified": 123456789, "permissions": "rw-r--r--"}


@pytest.fixture
def invalid_json_data_contents_unexpected_field():
    return {
        "name": "example",
        "size": 100,
        "time_modified": 123456789,
        "permissions": "rw-r--r--",
        "contents": [{"name": "file", "size": 50, "time_modified": 123456789,"permissions": "rw-r--r--", "invalid_field": "value"}]
    }

@pytest.fixture
def valid_json_data():
    return {
        "name": "example",
        "size": 100,
        "time_modified": 123456789,
        "permissions": "rw-r--r--",
        "contents": [{"name": "file1", "size": 50, "time_modified": 123456788, "permissions": "rw-r--r--"}]
    }


@pytest.fixture
def sample_file_system_entry():
    return FileSystemEntry(
        name="root",
        size=4096,
        time_modified=1621267200,  # Assuming a Unix timestamp
        permissions="rwxr-xr-x",
        contents=[
            FileSystemEntry(name="interpreter", size=1024, time_modified=1621267300, permissions="-rw-r--r--"),
            FileSystemEntry(name=".gitignore", size=2048, time_modified=1621267400, permissions="-rw-r--r--"),
            FileSystemEntry(name="LICENSE", size=3072, time_modified=1621267500, permissions="-rw-r--r--"),
            FileSystemEntry(name="README.md", size=4096, time_modified=1621267600, permissions="rwxr-xr-x"),
            FileSystemEntry(name="ast", size=1536, time_modified=1621267700, permissions="-rw-r--r--", contents=[
                FileSystemEntry(name="trail.py", size=0, time_modified=1621267700, permissions="-rw-r--r--")]),
        ]
    )
