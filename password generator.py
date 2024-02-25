import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    username = input("Enter your username: ")
    password_name = input("Enter the name for which you want to generate a password: ")
    length = int(input("Enter the length of the password: "))
    
    generated_password = generate_password(length)
    print("Generated Password:", generated_password)
    
    accept = input("Do you accept this password? (yes/no): ")
    if accept.lower() == "yes":
        print("Password accepted for '{}' with username '{}'.".format(password_name, username))
    else:
        print("Password reset.")
        main()  # Restart the process if the user does not accept the generated password

if __name__ == "__main__":
    main()

