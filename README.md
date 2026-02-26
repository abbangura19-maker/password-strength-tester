🔐 Password Strength Tester

A beginner-friendly **Python** command-line tool that evaluates password strength and gives clear feedback to help users create better passwords.

Features
- Rates passwords as **Weak**, **Medium**, or **Strong**
- Checks:
  - Minimum length (≥8 characters)
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
  - Not in a list of common weak passwords
- Gives specific improvement suggestions (e.g. "Add at least one uppercase letter")
- Allows testing multiple passwords in one session (type `quit` to exit)
- Includes a simple visual strength bar

How to Run

1. Make sure **Python 3** is installed on your computer.
2. Clone or download this repository:

   ```bash
   git clone https://github.com/abbangura19-maker/password-strength-tester.git
   cd password-strength-tester

Or just download the password_tester.py file directly.

Open a terminal/command prompt in the folder containing the script.

Run:

python password_tester.py

Enter a password when prompted → get strength rating + suggestions

Example session:

Enter a password to test (or 'quit' to exit): 123456
Password strength: Weak
- Password should be at least 8 characters long.
- Add at least one uppercase letter.
- Add at least one lowercase letter.
- Add at least one digit.
- Add at least one special character.
- This is a very common password!

Enter a password to test (or 'quit' to exit): Tr#9pL@5qR7!
Password strength: Strong
[##########]  Great password!

What I Learned (5-day beginner project)

Python fundamentals: functions, loops, conditionals, user input
Regular expressions (regex) for checking character types
Basic cybersecurity concepts:
Importance of password length vs complexity
Risks of common/reused passwords
Defense against brute-force and dictionary attacks

Project workflow: setup → coding → testing edge cases → adding features → documentation
Git & GitHub basics: init, add, commit, push, README writing

Built following a structured Monday–Friday schedule (skipping Wednesday).

Future Improvement Ideas

Graphical interface with Tkinter
Load large common password dictionaries from files
Calculate actual password entropy
Color-coded output in terminal
Check against real breach databases (ethically)

Skills Demonstrated

Python programming
Regular expressions
Command-line application development
Basic cybersecurity awareness
Git version control & GitHub
Writing clear documentation

Feel free to use, fork, or improve it!
