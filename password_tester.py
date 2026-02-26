import re

# List of common weak passwords (case-insensitive check)
# Sourced from various lists of top compromised passwords
common_passwords = [
    "123456", "123456789", "12345678", "password", "12345",
    "111111", "1234567", "sunshine", "qwerty", "admin",
    "welcome", "letmein", "abc123", "football", "monkey",
    "jesus", "princess", "superman", "batman", "trustno1", "iloveyou", 
    "mynameis",
]

def check_password_strength(password):
    strength_points = 0
    feedback = []
   
    # Check length
    if len(password) >= 12:
        strength_points += 1
    else:
        feedback.append("Password should be at least 12 characters long.")
   
    # Check for uppercase
    if re.search(r'[A-Z]', password):
        strength_points += 1
    else:
        feedback.append("Add at least one uppercase letter.")
   
    # Check for lowercase
    if re.search(r'[a-z]', password):
        strength_points += 1
    else:
        feedback.append("Add at least one lowercase letter.")
   
    # Check for digit
    if re.search(r'\d', password):
        strength_points += 1
    else:
        feedback.append("Add at least one digit.")
   
    # Check for special character
    if re.search(r'[!@#$%^&*()_+?~]', password):
        strength_points += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$).")
   
    # Original exact common check (keep or replace)
    if password.lower() not in [p.lower() for p in common_passwords]:
        strength_points += 1
    else:
        feedback.append("Avoid common passwords—choose something unique.")
   
    # New substring pattern check
    common_patterns = ["123", "abc", "qwerty", "password", "letmein"]  # Expand as needed
    for pattern in common_patterns:
        if pattern in password.lower():
            feedback.append("Your password contains a simple sequence like '123' or 'abc'—try randomizing numbers and letters.")
            break  # Avoid multiple messages
    else:
        strength_points += 1  # Add point if no patterns
   
    # Determine strength level (adjust thresholds if max points change)
    if strength_points <= 3:
        strength = "Weak"
    elif strength_points <= 5:
        strength = "Medium"
    else:
        strength = "Strong"
       
    return strength, feedback

if __name__ == "__main__":
    while True:
        password = input("Enter a password to test (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        strength, feedback = check_password_strength(password)
        print(f"Password strength: {strength}")
        if feedback:
            print("Suggestions:")
            for comment in feedback:
                print(f"- {comment}")
        print()