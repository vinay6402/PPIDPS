import csv
import re
import os

def remove_python_symbols(code):
    # remove python related symbols, indentation, variables, and underscores
    code = re.sub(r'[^\w\s]', ' ', code)
    print(code)
    code = re.sub(r'_', ' ', code)
    code = re.sub(r'\s+', ' ', code).strip()
    return code

def get_words_from_code(code):
    # split the code into words
    words = code.split(' ')
    words = [x for x in words if len(x) > 1]
    return words

def save_to_csv(words, file_name):
    # write each word to a separate row in a csv file
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for word in words:
            writer.writerow([word])

def read_all_python_files(folder_path):
    unique_words = set()
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            with open(os.path.join(folder_path, filename), 'r') as file:
                code = file.read()
                code = remove_python_symbols(code)
                words = get_words_from_code(code)
                unique_words.update(words)
    return unique_words

def main():
    folder_path = "CodeCleaner/CodesDir"
    unique_words = read_all_python_files(folder_path)
    save_to_csv(unique_words, 'CodeCleaner/csv/unique_words.csv')
    print("Unique words saved to unique_words.csv")

if __name__ == '__main__':
    main()
