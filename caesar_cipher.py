def caesar_cipher(string, offset):
    # Write your code here.
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encoded_str = list()
    out_str = str()

    for letter in string:
        position = alphabet.index(letter)
        encoded_str.append(alphabet[position - offset])

    return out_str.join(encoded_str)


caesar_cipher("hello", 3)
