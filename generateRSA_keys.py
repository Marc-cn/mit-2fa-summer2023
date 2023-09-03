import rsa

def generateKeys():
    publicKey, privateKey = rsa.newkeys(2048)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def load_keys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return  publicKey, privateKey
    

generateKeys()
publicKey, privateKey =load_keys()

message = "hello geeks"
encMessage = rsa.encrypt(message.encode(),publicKey)
print("original string: ", message)
decMessage = rsa.decrypt(encMessage, privateKey).decode() 
print("decrypted string: ", decMessage)
