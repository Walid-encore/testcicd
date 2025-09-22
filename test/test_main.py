from fastapi.testclient import TestClient
from src.main import api  

client = TestClient(api)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}

def test_add_ticket():
    ticket_data = {
        "id": 1,
        "flight_name": "Flight A",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "New York"
    }
    response = client.post("/ticket", json=ticket_data)
    assert response.status_code == 200
    assert response.json() == ticket_data

def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    tickets = response.json()
    assert isinstance(tickets, list)
    assert len(tickets) >= 1

def test_update_ticket():
    updated_ticket = {
        "id": 1,
        "flight_name": "Flight A Updated",
        "flight_date": "2025-10-16",
        "flight_time": "16:00",
        "destination": "Boston"
    }
    response = client.put("/ticket/1", json=updated_ticket)
    assert response.status_code == 200
    assert response.json() == updated_ticket

def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    deleted_ticket = response.json()
    assert deleted_ticket["id"] == 1

def test_delete_nonexistent_ticket():
    response = client.delete("/ticket/999")
    assert response.status_code == 200
    assert response.json() == {"error": "Ticket not found, deletion failed"}