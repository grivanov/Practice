def get_n_longest_unique_words(words, n):
    # Write your code here.
    unique_words = []

    for element in words:
        if words.count(element) > 1:
            continue
        else:
            unique_words.append(element)

    result_list = sorted(unique_words, key=len, reverse=True)

    return result_list[:3]


words = [
    'Longer',
    'Whatever',
    'Longer',
    'Ball',
    'Rock',
    'Rocky',
    'Rocky'
]
get_n_longest_unique_words(words, 4)
