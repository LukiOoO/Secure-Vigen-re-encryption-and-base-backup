# Flask Crypto–DB

A simple Flask web application demonstrating:

* Vigenère cipher encryption and decryption (letters A–Z)
* User registration & login with password hashing
* SQLite database backup and restore
* Automatic logout if a user’s record is removed from the database
* Real-time password & key strength meters

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation / Running the App](#installation)

---

## Features

* **Vigenère Cipher** – encrypt or decrypt text via a simple web form.
* **Authentication** – register and log in with bcrypt-hashed passwords.
* **Database Backup/Restore** – download or upload the SQLite file.
* **Auto-Logout** – if your user account is removed from the DB, you’re immediately logged out.
* **Strength Meters** – visual indicators for password and cipher-key strength.

---

## Prerequisites

* Python 3.8 or newer.
* Git (optional, for cloning the repo).

---

<a id="installation"></a>

## Installation / Running the App

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/flask-crypto-db.git  
   cd flask-crypto-db
   ```

2. **Create and activate a virtual environment**

   * On **Linux/macOS**:

     ```bash
     python3 -m venv env  
     source env/bin/activate
     ```
   * On **Windows (PowerShell)**:

     ```powershell
     python -m venv env  
     .\env\Scripts\Activate.ps1
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

   By default the app will be available at:

   ```
   http://127.0.0.1:5000
   ```
