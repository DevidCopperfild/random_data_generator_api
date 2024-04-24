import random
import string

def generate_random_data(data_type, count):
    if data_type == "name":
        return [generate_random_name() for _ in range(count)]
    elif data_type == "surname":
        return [generate_random_surname() for _ in range(count)]
    elif data_type == "address":
        return [generate_random_address() for _ in range(count)]
    elif data_type == "email":
        return [generate_random_email() for _ in range(count)]
    elif data_type == "phone_number":
        return [generate_random_phone_number() for _ in range(count)]
    else:
        return {"error": "Invalid data type"}

def generate_random_name():
    return random.choice(["John", "Jane", "Alice", "Bob", "Charlie"])

def generate_random_surname():
    return random.choice(["Doe", "Smith", "Johnson", "Brown", "Taylor"])

def generate_random_address():
    return f"{random.randint(1, 1000)} {random.choice(['Main', 'High', 'Park'])} St, {random.choice(['New York', 'Los Angeles', 'Chicago'])}"

def generate_random_email():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10)) + "@gmail.com"

def generate_random_phone_number():
    return f"+7-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000,9999)}"