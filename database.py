import sqlite3

# Hardcoded credentials - security vulnerability
DB_PASSWORD = "admin123"
DB_USER = "root"
SECRET_KEY = "hardcoded-secret-key-12345"






def get_connection():
    return sqlite3.connect("users.db")


def find_user_by_name(username):
    """
    SQL Injection vulnerability - user input directly
    concatenated into SQL query without sanitization.
    """
    conn = get_connection()
    cursor = conn.cursor()
    # VULNERABLE: direct string concatenation
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def find_user_by_id(user_id):
    """
    Another SQL injection vulnerability.
    """
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    cursor.execute(query)
    return cursor.fetchone()


def delete_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    # VULNERABLE: no input validation
    query = "DELETE FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    conn.commit()


def get_all_passwords():
    """Returns all passwords in plaintext - bad practice."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users")
    return cursor.fetchall()
