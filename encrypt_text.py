#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 21, 2017

@author: Ben Shiller
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def encrypt_msg(text, password):
    text_bytes = text.encode()
    password_bytes = password.encode()
    # pad key with blocksize of 32
    key = pad(password_bytes, 32)
    aes = AES.new(key, AES.MODE_OFB)
    iv = base64.b64encode(aes.iv)
    ciphertext = base64.b64encode(aes.encrypt(text_bytes))
    return ciphertext, iv

# used for testing
def decrypt_msg(ciphertext, iv, password):
    ciphertext_bytes = base64.b64decode(ciphertext)
    iv_bytes = base64.b64decode(iv)
    password_bytes = password.encode()
    key = pad(password_bytes, 32)
    aes = AES.new(key, AES.MODE_OFB, iv=iv_bytes)
    plaintext = aes.decrypt(ciphertext_bytes)
    return plaintext.decode()
    