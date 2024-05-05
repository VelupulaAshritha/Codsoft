mport string
import secrets


def generate_password(length: int, special_characters: bool):
    # Internal password constraints
    num_digits = length // 4
    num_special_characters = length // 5
    num_letters = length - (num_digits + num_special_characters)
    num_uppercase, num_lowercase = num_letters // 3, num_letters // 3
    num_letters -= num_uppercase + num_lowercase

    # Generate random characters for every constraint
    pool = (
        "".join(secrets.choice(string.ascii_uppercase) for _ in range(num_uppercase))
        + "".join(secrets.choice(string.ascii_lowercase) for _ in range(num_lowercase))
        + "".join(secrets.choice(string.ascii_letters) for _ in range(num_letters))
        + "".join(secrets.choice(string.digits) for _ in range(num_digits))
    )

    if special_characters:
        pool += "".join(
            secrets.choice(string.punctuation) for _ in range(num_special_characters)
        )

    # Shuffle the string to randomize the order of characters
    pw_list = list(pool)
    secrets.SystemRandom().shuffle(pw_list)

    return "".join(pw_list)


def main():
    print("Random Password Generator")
    print("=========================")

    # Prompt user for password length
    pw_len = input("Enter the length of the password [12-32] (default: 16): ").strip()

    # Ensure validity of given input
    if pw_len:
        try:
            pw_len = int(pw_len)

            if pw_len not in range(8, 33):
                raise ValueError

        except ValueError:
            return print("Invalid length entered!")

    # Prompt user on whether to include special characters
    pw_sp_chr = input("Include special characters (!@#$%)? [Yes/No]: ")

    # Ensure validity of given input
    if pw_sp_chr.lower() not in ["yes", "no"]:
        return print("Invalid response!")

    # Generate a password per the input
    res = generate_password(
        length=pw_len if pw_len else 16,
        special_characters=True if pw_sp_chr.lower() == "yes" else False,
    )

    print(f"Generated Password: {res}")


if __name__ == "__main__":
    main()