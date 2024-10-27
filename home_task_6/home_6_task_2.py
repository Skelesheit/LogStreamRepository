import pytest


def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"


@pytest.fixture
def setup_files(tmp_path):
    file_1 = tmp_path / "file1.txt"
    file_2 = tmp_path / "file2.txt"
    output = tmp_path / "output.txt"
    file_1.write_text("Something in 1 file")
    file_2.write_text("Something in 2 file")
    return file_1, file_2, output


def test_merge_exists_files(setup_files):
    file_1, file_2, output = setup_files
    result = merge_and_write(file_1, file_2, output)
    assert result == "Something in 1 file Something in 2 file"


def test_merge_not_exists_file():
    result = merge_and_write("not_exist_file1.txt", "not_exist_file2.txt", "output.txt")
    assert result == "Один из файлов не найден"
