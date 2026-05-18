import pytest
from app import app, get_user_by_id, add_user, users
from calculator import add, subtract, multiply, divide, power

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Route tests ────────────────────────────────────────────

def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_running_status(client):
    response = client.get("/")
    data = response.get_json()
    assert data["status"] == "running"


def test_get_users_returns_list(client):
    response = client.get("/users")
    assert response.status_code == 200
    data = response.get_json()
    assert "users" in data
    assert "count" in data


def test_get_existing_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Alice"


def test_get_nonexistent_user_returns_404(client):
    response = client.get("/users/999")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data


# ── Logic tests ────────────────────────────────────────────

def test_get_user_by_id_found():
    user = get_user_by_id(1)
    assert user is not None
    assert user["name"] == "Alice"


def test_get_user_by_id_not_found():
    user = get_user_by_id(999)
    assert user is None


def test_add_user_success():
    new_user = add_user(99, "Charlie", "charlie@example.com")
    assert new_user["name"] == "Charlie"
    # Clean up
    users.remove(new_user)


def test_add_user_missing_name_raises_error():
    with pytest.raises(ValueError):
        add_user(100, "", "test@example.com")


def test_add_user_missing_email_raises_error():
    with pytest.raises(ValueError):
        add_user(100, "Test", "")

# def test_intentional_failure():
#     # Naam
#     assert False, "This test is intentionally broken"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(3, 2) == 9