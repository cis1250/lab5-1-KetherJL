import re

# This is a function that checks if a text qualifies as a sentence.
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# Cleans sentence
def get_sentence():
    user_sentence = input("Enter a sentence: ")
    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    cleaned = re.sub(r'[^\w\s]', '', user_sentence)
    split_sentence = cleaned.lower().split()
    return split_sentence, user_sentence

def calculate_frequency(split_sentence):
    list_a = [] #for words
    list_b = [] #for frequencies
    for word in split_sentence:
        if word not in list_a:
            list_a.append(word)
            list_b.append(1)
        else:
            index = list_a.index(word)
            list_b[index] += 1
    return list_a, list_b

def print_frequencies(words, frequencies):
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    split_sentence, o_sentence = get_sentence()
    words, frequencies = calculate_frequency(split_sentence)
    print_frequencies(words, frequencies)
    
    main()
