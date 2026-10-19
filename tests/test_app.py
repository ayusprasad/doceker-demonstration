from __future__ import annotations

from app import app


def test_home_page_contains_name_form() -> None:
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b'name="username"' in response.data


def test_greeting_escapes_user_input() -> None:
    response = app.test_client().post("/greet", data={"username": "<script>alert(1)</script>"})
    assert response.status_code == 200
    assert b"&lt;script&gt;" in response.data
    assert b"<script>" not in response.data


def test_empty_greeting_is_rejected() -> None:
    response = app.test_client().post("/greet", data={"username": " "})
    assert response.status_code == 400
