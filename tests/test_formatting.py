import pytest
from utils.formatting import format_size, format_timestamp

@pytest.mark.parametrize("input_size, human_readable, expected_output", [
    (11024, True, "10.8K"),
    (2048, True, "2.0K"),
    (0, True, "0"),
    (1024, False, "1024"),
])
def test_format_size(input_size, human_readable, expected_output):
    assert format_size(input_size, human_readable) == expected_output

@pytest.mark.parametrize("input_timestamp, expected_output", [
    (1699950453, " Nov 14 13:57"),
    (1699941437, " Nov 14 11:27"),
    (0, " Jan 01 05:30"),
    (3600, " Jan 01 06:30"),
])
def test_format_timestamp(input_timestamp, expected_output):
    assert format_timestamp(input_timestamp) == expected_output
