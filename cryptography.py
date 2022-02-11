def encrypt(text, key):
    result = ""
    for ch in text:
        ch_encrypted = ch
        ch_value = ord(ch)
        if ch_value >= 97 and ch_value <= 122:
            ch_value += (key % 26)
            if ch_value > 122:
                ch_value = ch_value - 123 + 97
            ch_encrypted = chr(ch_value)
        elif ch_value >= 65 and ch_value <= 90:
            ch_value += (key % 26)
            if ch_value > 90:
                ch_value = ch_value - 91 + 65
            ch_encrypted = chr(ch_value)
        result += ch_encrypted
    return result



def decrypt(text, key):
    result = ""
    for ch in text:
        ch_decrypted = ch
        ch_value = ord(ch)
        if ch_value >= 97 and ch_value <= 122:
            ch_value += -(key % 26)
            if ch_value < 97:
                ch_value = 123 - (97 - ch_value)
            ch_decrypted = chr(ch_value)
        elif ch_value >= 65 and ch_value <= 90:
            ch_value += -(key % 26)
            if ch_value < 65:
                ch_value = 91 - (65 - ch_value)
            ch_decrypted = chr(ch_value)
        result += ch_decrypted
    return result


def crack():
    pass

print(ord("Z"))

# a = 97; z = 122; A = 65; Z = 90