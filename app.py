# DevOps Lab API - webhook trigger test
# DevOps Lab API - webhook trigger test 2
# DevOps Lab API - full data collection pipeline trigger test 1
# DevOps Lab API - full data collection pipeline trigger test 2
# DevOps Lab API - full data collection pipeline trigger test 3
# DevOps Lab API - full data collection pipeline trigger test 4
# DevOps Lab API - full data collection pipeline trigger test 5
# DevOps Lab API - full data collection pipeline trigger test 6
# DevOps Lab API - full data collection pipeline trigger test 7
# DevOps Lab API - full data collection pipeline trigger test 8


# DevOps Lab API - full data collection pipeline trigger with frontend test 1
# DevOps Lab API - full data collection pipeline trigger with frontend test 2
# DevOps Lab API - full data collection pipeline trigger with frontend test 3
# DevOps Lab API - full data collection pipeline trigger with frontend test 4

# DevOps Lab API - full data collection pipeline trigger with frontend test 5
# DevOps Lab API - full data collection pipeline trigger with frontend test 6
# DevOps Lab API - full data collection pipeline trigger with frontend test 7

# DevOps Lab API - full testing 1
from flask import Flask, jsonify

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob",   "email": "bob@example.com"},
]


def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def add_user(user_id, name, email):
    if not name or not email:
        raise ValueError("Name and email are required")
    new_user = {"id": user_id, "name": name, "email": email}
    users.append(new_user)
    return new_user



@app.route("/")
def home():
    return jsonify({"message": "DevOps Lab API", "status": "running"})


@app.route("/users")
def get_users():
    return jsonify({"users": users, "count": len(users)})


@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
