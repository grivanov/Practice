def get_n_longest_unique_words(words, n):
    # Write your code here.
    unique_words = []

    for element in words:
        if words.count(element) > 1:
            continue
        else:
            unique_words.append(element)

    def len_sort(a):
        return len(a)

    unique_words.sort(key=len_sort, reverse=True)

    result_list = unique_words[:n]

    return result_list


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
