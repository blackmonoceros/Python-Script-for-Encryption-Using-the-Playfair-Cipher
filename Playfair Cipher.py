def prepare_key_table(key):
    # Remove duplicates from the key and replace 'J' with 'I'
    key = key.upper().replace("J", "I")
    key = "".join(dict.fromkeys(key))  # Removes duplicates while preserving order

    # Create the alphabet without 'J'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in key:
            key += letter

    # Create a 5x5 table
    table = [list(key[i:i+5]) for i in range(0, 25, 5)]
    return table

def find_position(table, char):
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return row, col
    return None

def encrypt_pair(table, char1, char2):
    row1, col1 = find_position(table, char1)
    row2, col2 = find_position(table, char2)

    # Encryption rules
    if row1 == row2:  # Same row
        return table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
    else:  # Rectangle
        return table[row1][col2] + table[row2][col1]

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared_text = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text) and text[i + 1] != char1:
            char2 = text[i + 1]
            i += 2
        else:
            char2 = "X"  # Add 'X' if the pair is incomplete
            i += 1
        prepared_text += char1 + char2
    return prepared_text

def playfair_encrypt(text, key):
    table = prepare_key_table(key)
    prepared_text = prepare_text(text)
    encrypted_text = ""

    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i + 1]
        encrypted_text += encrypt_pair(table, char1, char2)

    return encrypted_text

# Example usage
key = "CIPHER"
plaintext = "EXAMPLE TEXT"
ciphertext = playfair_encrypt(plaintext, key)
print("Encrypted text:", ciphertext)