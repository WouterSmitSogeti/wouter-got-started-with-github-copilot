def test_get_activities_returns_expected_structure(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "Programming Class" in payload
    assert "Gym Class" in payload

    chess = payload["Chess Club"]
    assert {"description", "schedule", "max_participants", "participants"}.issubset(chess.keys())
    assert isinstance(chess["participants"], list)
    assert len(chess["participants"]) == 2