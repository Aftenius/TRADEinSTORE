FILE_OLD = 'OLD_list/post_tg_1.txt'
FILE_NEW = 'NEW_list/post_tg_1.txt'

def read_file(file_path):
    """Чтение содержимого файла и возврат списка строк."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def compare_files(old_file, new_file):
    """Сравнение содержимого двух файлов и возврат уникальных строк из второго файла."""
    content1 = set(read_file(old_file))
    content2 = set(read_file(new_file))

    return content2 - content1

def copy_and_clear_file(new_file, old_file):
    """Копирование содержимого из new_file в old_file и очистка new_file."""
    # Читаем содержимое new_file
    with open(new_file, 'r', encoding='utf-8') as source_file:
        data = source_file.read()

    # Записываем прочитанные данные в old_file
    with open(old_file, 'w', encoding='utf-8') as destination_file:
        destination_file.write(data)

    # Очищаем содержимое new_file
    with open(new_file, 'w', encoding='utf-8') as source_file:
        source_file.write('')


def main():
    differences = compare_files(FILE_OLD, FILE_NEW)
    copy_and_clear_file(FILE_NEW, FILE_OLD)

    for line in differences:
        print(line)


if __name__ == "__main__":
    main()
