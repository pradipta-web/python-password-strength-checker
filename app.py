import string
from colorama import init, Fore, Style

init(autoreset=True)


def check_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    return score, suggestions


def display_result(score, suggestions):
    print("\n" + "=" * 45)
    print("             PASSWORD RESULT")
    print("=" * 45)

    print(f"Score: {score}/5")

    if score <= 2:
        print(Fore.RED + "Strength: WEAK")
    elif score <= 4:
        print(Fore.YELLOW + "Strength: MEDIUM")
    else:
        print(Fore.GREEN + "Strength: STRONG")

    if suggestions:
        print("\nSuggestions:")

        for suggestion in suggestions:
            print(Fore.YELLOW + f"- {suggestion}")
    else:
        print(Fore.GREEN + "\nYour password meets all basic checks!")

    print("=" * 45)


def main():
    while True:
        print("\n" + "=" * 45)
        print("       PASSWORD STRENGTH CHECKER")
        print("=" * 45)

        password = input("\nEnter your password: ")

        if not password:
            print(Fore.RED + "Password cannot be empty!")
            continue

        score, suggestions = check_password(password)

        display_result(score, suggestions)

        again = input(
            "\nCheck another password? (y/n): "
        ).strip().lower()

        if again != "y":
            print(
                Fore.GREEN +
                "\nThank you for using Password Strength Checker!"
            )
            break


if __name__ == "__main__":
    main()