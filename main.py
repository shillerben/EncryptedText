#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 21, 2017
Sends an encrypted text message to be decrypted using my app
@author: Ben Shiller
"""

from encrypt_text import encrypt_msg
from send_text_by_email import send_text


text = ''
key  = ''

# constants for sending the text via email
PHONE = ''
SMTP  = ''
EMAIL = ''
EMAIL_PASSWORD = ''

# build and send text
ciphertext, iv = encrypt_msg(text, key)
msg = ciphertext.decode() + '\n\n\n' + iv.decode()
send_text(msg, PHONE, SMTP, EMAIL, EMAIL_PASSWORD)
