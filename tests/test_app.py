import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.test_client() as client:
        yield client


def test_create_note(client):
    response = client.post(
        "/notes",
        json={"text": "Learn Flask"}
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["text"] == "Learn Flask"
    assert "id" in data


def test_get_notes(client):
    client.post(
        "/notes",
        json={"text": "Learn Docker"}
    )

    response = client.get("/notes")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 1
    assert data[0]["text"] == "Learn Docker"
