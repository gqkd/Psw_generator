import random
import string
import math

def generate_strong_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_-+=<>?[]{}"

    # Ensure at least one character from each character set
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_chars)

    # Generate the remaining characters randomly
    remaining_length = length - 4
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    password += ''.join(random.choice(all_chars) for _ in range(remaining_length))

    # Shuffle the characters to make it more secure
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def estimate_crack_time(password_length):
    # Assumptions for the estimation
    char_set_size = 94  # Total number of possible characters
    attempts_per_second = 1000000000  # Number of attempts per second (adjust as needed)
    seconds_in_a_day = 86400

    possible_combinations = char_set_size ** password_length
    seconds_to_crack = possible_combinations / attempts_per_second
    days_to_crack = seconds_to_crack / seconds_in_a_day

    return days_to_crack

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    
    strong_password = generate_strong_password(password_length)
    print("Generated Strong Password:", strong_password)
    
    estimated_crack_time = estimate_crack_time(password_length)
    print(f"Estimated Time to Crack: {estimated_crack_time:.2f} days")
