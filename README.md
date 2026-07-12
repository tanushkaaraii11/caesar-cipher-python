# Caesar Cipher Encryption & Decryption using Python

## Project Overview

This project is a Python implementation of the **Caesar Cipher**, one of the oldest and simplest encryption techniques in cryptography.

The program allows users to **encrypt** or **decrypt** a message by shifting each alphabetic character by a user-defined number. It correctly handles both uppercase and lowercase letters while preserving spaces, numbers, and special characters.

This project was developed as part of a Cyber Security Internship to understand the basics of classical cryptography and Python programming.

## Features

- Encrypt messages using the Caesar Cipher algorithm
- Decrypt encrypted messages
- Supports both uppercase (A-Z) and lowercase (a-z) letters
- Preserves spaces without modification
- Preserves numbers and special characters
- User-defined shift value
- Simple command-line interface
- Beginner-friendly implementation with readable code

## Technologies Used

- Python 3
- Visual Studio Code
- Git & GitHub

## Concepts Used

This project demonstrates the following Python concepts:
- Variables
- User Input
- Data Types
- For Loops
- Conditional Statements (`if`, `elif`, `else`)
- String Manipulation
- ASCII Conversion
- `ord()` Function
- `chr()` Function
- Modulo Operator (`%`)
- Basic Cryptography Concepts

## How the Caesar Cipher Works
The Caesar Cipher encrypts text by shifting every alphabetic character by a fixed number of positions in the alphabet.

### Example
Original Message:

```
HELLO
```

Shift Value:

```
3
```

Encrypted Message:

```
KHOOR
```

For decryption, the program simply shifts the letters backward using the same shift value.

## How the Program Works
1. The user enters a message.
2. The user enters a shift value.
3. The user chooses:
   - **E** for Encryption
   - **D** for Decryption
4. The program processes each character individually.
5. Alphabetic characters are shifted according to the Caesar Cipher algorithm.
6. Spaces, numbers, and special characters remain unchanged.
7. The final encrypted or decrypted message is displayed.

## Sample Execution
### Encryption
```
Enter the message: Hello World!
Enter the shift value: 3
Enter E for Encryption or D for Decryption: E

Output:
Khoor Zruog!
```

### Decryption
```
Enter the message: Khoor Zruog!
Enter the shift value: 3
Enter E for Encryption or D for Decryption: D

Output:
Hello World!
```

## Author
**Tanushka Rai**

