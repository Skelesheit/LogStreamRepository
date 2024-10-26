def write_text_to_file(file_name: str, text: str, encoding_system='utf-8'):
    with open(file_name, 'a+', encoding=encoding_system) as file:
        file.write('\n' + text)

    with open(file_name, mode='r', encoding=encoding_system) as file:
        lines = file.readlines()
        lines_ans = list()
        for index, line in enumerate(lines):
            if index % 2 == 0:
                lines_ans.append(line.strip())
    return lines_ans


if __name__ == '__main__':
    answer = write_text_to_file('text', 'hello world')
    for i in range(len(answer)):
        print(i * 2, answer[i])
