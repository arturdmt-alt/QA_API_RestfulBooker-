import pytest
from models.booking_model import BookingModel


class TestBookings:
    """Tests de operaciones CRUD de reservas"""
    
    def test_create_booking(self, booking_api):
        """Verifica creación de reserva"""
        booking_data = BookingModel.create_default()
        response = booking_api.create_booking(booking_data)
        
        assert response.status_code == 200
        assert "bookingid" in response.json()
        assert response.json()["booking"]["firstname"] == "John"
    
    def test_get_booking(self, booking_api):
        """Verifica obtener reserva por ID"""
        # Primero crear una reserva
        booking_data = BookingModel.create_default()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        
        # Obtener la reserva
        response = booking_api.get_booking(booking_id)
        
        assert response.status_code == 200
        assert response.json()["firstname"] == "John"
    
    def test_get_all_bookings(self, booking_api):
        """Verifica obtener todas las reservas"""
        response = booking_api.get_all_bookings()
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
    
    def test_update_booking(self, booking_api, auth_token):
        """Verifica actualización completa de reserva"""
        # Crear reserva
        booking_data = BookingModel.create_default()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        
        # Actualizar reserva
        updated_data = BookingModel.create_booking(
            firstname="Jane",
            lastname="Smith",
            totalprice=200,
            depositpaid=False,
            checkin="2024-02-01",
            checkout="2024-02-10"
        )
        response = booking_api.update_booking(booking_id, updated_data, auth_token)
        
        assert response.status_code == 200
        assert response.json()["firstname"] == "Jane"
        assert response.json()["totalprice"] == 200
    
    def test_partial_update_booking(self, booking_api, auth_token):
        """Verifica actualización parcial de reserva"""
        # Crear reserva
        booking_data = BookingModel.create_default()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        
        # Actualizar solo firstname
        partial_data = {"firstname": "UpdatedName"}
        response = booking_api.partial_update_booking(booking_id, partial_data, auth_token)
        
        assert response.status_code == 200
        assert response.json()["firstname"] == "UpdatedName"
    
    def test_delete_booking(self, booking_api, auth_token):
        """Verifica eliminación de reserva"""
        # Crear reserva
        booking_data = BookingModel.create_default()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        
        # Borrar reserva
        response = booking_api.delete_booking(booking_id, auth_token)
        
        assert response.status_code == 201
    
    def test_create_booking_missing_fields(self, booking_api):
        """Verifica que falla al crear reserva sin campos obligatorios"""
        invalid_data = {
            "firstname": "John"
            # Faltan campos obligatorios
        }
        response = booking_api.create_booking(invalid_data)
        
        assert response.status_code == 500
    
    def test_get_nonexistent_booking(self, booking_api):
        """Verifica manejo de reserva inexistente"""
        response = booking_api.get_booking(999999)
        
        assert response.status_code == 404
    
    def test_delete_without_token(self, booking_api):
        """Verifica que falla al borrar sin token"""
        # Crear reserva primero
        booking_data = BookingModel.create_default()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        
        # Intentar borrar sin token
        response = booking_api.delete_booking(booking_id, "")
        
        assert response.status_code == 403
        
        
        
        