def caesar_crack(cipher_text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = cipher_text.upper()
    
    for shift in range(1, 26):
        decoded_text = ""
        for char in cipher_text:
            if char in alphabet:
                shifted_index = (alphabet.index(char) - shift) % 26
                decoded_text += alphabet[shifted_index]
            else:
                decoded_text += char
        print(f"Shift {shift}: {decoded_text}")

cipher_text = 'Gdoqs: hvs twboz tfcbhwsf. Hvsgs ofs hvs jcmousg ct hvs ghofgvwd Sbhsfdfwgs'
caesar_crack(cipher_text)
