# Python Password Strength Checker

A lightweight Python-based application that evaluates password strength based on length, uppercase letters, lowercase letters, numbers, and special characters.

## Features

- Check password length.
- Detect uppercase and lowercase letters.
- Detect numbers.
- Detect special characters.
- Calculate password strength score.
- Classify passwords as Weak, Medium, or Strong.
- Provide suggestions to improve password strength.
- Interactive command-line interface.

## Technologies Used

- Python
- Colorama
- String Module

## Project Structure

```text
python-password-strength-checker/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/pradipta-web/python-password-strength-checker.git
```

2. Navigate to the project directory:

```bash
cd python-password-strength-checker
```

3. Create a virtual environment:

```bash
py -m venv venv
```

4. Install dependencies:

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Usage

Run the application:

```bash
.\venv\Scripts\python.exe app.py
```

Enter a sample password to check its strength.

## Password Strength Criteria

| Criteria | Description |
|---|---|
| Length | At least 8 characters |
| Uppercase | Contains uppercase letters |
| Lowercase | Contains lowercase letters |
| Numbers | Contains numeric characters |
| Special Characters | Contains special symbols |

## Author

**Kinervaaa**

GitHub: https://github.com/pradipta-web