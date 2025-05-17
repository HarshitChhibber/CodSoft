import random
import string

def generate_password(length, uppercase, lowercase, digits, special):
    selected_sets = []
    password_chars = []

    if uppercase:
        selected_sets.append(string.ascii_uppercase)
        password_chars.append(random.choice(string.ascii_uppercase))
    if lowercase:
        selected_sets.append(string.ascii_lowercase)
        password_chars.append(random.choice(string.ascii_lowercase))
    if digits:
        selected_sets.append(string.digits)
        password_chars.append(random.choice(string.digits))
    if special:
        selected_sets.append(string.punctuation)
        password_chars.append(random.choice(string.punctuation))

    if not selected_sets:
        return "Error: No character types selected."

    combined_chars = ''.join(selected_sets)

    remaining_length = length - len(password_chars)
    password_chars.extend(random.choice(combined_chars) for _ in range(remaining_length))

    random.shuffle(password_chars)

    return ''.join(password_chars)

def response(prompt):
    choice = input(prompt + " (y/n): ").strip().lower()
    return choice == 'y'

def main():
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password Length needs to be at least 4 characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    uppercase = response("Include uppercase letters?")
    lowercase = response("Include lowercase letters?")
    digits = response("Include digits?")
    special = response("Include special characters?")

    password = generate_password(length, uppercase, lowercase, digits, special)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()