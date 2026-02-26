Password Strength Tester Project README

Project Overview

A Python tool to rate password strength based on length, variety, and common lists. It evaluates passwords on criteria like minimum length (12 characters), mix of uppercase/lowercase letters, digits, special characters, and avoidance of common weak passwords.
 The tool provides a rating (Weak, Medium, or Strong) and specific suggestions for improvement.
How to Use
Ensure Python is installed and added to your PATH.
Open Command Prompt and navigate to the folder containing the script (e.g., cd %USERPROFILE%\Desktop).
Run the script: python password_tester.py.
Enter a password when prompted—you'll get the strength rating and suggestions.
Test multiple passwords in one session; type 'quit' to exit.
Optional: The tool includes a visual strength bar (e.g., [##########] for Strong).

What I Did and Learned

This project was a week-long beginner cybersecurity exercise in Python, starting from setup and research to a polished tool. Here's a summary of what I did and key learnings:
Monday (Setup and Research): Installed Python, set up a text editor, created the script file, and tested a "Hello, World!" run. Researched password strength criteria from sources like NIST and NordPass (e.g., length over complexity, avoiding common passwords like "123456"). Learned: Basic environment troubleshooting (e.g., navigating cmd, fixing PATH issues) is essential; weak passwords are vulnerable to brute-force and dictionary attacks.
Tuesday (Core Coding and Tweaks): Copied the base script, understood regex for character checks, fixed indentation errors, and experimented with tweaks like changing length to 12 chars, expanding the common passwords list (added "iloveyou"), and adjusting scoring thresholds for stricter ratings. Learned: Python's indentation matters a lot; small changes like variety requirements boost security against cracking.
Thursday (Testing and Feedback): Ran edge cases (empty strings, single chars, all uppercase, no digits/specials, very long passwords) and verified each criterion with targeted tests (e.g., failing uppercase drops a point). Compared with NordPass—my tool is stricter on length but misses some patterns. Added feedback suggestions (e.g., "Add at least one digit"). Learned: Thorough testing reveals limitations (e.g., exact-match common checks miss substrings like "123" in "My123Pass!"); feedback makes the tool educational, aligning with real-world checkers.
Friday (Polish and Reflection): Added a loop for multiple tests without restarting and a visual strength bar. Created this README and reflected on the process. Learned: Strong passwords need 12+ chars and mixed types to resist attacks; tools like NordPass detect patterns better, inspiring future improvements like substring checks or entropy calculation. Overall, debugging (e.g., PATH, indentation) built persistence, and the project showed how simple code can demonstrate cybersecurity principles ethically.

Future Ideas: Add a GUI with Tkinter, load larger common password dictionaries from files, calculate entropy using math libraries, or simulate brute-force times.