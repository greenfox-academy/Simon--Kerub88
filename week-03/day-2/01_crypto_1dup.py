# Create a method that decrypts the texts/duplicated_chars.txt
fr = open("duplicated-chars.txt", "r")
text = fr.read()

def decrypt(file_name):
    text_decrypt = ""
    for t in range(0, len(file_name), 2):
        # if (t % 2) == 0:
            # every_secund = file_name[t]
            text_decrypt += file_name[t]

    return text_decrypt


print(decrypt(text))
