# Import biblioteke i elipticne krivulje
from ecdsa import SigningKey, NIST384p

# Generiranje privatnog kljuca s P-384 krivuljom
private_key = SigningKey.generate(curve=NIST384p)
print("Privatni kljuc:", private_key)

# Generiranje javnog kljuca iz privatnog
public_key = private_key.get_verifying_key()
print("Javni kljuc:", public_key)

# Spremanje privatnog i javnog kljuca u .pem formatu
with open("private_key.pem", "wb") as priv_file:
    priv_file.write(private_key.to_pem())
    
with open("public_key.pem", "wb") as pub_file:
    pub_file.write(public_key.to_pem())
