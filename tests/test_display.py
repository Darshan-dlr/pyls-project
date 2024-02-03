from core.display import sort_files, display_detailed_file_list, display_files_names


def test_sort_files_by_name(sample_file_system_entry):
    sorted_files = sort_files(sample_file_system_entry.contents, reverse_order=False)
    assert sorted_files[0].name == '.gitignore'
    assert sorted_files[-1].name == 'interpreter'

def test_sort_files_reverse_order_by_name(sample_file_system_entry):
    sorted_files = sort_files(sample_file_system_entry.contents, reverse_order=True)
    assert sorted_files[0].name == 'interpreter'
    assert sorted_files[-1].name == '.gitignore'

def test_sort_files_by_time_modified(sample_file_system_entry):
    sorted_files = sort_files(sample_file_system_entry.contents, sort_by_date=True, reverse_order=False)    
    assert sorted_files[0].name == 'interpreter'
    assert sorted_files[-1].name == 'ast'

def test_sort_files_reverse_order_by_time_modified(sample_file_system_entry):
    sorted_files = sort_files(sample_file_system_entry.contents, sort_by_date=True, reverse_order=True)
    assert sorted_files[0].name == 'ast'
    assert sorted_files[-1].name == 'interpreter'

def test_display_detailed_file_list(capsys, sample_file_system_entry):
    display_detailed_file_list(sample_file_system_entry, show_hidden=True)
    captured = capsys.readouterr()
    
    assert 'interpreter' in captured.out
    assert '.gitignore' in captured.out
    assert 'LICENSE' in captured.out
    assert 'README.md' in captured.out
    assert 'ast' in captured.out

def test_display_files_names_hidden(capsys, sample_file_system_entry):
    display_files_names(sample_file_system_entry, show_hidden=True)
    captured = capsys.readouterr()

    assert 'interpreter' in captured.out
    assert '.gitignore' in captured.out
    assert 'LICENSE' in captured.out
    assert 'README.md' in captured.out
    assert 'ast' in captured.out

def test_display_files_names_non_hidden(capsys, sample_file_system_entry):
    display_files_names(sample_file_system_entry, show_hidden=False)
    captured = capsys.readouterr()

    assert 'interpreter' in captured.out
    assert 'ast' in captured.out
    assert '.gitignore' not in captured.out
    assert 'LICENSE'  in captured.out
    assert 'README.md' in captured.out

def test_display_files_names_filter_file(capsys, sample_file_system_entry):
    display_files_names(sample_file_system_entry, show_hidden=True, content_filter='file')
    captured = capsys.readouterr()

    assert '.gitignore' in captured.out
    assert 'LICENSE' in captured.out
    assert 'README.md' in captured.out
    assert 'ast' not in captured.out
    assert 'interpreter' in captured.out

def test_display_files_names_filter_dir(capsys, sample_file_system_entry):
    display_files_names(sample_file_system_entry, show_hidden=True, content_filter='dir')
    captured = capsys.readouterr()

    assert 'ast' in captured.out
    assert 'interpreter' not in captured.out
    assert '.gitignore' not in captured.out
    assert 'LICENSE' not in captured.out
    assert 'README.md' not in captured.out


def test_display_detailed_file_list_hidden(capsys, sample_file_system_entry):
    display_detailed_file_list(sample_file_system_entry, show_hidden=True)
    captured = capsys.readouterr()

    assert '.gitignore' in captured.out.split('\n')[0]
    assert 'interpreter' in captured.out.split('\n')[-2] 

def test_display_detailed_file_list_reverse(capsys, sample_file_system_entry):
    display_detailed_file_list(sample_file_system_entry, reverse_order=True)
    captured = capsys.readouterr()

    assert 'interpreter' in captured.out.split('\n')[0]
    assert 'LICENSE' in captured.out.split('\n')[-2]


def test_display_detailed_file_list_date_reverse(capsys, sample_file_system_entry):
    display_detailed_file_list(sample_file_system_entry, reverse_order=True, sort_by_date=True)
    captured = capsys.readouterr()

    assert 'ast' in captured.out.split('\n')[0]
    assert 'interpreter' in captured.out.split('\n')[-2]

def test_display_detailed_file_list_human_readable_size(capsys, sample_file_system_entry):
    display_detailed_file_list(sample_file_system_entry, human_readable=True)
    captured = capsys.readouterr()

    assert '3.0K' in captured.out
    assert '4.0K' in captured.out
    assert '1.5K' in captured.out
    assert '1.0K' in captured.out

