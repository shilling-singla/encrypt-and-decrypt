alphabets = 'abcdefghijklmnopqrstuvwxyz'

key = int(input('Enter the key: '))

def encryption(key):
 newMessage = ''
 message = input("Enter the message to encrypt: ").lower()
 for character in message:
    if character in alphabets:
        position =  alphabets.find(character)
        newPosition = (position + key)%26
        newCharacter = alphabets[newPosition]
        newMessage += newCharacter

    else:
        newMessage += character
 print('Your encrypted message is: ', newMessage)

def decryption(key):
 newMessage = ''
 message = input("Enter the message to decrypt: ").lower()
 character: str
 for character in message:
     if character in alphabets:
        position = alphabets.find(character)
        newPosition = (position - key)%26
        newCharacter = alphabets[newPosition]
        newMessage += newCharacter
     else:
        newMessage += character
 print('Your decrypted message is: ',newMessage)


print("Enter 1 to encrypt your message")
print("Enter 2 to decrypt your message")
choice = int(input('Enter your choice:'))

if choice == 1:
    encryption(key)
elif choice == 2:
    decryption(key)

