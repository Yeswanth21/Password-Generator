# Password-Generator (python)

A Python-based Secure Password Generator that creates strong, customizable passwords with enforced security rules. Built as part of a Cybersecurity project to follow best practices in password policy and strength.

## 🚀 Features

- ✅ Generates strong random passwords
- ✅ Enforces minimum security requirements:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
- ✅ User-defined password length (must be > 8)
- ✅ Shuffles characters to enhance randomness
- ✅ Simple and clean command-line interface (CLI)

---

## 🛠️ How it Works

The script uses Python’s built-in `random` and `string` libraries to generate a secure password. It ensures the generated password contains all required character types and shuffles the final password to avoid predictable patterns.

---

## 💻 Demo

```bash
$ python password_generator.py
🔐 Secure Password Generator 🔐
Enter password length (must be > 8): 12
For security reasons password will include:
✅ Uppercase letters
✅ Digits
✅ Symbols
(This is required for strong password enforcement.)

✅ Generated password: G#3adL!9bfP@
```

---

## 🧱 Tech Stack

- Python 3.x
- No external libraries required

---

## 🧠 Why This Project?

This project follows the principle of "Security by Design" — ensuring passwords meet a minimum strength policy by default. It’s perfect for showcasing Python, cybersecurity logic, and CLI interaction in GitHub and LinkedIn portfolios.


