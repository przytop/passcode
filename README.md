# PassCode

## Overview
A PassCode is a simple password manager with GUI to securely manage and store passwords to your websites. 
Uses a built-in generator to generate strong passwords and secure them encrypted in MySQL database

## Features
- Simple, intuitive user interface created with PySimpleGUI module
- Easily generate a strong password for your use everywhere
- Fast copy password or email to your clipboard with one click
- Store your entries encrypted in MySQL database whit Fernet - symmetric encryption
- Requires a Master Password, hashed with argon2id, to access into the manager

## Requirements
- Python3
- MySQL

## Libraries
- argon2-cffi
- cryptography
- mysql-connector-python
- pyperclip
- PySimpleGUI

## Setup

### Step 1: Clone project

```
git clone https://github.com/przytop/passcode
```

### Step 2: Libraries

Install required libraries
```
pip install -r requirements.txt
```
OR
```
pip install argon2-cffi
```
```
pip install cryptography
```
```
pip install mysql-connector-python
```
```
pip install pyperclip
```
```
pip install PySimpleGUI
```

### Step 3: Config database

You must edit the connection. Enter the correct 'user' and 'password' in config.py to connect to your MySQL

### Step 4: Installation

Run start.py and follow the instructions