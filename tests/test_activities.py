def test_get_activities_returns_expected_payload(client):
    response = client.get("/activities")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_get_activities_items_have_required_fields(client):
    response = client.get("/activities")
    data = response.json()

    required_keys = {"description", "schedule", "max_participants", "participants"}

    for details in data.values():
        assert required_keys.issubset(details.keys())
        assert isinstance(details["description"], str)
        assert isinstance(details["schedule"], str)
        assert isinstance(details["max_participants"], int)
        assert isinstance(details["participants"], list)
