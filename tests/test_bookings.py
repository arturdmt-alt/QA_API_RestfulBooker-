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
        