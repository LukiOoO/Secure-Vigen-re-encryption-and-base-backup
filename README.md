# Secure-Vigen-re-encryption-and-base-backup
A simple Flask web application demonstrating:

- Vigenère cipher encryption and decryption (letters A–Z)  
- User registration & login with password hashing  
- SQLite database backup and restore  
- Automatic logout if a user’s record is removed from the database  
- Real-time password & key strength meters  

---

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation / Running the App](#installation)  

---

## Features

- **Vigenère Cipher** – encrypt or decrypt text via a simple web form  
- **Authentication** – register and log in with bcrypt-hashed passwords  
- **JWT Ready** – (placeholder) can be extended with `flask-jwt-extended`  
- **Database Backup/Restore** – download or upload the SQLite file  
- **Auto-Logout** – if your user account is removed from the DB, you’re immediately logged out  
- **Strength Meters** – visual indicators for password and cipher-key strength  

---

## Prerequisites

- Python 3.8 or newer  
- Git (optional, for cloning the repo)  

---

## Installation / Running the App

1. **Clone the repository**  
   git clone https://github.com/yourusername/flask-crypto-db.git
   cd flask-crypto-db
   pip install virtualenv
   virtualenv env
   .\env\Scripts\activate
   pip install -r requirements.txt
   python app.py

   By default the app runs at http://127.0.0.1:5000
