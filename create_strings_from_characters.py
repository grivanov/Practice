def create_strings_from_characters(frequencies, string1, string2):
    # Write your code here.

    combined_string = string1 + string2

    string1_created = check_string(frequencies, string1)
    string2_created = check_string(frequencies, string2)
    combined_created = check_string(frequencies, combined_string)

    if combined_created:
        return (2)
    elif string1_created or string2_created:
        return (1)
    else:
        return (0)


def check_string(dictionary, string):

    string_created: True
    dictionary = dictionary.copy()

    if string == "":
        return True

    if dictionary == "":
        return False

    for letter in string:
        if letter in dictionary.keys() and dictionary[letter] > 0:
            dictionary[letter] = dictionary[letter] - 1
            string_created = True
        else:
            string_created = False
            break

    return string_created


frequencies = {
    "h": 2,
    "e": 1,
    "l": 3,
    "r": 4,
    "a": 3,
    "o": 2,
    "d": 1,
    "w": 1
}

string1 = ""
string2 = ""


create_strings_from_characters(frequencies, string1, string2)
