from include.ciphers import (
    rba_vigenere,
    rba_xor,
    rba_quagmire,
)

def decrypt(file, format, key):
    file_content: str = ""
    with open(file, "r") as fd:
        file_content = fd.read()
    
    match (format):
        case 'vigenere':
            file_content = rba_vigenere.vig_decrypt(file_content, key)
        case 'xor':
            file_content = rba_xor.xor_decrypt(file_content, key)
        case 'quagmire':
            file_content = rba_quagmire.q3_decrypt(file_content, key)
        case _:
            return -1
    
    with open(file, "w") as fd:
        fd.write(file_content)
    
    return 0