# EncryptedText
Sends an [AES-256](https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf) encrypted text message to be decrypted using my [DecryptAES](https://github.com/shillerben/DecryptAES-iPhone) app.
This program uses the [Output FeedBack (OFB)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_Feedback_(OFB)) mode of operation for encrypting with AES.

## Requirements
* iPhone with iOS 9.0+
* [Python](https://www.python.org/) (tested with Python 3.6.1)

## Installation
To use EncryptedText, I recommend making a virtual environment using [virualenv](https://virtualenv.pypa.io/en/stable/).
### Clone Repository
`git clone https://github.com/shillerben/EncryptedText.git`
### Install virtualenv and Make Virtual Environment
```
pip install virtualenv
virtualenv EncryptedText
cd EncryptedText
```
### Activate Virtual Environement 
On a Unix-like computer:
```
source bin/activate
```
On a Windows computer:
```
Scripts\activate
```
### Install Needed Python Modules
`pip install -r requirements.txt`

## Usage
1. Modify the text and key variables in main.py
  * text is the message to be encrypted
  * key is the key used to encrypt and decrypt the message
2. Modify the GATEWAY, SMTP, EMAIL, and EMAIL_PASSWORD constants in main.py
  * GATEWAY is that the gateway corresponding to the recipient's phone number
    * See [here](https://www.tutsandtips.com/domains/full-list-of-mms-gateway-domains-for-mobile-carriers/) for a list of gateways for common carriers
  * SMTP is the outgoing server for your email provider
    * See [here](https://www.verizonwireless.com/support/knowledge-base-17067/) for a list of common email providers and their outgoing servers
3. Save main.py and run the program with:
```
python main.py
```
4. On the phone that received the text, copy the text and paste into the DecryptAES app
5. Enter your key in the app and press "Decrypt"

## Disclaimer
* This program uses MMS, so standard messaging rates may apply.
* I make no promises that the encryption used in this program is uncrackable. This program uses the [PyCryptodome](https://github.com/Legrandin/pycryptodome) Python library to perform the encryption.
