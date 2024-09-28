import string

alphabet = list(string.ascii_lowercase)

def caesar_cipher():
    decode_or_encode = input('Do you want encode or decode?')
    user_decode_input = input(f'What do you want to {decode_or_encode}? \n')
    user_count_input = int(input(f'With how many sets do you want to {decode_or_encode}? \n')) % len(alphabet)

    user_input_split = list(user_decode_input)

    new_list = []
    index_list = []

    result = ''

    for item in range(0, len(alphabet)):
        if decode_or_encode == 'decode':
            new_list += alphabet[item - user_count_input]
        else:
            new_list += alphabet[item - (len(alphabet) - user_count_input)]

    for item in user_input_split:
        index_list.append(alphabet.index(item))

    for item in index_list:
        result += new_list[item]

    print(result)

    stop_or_continue = input('Do you want to try again? Yes or No \n').lower()
    if stop_or_continue == 'yes':
        caesar_cipher()

caesar_cipher()