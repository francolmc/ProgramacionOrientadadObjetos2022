import bcrypt

pwd = b'holacomoestas'

# salt = bcrypt.gensalt()
salt = b'$2b$12$px5IIBlPTHKNGs7mz.mI0O'

encryptpwd = bcrypt.hashpw(pwd, salt)

print(encryptpwd)