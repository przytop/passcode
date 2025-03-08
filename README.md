# PassCode - Password Manager & Generator

**PassCode** is a password manager application that allows you to securely store and generate passwords for various websites. With its built-in password generator, the app helps you create passwords that meet high security standards and then stores them in an encrypted **MySQL** database.

## Features

- An intuitive user interface created using the **PySimpleGUI** module
- Easily generate strong passwords for use everywhere
- Quickly copy passwords or your email to the clipboard with one click
- Store entries encrypted in **MySQL** database using **Fernet** (symmetric encryption)
- Requires a Master Password, hashed with **argon2id**, to access the manager

## Requirements

- **Python3**
- **MySQL**

## Required Libraries

- `argon2-cffi`
- `cryptography`
- `mysql-connector-python`
- `pyperclip`
- `PySimpleGUI`

## Installation

### Step 1: Clone the project

```bash
git clone https://github.com/przytop/passcode
```

### Step 2: Install Libraries

Install required libraries:

```bash
pip install -r requirements.txt
```

Or install them individually:

```bash
pip install argon2-cffi
```

```bash
pip install cryptography
```

```bash
pip install mysql-connector-python
```

```bash
pip install pyperclip
```

```bash
pip install PySimpleGUI
```

### Step 3: Configure the database

You must edit the connection settings in `config.py`. Enter the correct `user` and `password` for your `MySQL` connection.

### Step 4: Installation

Run `start.py` and follow the instructions to set up and use the password manager.
