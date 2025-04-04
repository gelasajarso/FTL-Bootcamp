# Word Count in Text File: Write a program to count the occurrences of each word in a given 
# text file. Rotate: Modify the program to exclude common stop words from the word count. 
# There should be 4 function named as read_text_from_file(file_path), count_words(text), 
# print_word_count(word_count) and main(file_path)

import re
from collections import Counter

# List of common stop words to exclude from the count
STOP_WORDS = {"the", "is", "in", "and", "to", "of", "a", "that", "it", "on", "for", "with", 
              "as", "was", "at", "by", "an", "be", "this", "which", "or", "from", "but", "not"}

def read_text_from_file(file_path):
    """
    Reads the content of a text file.

    Parameters:
    file_path (str): Path to the text file.

    Returns:
    str: Content of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def count_words(text):
    """
    Counts the occurrences of each word in a given text, excluding common stop words.

    Parameters:
    text (str): The input text.

    Returns:
    dict: A dictionary with words as keys and their counts as values.
    """
    # Convert text to lowercase and extract words using regex
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    # Filter out stop words and count occurrences
    word_count = Counter(word for word in words if word not in STOP_WORDS)

    return word_count

def print_word_count(word_count):
    """
    Prints the word count in a readable format.

    Parameters:
    word_count (dict): Dictionary containing words and their respective counts.
    """
    for word, count in word_count.most_common():
        print(f"{word}: {count}")

def main(file_path):
    """
    Main function to read a file, count words, and print the word count.

    Parameters:
    file_path (str): Path to the text file.
    """
    text = read_text_from_file(file_path)
    word_count = count_words(text)
    print_word_count(word_count)

# Example usage:
# Replace 'sample.txt' with the actual file path
if __name__ == "__main__":
    main("sample.txt")
