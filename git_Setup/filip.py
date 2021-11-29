def SHA256(string :str):
    # returns a string containing the hash (SHA 256) of the given string in hexadecimal
    from hashlib import sha256
    return sha256(string.encode('utf-8')).hexdigest()