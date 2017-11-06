key = {'A': '@', 'B': '*', 'C': '^', 'D': '!', 'E': '&', 'F': '#', 'G': '%',
       'H': '(', 'I': '|', 'J': '$', 'K': ')', 'L': ';', 'M': '>', 'N': '<',
       'O': '?', 'R': '=', 'S': '+', 'T': '-', 'U': '[', 'V': ']', 'W': ',',
       'X': '"', 'Y': '/', ' ': '~'}

encrypted_msg = ''
def encrypt():
    msg = input('Enter a sentence').upper()
    for char, symbol in key.items():
        msg = msg.replace(char, symbol)
        encrypted_msg = msg
    print('Encypted message:', encrypted_msg)
    return

def decrypt():
    for char, symbol in key.items():
        decrypted_msg = encrypted_msg.replace(symbol, char)
    print('Decrypted message:', decrypted_msg)
    return

encrypt()
decrypt()