from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import MD5
import base64
import sys

def aesencrypt(key,plaintext):
	hashedkey = MD5.new()
	hashedkey.update(key.encode('utf-8'))
	newkey = hashedkey.hexdigest()
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(newkey,AES.MODE_CFB,iv)
	misg = iv + cipher.encrypt(plaintext)
	b64encodedmsg = base64.b64encode(misg)
	#return misg
	return b64encodedmsg

def aesdecrypt(key,enc):
	decoded = base64.b64decode(enc)
	iv = decoded[:16]
	hashedkey = MD5.new()
	hashedkey.update(key.encode('utf-8'))
	newkey = hashedkey.hexdigest()
	cipher = AES.new(newkey,AES.MODE_CFB,iv)
	decrypted = cipher.decrypt(decoded)
	return decrypted[16:]

def aesencrypt_unencoded(key,plaintext):
	hashedkey = MD5.new()
	hashedkey.update(key.encode('utf-8'))
	newkey = hashedkey.hexdigest()
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(newkey,AES.MODE_CFB,iv)
	misg = iv + cipher.encrypt(plaintext)
	return misg

def aesdecrypt_unencoded(key, enc):
	iv = enc[:16]
	hashedkey = MD5.new()
	hashedkey.update(key.encode('utf-8'))
	newkey = hashedkey.hexdigest()
	cipher = AES.new(newkey, AES.MODE_CFB, iv)
	decrypted = cipher.decrypt(enc)
	return decrypted[16:]
