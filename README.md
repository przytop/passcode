# PassCode

## Overview
A PassCode is a simple password manager with GUI to securely manage and store passwords to your websites. Uses a built-in generator to generate strong passwords and secure them encrypted in MySQL database

## Features
- Intuitive, simple UI created with PySimpleGUI module
- Easily generate a strong password for your use
- Fast copy password or your emial to your clipboard with one click
- Store your entries encrypted in MySQL database whit Fernet - symmetric encryption
- Require a Master Password, hashed with argon2id, to access in to the manager, created when you install manager

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
git clone
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

### Step 4: Instalation

Run start.py and follow the instructions