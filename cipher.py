alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Write a message")
message = input()
shifted_alphbet = {}
for i in range(0, 26):
        letter = alphabet[i]
        shifted_alphbet[letter] = alphabet[(i + 5) % 26]
        
    
cipher_message = ''
for letter in message:
        if letter in shifted_alphbet:
            letter = shifted_alphbet[letter]
            cipher_message = cipher_message + letter
        else:
            cipher_message = cipher_message + " "

print(cipher_message)
