message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        first = 'A' if ch.isupper() else 'a'
        pos = ord(ch) - ord(first)  
        pos = (pos + offset) % 26  
        new_char = chr(pos + ord(first))  
        
    else:
        new_char = ch
        
    encoded_message = encoded_message + new_char

    print(encoded_message)
