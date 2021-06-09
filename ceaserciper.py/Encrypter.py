

plaintxt = input('Enter your string: '.lower())
# ⬆️ Ask the String to be encrypted or decrypted from user and convert into lowercase.

alphabet = "abcdefghijklmnopqrstuvwxyz"
# ⬆️ here we created variable alphabet to list out alphabets.

Key = int(input("Enter the key to be shifted 1 to 26: "))

cipher = ''
# ⬆️ we create cipher a variable where our encrypted message is stored.

for c in plaintxt:
    # ⬆️ this will assign the value of plaintext to c
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c)+Key) % len(alphabet)]
        # ⬆️ formula ---> e(x)= (x+k) mod 26
        # ⬆️ index (): basically returns the place where element appears
        # eg: no = [4, 55, 64, 32, 16, 32], print(no.index(64)) will display = 2
        # ⬆️ len() is a function used to get length of string, array, dictionary and so on.
        # eg: a='bishal ad' then print(len(a))=9
print("Your Encrupted message: " + cipher)
# + string, basically displays them together with + your python won't display result.
