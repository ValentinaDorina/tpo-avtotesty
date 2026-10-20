# -*- coding: utf-8 -*-
"""ЛР5. Python-эквивалент Postman-тестов для reqres.in (requests + pytest).
Повторяет логику тестов из Postman-коллекции."""

import pytest
import requests

BASE = "https://reqres.in/api"


@pytest.fixture(scope="session")
def http():
    s = requests.Session()
    yield s
    s.close()


# ---------- GET: получить пользователя ----------
def test_get_user_status_200(http):
    resp = http.get(f"{BASE}/users/2")
    assert resp.status_code == 200


def test_get_user_has_id_and_email(http):
    resp = http.get(f"{BASE}/users/2")
    data = resp.json()["data"]
    assert "id" in data
    assert "email" in data
    assert data["id"] == 2


# ---------- POST: создать пользователя ----------
def test_post_creates_user_status_201(http):
    resp = http.post(f"{BASE}/users",
                     json={"name": "morpheus", "job": "leader"})
    assert resp.status_code == 201


def test_post_creates_user_has_id_and_createdAt(http):
    resp = http.post(f"{BASE}/users",
                     json={"name": "morpheus", "job": "leader"})
    body = resp.json()
    assert "id" in body
    assert "createdAt" in body
    assert body["name"] == "morpheus"
    assert body["job"] == "leader"


# ---------- PUT: обновить пользователя ----------
def test_put_updates_user_status_200(http):
    resp = http.put(f"{BASE}/users/2",
                    json={"name": "morpheus", "job": "zion resident"})
    assert resp.status_code == 200


def test_put_updates_user_has_updatedAt(http):
    resp = http.put(f"{BASE}/users/2",
                    json={"name": "morpheus", "job": "zion resident"})
    body = resp.json()
    assert "updatedAt" in body
    assert body["name"] == "morpheus"