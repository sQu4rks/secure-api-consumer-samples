from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

token = "secret"

encrypted = f.encrypt(token.encode('utf-8'))
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)
