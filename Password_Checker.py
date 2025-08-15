import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Determine strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback messages
    feedback = []
    if not length_criteria:
        feedback.append("• Use at least 8 characters.")
    if not upper_criteria:
        feedback.append("• Add uppercase letters (A-Z).")
    if not lower_criteria:
        feedback.append("• Add lowercase letters (a-z).")
    if not digit_criteria:
        feedback.append("• Include numbers (0-9).")
    if not special_criteria:
        feedback.append("• Include special characters (!@#$...).")

    return strength, feedback

def main():
    print("🔐 Password Complexity Checker 🔐")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Strength:", strength)
    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print(tip)
    else:
        print("Great job! Your password is strong.")

if __name__ == "__main__":
    main()
