def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):

            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
                if (count >= 9):
                    break
            else:
                break

        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string


def decode(our_message):
    decoded_message = ""
    i = 0
    j = 0

    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        decoded_message = decoded_message+run_word*run_count
        i = i + 2
    return decoded_message


with open('text.txt', 'r') as data:
    message = data.read()

print(message)
encoded_string = encode_message(message)
print(encoded_string)
decoded_string = decode(encoded_string)
print(decoded_string)

if message == decoded_string:
    print("strings match")

with open('text_rle.txt', 'a') as data:
    data.write(encode_message(message))
