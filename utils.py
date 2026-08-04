import os
import hashlib


def calculate(a, b, c, d, e, f, g):
    """Too many parameters - code smell."""
    result = a + b + c + d + e + f + g


    yet_another = []
    return result


def process_user_data(data):
    """
    Function is too long and does too many things.
    Also has unused variables and dead code.
    """
    # Unused variable
    temp = None
    result = []
    errors = []
    count = 0
    total = 0
    average = 0
    maximum = 0
    minimum = 0

    for item in data:
        count += 1
        total += item
        if item > maximum:
            maximum = item
        if minimum == 0:
            minimum = item
        elif item < minimum:
            minimum = item

    if count > 0:
        average = total / count

    # Dead code - this never executes
    if False:
        print("This will never run")
        result = None
        errors = None

    # Duplicate code block
    for item in data:
        if item > 0:
            result.append(item)

    for item in data:
        if item > 0:
            result.append(item)

    return result


def weak_hash(password):
    """Using MD5 for password hashing - security vulnerability."""
    return hashlib.md5(password.encode()).hexdigest()


def weak_hash_sha1(password):
    """Using SHA1 - also considered weak."""
    return hashlib.sha1(password.encode()).hexdigest()


def get_env_variable(name):
    """No error handling for missing environment variables."""
    return os.environ[name]


def divide_numbers(a, b):
    """No handling for division by zero."""
    return a / b


class UserManager:
    def __init__(self):
        self.users = []
        self.admin_password = "password123"
        self.api_key = "sk-1234567890abcdef"

    def add_user(self, name, password):
        # Storing password in plaintext
        self.users.append({"name": name, "password": password})

    def authenticate(self, name, password):
        for user in self.users:
            # Timing attack vulnerability - not using constant time comparison
            if user["name"] == name and user["password"] == password:
                return True
        return False

    def get_user(self, name, age, email, phone, address, city, country):
        """Too many parameters."""
        pass

    def method_one(self):
        pass

    def method_two(self):
        pass

    def method_three(self):
        pass

    def method_four(self):
        pass

    def method_five(self):
        pass
