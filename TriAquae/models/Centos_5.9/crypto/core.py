import rsa
import base64
from helpers import split_len

def encrypt(text, pub_key):
    block_size = rsa.common.byte_size(pub_key.n) - 11
    encrypted = ""
    for part in split_len(text, block_size):
        encrypted += rsa.encrypt(part, pub_key)
    return encrypted

def encrypt_str(text, pub_key, encode=base64.standard_b64encode):
    return encode(encrypt(text, pub_key))

def decrypt(encrypted, pri_key):
    block_size = rsa.common.byte_size(pri_key.n)
    text = ""
    for part in split_len(encrypted, block_size):
        text += rsa.decrypt(part, pri_key)
    return text

def decrypt_str(text, pub_key, decode=base64.standard_b64decode):
    return decrypt(decode(text), pub_key)

def export_key(key):
    return key.save_pkcs1()

def export_key_file(key, path):
    file(path, "w").write(export_key(key))

def load_key(key_str):
    if "-----BEGIN RSA PRIVATE KEY-----" in key_str:
        return rsa.PrivateKey.load_pkcs1(key_str)
    else:
        return rsa.PublicKey.load_pkcs1(key_str)

def load_key_file(path):
    return load_key(file(path).read())
