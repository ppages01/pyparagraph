import re
import sys

with open('raw_data/paragraph_2.txt', 'r') as file:
    paragraph = file.read()
    # lower case all letters
    paragraph = paragraph.lower()

    # sentences grouped and counted
    sentences = re.split('(?<=[.!?]) +', paragraph)
    sentence_count = len(sentences)

    # words without punctuation, grouped and counted
    clean = re.sub(r'[^\w\s]', '', paragraph)
    words = clean.split()
    word_count = len(words)
    # attempt letter and average sentence length
    letter_count = 0
    for letter in paragraph:
        letter_count += 1

    alc = letter_count/word_count
    asl = word_count/sentence_count

# Display Results
print("Paragraph Analysis")
print("-" * 25)
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Sentence Count: {sentence_count} ')
print(f'Average Letter Count: {alc} ')
print(f'Average Sentence Length: {asl}')
