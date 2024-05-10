# Define a function `letter_frequency` that takes in an argument called `word` of type `str` and returns a mapping of each letter in word to its number of occurrences i.e. `dict[str, int]`.


def letter_frequency(word: str) -> dict:
    word_count = {}
    word_set = set(word.lower())

    for i in word_set:
        print(i, word)
        word_count[i] = word.lower().count(i)
    return word_count


print(letter_frequency("Andrea"))