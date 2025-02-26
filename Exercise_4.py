import random
import string

# Encodeing Part

word = input("Give the input for encription: ")
encripted_word = ""
if(len(word) < 4):
    for i in range(len(word)):
        encripted_word += word[len(word)-1-i]
    print(encripted_word)

else:
    for i in range(len(word)):
        if(1 + i == len(word)):
            encripted_word += word[0]
            break
        encripted_word += word[1 + i]
    encripted_word = "".join(random.choices(string.ascii_letters, k=3)) + encripted_word + "".join(random.choices(string.ascii_letters, k=3))
    print(encripted_word)

# Decoding Part

Decode_word = ""
if(len(encripted_word) < 4):
    for i in range(len(word)):
        Decode_word += encripted_word[len(word)-1-i]
    print(Decode_word)

else:
    encripted_word = encripted_word[3:len(word)+3:1]
    Decode_word = encripted_word[len(encripted_word)-1] + encripted_word[0:len(word)-1:1]
    print(Decode_word)