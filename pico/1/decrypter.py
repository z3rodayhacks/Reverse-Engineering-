# Given encrypted text in 'enc'
enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
flag = ""

# Process each character in 'enc' by reversing the encoding logic
for char in enc:
    # Convert each character in 'enc' to its code point
    code_point = ord(char)
    
    # Extract the two original characters:
    # First character is the higher byte, so shift right by 8
    first_char = chr(code_point >> 8)
    # Second character is the lower byte, use bitwise AND with 0xFF to get it
    second_char = chr(code_point & 0xFF)
    
    # Append these characters to the flag
    flag += first_char + second_char

print("Decrypted flag:", flag)
