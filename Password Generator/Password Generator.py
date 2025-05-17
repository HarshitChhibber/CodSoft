import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    char_types = {
        "uppercase": string.ascii_uppercase if use_upper else '',
        "lowercase": string.ascii_lowercase if use_lower else '',
        "digits": string.digits if use_digits else '',
        "special": string.punctuation if use_special else ''
    }

    selected_sets = [chars for chars in char_types.values() if chars]

    if not selected_sets:
        return "Need to select at least 1 datatype."

    password_chars = [random.choice(chars) for chars in selected_sets]

    remaining_length = length - len(password_chars)
    combined_chars = ''.join(selected_sets)

    password_chars += [random.choice(combined_chars) for _ in range(remaining_length)]
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
    numbers = response("Include numbers?")
    special = response("Include special characters?")

    password = generate_password(length, uppercase, lowercase, numbers, special)
    print("\nGenerated Password:", password)

    if response("Do you want to save this password?"):
        website = input("Enter the Website Name/Link : ").strip()
        with open("Saved Passwords.txt", "a") as file:
            file.write(f"{website} - {password}\n")
        print("Password saved successfully to 'Saved Passwords.txt'.")

if __name__ == "__main__":
    main()