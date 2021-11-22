import hashlib

def SHA256(string :str):
    # returns a string containing the hash of the given string in hexadecimal
    return hashlib.sha256(string.encode('utf-8')).hexdigest()