#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2012
Send text message via email
@author: user352472
'''
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

def send_text(text, phone, smtp, email, password): 
    numFail = 0
    msg = MIMEText(text, 'plain') 
    me = phone
    msg['To'] = me
    try:
        conn = SMTP(smtp)
        conn.set_debuglevel(True)
        conn.login(email, password)
        try:
            conn.sendmail(me, me, msg.as_string())
        finally:
            conn.close()
    except KeyboardInterrupt:
        numFail += 1
        if numFail < 3:
            print('\nTrying again...')
            send_text(text, phone, smtp, email, password)
        else:
            print('\nSending email failed 3 times.')
    except Exception:
        numFail += 1
        if numFail < 3:
            send_text(text, phone, smtp, email, password)
        else:
            print('Sending email failed 3 times.')
