
key = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
       'f', 'g', 'h', 'j', 'k', 'l', 'z', '', 'x', 'c', 'v', 'b', 'n', 'm']
# ⬆️ We selected a random key with all the alphabets and space too.
originaltext = input("Enter Plaintext to be encrypted: ")
# ⬆️ we ask input from user
c = []
d = []
#  ⬆️ [] are  dynamic array(lists) which stores data temporaily
# that can be changed in future.
for i in range(0, len(originaltext)):
    c.append(key[ord(originaltext[i])-97])
# ⬆️ range(start_value, stop_value)--> used generates the sequence based
#     on the start and stop value.
# ⬆️ len() is a function used to get length of string, array, dictionary and so on.
# ⬆️ append() method adds a single item to the existing list.
# ⬆️ ord() function returns the number
#     representing the unicode(ASCII) code of a specified character.
print("Ciphertext (Encryption): ")
print(c)
for i in range(0, len(c)):
    for j in range(0, len(key)):
        if(c[i] == key[j]):
            d.append(chr(j+97))
print("Plaintext (Decryption): ")
print(d)
