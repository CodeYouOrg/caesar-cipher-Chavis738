alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Write a message")
message = input()
shifted_alphbet = {}
for i in range(0, 26):
        letter = alphabet[i]
        shifted_alphbet[letter] = alphabet[(i + 5) % 26]
        
    
cipher_message = ''
for chr in message:
        if chr in shifted_alphbet:
            chr = shifted_alphbet[chr]
            cipher_message = cipher_message + chr
        elif chr not in shifted_alphbet and chr != " ":
            cipher_message = cipher_message + chr              
        else:
            cipher_message = cipher_message + " "

print(cipher_message)
