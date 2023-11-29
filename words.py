def print_upper_words(words, must_start_with=None):
    """Print words from a list in uppercase, optionally filtered by starting letters."""
    for word in words:
        if must_start_with is None or any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())


