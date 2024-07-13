import re

def project(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))
    
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    feedback = []
    
    if length_criteria:
        feedback.append("Length is sufficient")
    else:
        feedback.append("Password should be at least 8 characters long")
        
    if uppercase_criteria:
        feedback.append("Contains uppercase letter(s)")
    else:
        feedback.append("Password should contain at least one uppercase letter")
        
    if lowercase_criteria:
        feedback.append("Contains lowercase letter(s)")
    else:
        feedback.append("Password should contain at least one lowercase letter")
        
    if number_criteria:
        feedback.append("Contains number(s)")
    else:
        feedback.append("Password should contain at least one number")
        
    if special_char_criteria:
        feedback.append("Contains special character(s)")
    else:
        feedback.append("Password should contain at least one special character")
    
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    
    return strength_levels[strength_score], feedback

def main():
    print("Password Strength Assessment Tool")
    
    while True:
        password = input("Enter your password: ")
        
        strength, feedback = project(password)
        
        if strength != "Very Weak":
            break
        
        print("\nPassword Strength: Very Weak")
        print("Please follow the feedback to improve your password:")
        for comment in feedback:
            print(f"- {comment}")
        print("\nTry again.\n")
    
    print(f"\nPassword Strength: {strength}")
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")

if __name__ == "__main__":
    main()
