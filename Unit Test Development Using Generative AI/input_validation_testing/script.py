import re

def get_username():
    while True:
        username = input("Enter your username: ")
        # Simple validation to check for alphanumeric characters and underscores
        if re.match("^[a-zA-Z0-9_]*$", username):
            return username
        else:
            print("Invalid username. Only alphanumeric characters and underscores are allowed.")

def get_password():
    while True:
        password = input("Enter your password: ")
        # Password validation can be more complex, checking for length, complexity, etc.
        if len(password) >= 8:
            return password
        else:
            print("Invalid password. It must be at least 8 characters long.")

def get_email():
    while True:
        email = input("Enter your email address: ")
        # Simple regex pattern for validating an email address
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return email
        else:
            print("Invalid email address format.")

def get_sql_query():
    while True:
        query = input("Enter your SQL query: ")
        # This is a trivial check; in a real scenario, use parameterized queries or ORM
        if "DROP" not in query.upper() and "DELETE" not in query.upper():
            return query
        else:
            print("Invalid query. Destructive operations are not allowed.")

# Usage example
def main():
    username = get_username()
    password = get_password()
    email = get_email()
    query = get_sql_query()

    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")
    print(f"SQL Query: {query}")

if __name__ == "__main__":
    main()
