alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def caesar_cipher(text, shift=3):
    result = []
    for ch in text.upper():
        if ch in alphabet:
            idx = alphabet.index(ch)
            new_idx = (idx + shift) % len(alphabet)
            result.append(alphabet[new_idx])
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decipher(text, shift=3):
    return caesar_cipher(text, -shift)

word = "КОД"
encrypted = caesar_cipher(word)
print("Зашифрованное:", encrypted)
print("Расшифрованное:", caesar_decipher(encrypted))