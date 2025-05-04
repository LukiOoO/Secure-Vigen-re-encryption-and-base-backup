import string

a = string.ascii_uppercase


def generate_keystream(text: str, key: str) -> str:
    key = ''.join(ch for ch in key if ch.isalpha()).upper()
    keystream = []
    key_index = 0
    for char in text:
        if char.upper() in a:
            keystream.append(key[key_index % len(key)])
            key_index += 1
        else:
            keystream.append(char)
    return ''.join(keystream)


def vigenere_cipher(text: str, key: str, mode: str = 'encrypt') -> str:
    result = []
    keystream = generate_keystream(text, key)
    for t_char, k_char in zip(text, keystream):
        up = t_char.upper()
        if up in a:
            idx_t = a.index(up)
            idx_k = a.index(k_char)
            if mode == 'encrypt':
                idx_new = (idx_t + idx_k) % 26
            else:
                idx_new = (idx_t - idx_k) % 26
            new_char = a[idx_new]
            result.append(new_char if t_char.isupper() else new_char.lower())
        else:
            result.append(t_char)
    return ''.join(result)
