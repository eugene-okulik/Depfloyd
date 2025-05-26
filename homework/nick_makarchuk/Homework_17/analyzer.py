import os
import sys
import argparse

def extract_snippet(line, search_text):
    words = line.strip().split()
    snippet = []

    for idx, word in enumerate(words):
        if search_text in word:
            start = max(0, idx - 5)
            end = min(len(words), idx + 6)
            snippet = words[start:end]
            break

    return ' '.join(snippet)


def search_in_file(filepath, search_text):
    results = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for lineno, line in enumerate(f, start=1):
                if search_text in line:
                    snippet = extract_snippet(line, search_text)
                    results.append((filepath, lineno, snippet))
    except Exception as e:
        print(f"Ошибка при чтении файла {filepath}: {e}")
    return results


def main():
    parser = argparse.ArgumentParser(description='Лог-анализатор')
    parser.add_argument('logdir', help='Путь к папке с логами')
    parser.add_argument('--text', required=True, help='Текст для поиска')

    args = parser.parse_args()

    if not os.path.isdir(args.logdir):
        print(f"Указанная папка не существует: {args.logdir}")
        sys.exit(1)

    for filename in os.listdir(args.logdir):
        filepath = os.path.join(args.logdir, filename)
        if os.path.isfile(filepath):
            matches = search_in_file(filepath, args.text)
            for file, line_num, snippet in matches:
                print(f'{file} - строка {line_num}: {snippet}')


if __name__ == '__main__':
    main()
