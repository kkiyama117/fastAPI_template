import json

# TODO: implement


def test_get(scope_module):
    client = scope_module
    headers = {"content-type": "application/json", "origin": "http://localhost:3000"}
    res = client.get("/v1/users/", headers=headers)
    assert res.status_code == 200


def test_create(scope_module):
    client = scope_module
    email = "test@test.com"
    headers = {"content-type": "application/json"}
    res = client.post("/v1/users/", headers=headers, data=json.dumps({"email": email}))
    assert res.status_code == 201
    data = json.loads(res.content)
    assert data.get("email") == email
