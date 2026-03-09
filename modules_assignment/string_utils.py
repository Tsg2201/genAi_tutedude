# string_utils.py
# This module contains simple string utility functions.


# Function to capitalize each word in a sentence
def capitalize_words(text):
    return text.title()


# Function to reverse a string
def reverse_string(text):
    return text[::-1]


# Function to count the number of words in a sentence
def word_count(text):
    words = text.split()
    return len(words)