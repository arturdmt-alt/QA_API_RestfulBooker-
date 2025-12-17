import pytest
from pydantic import ValidationError
from api.booking_api import BookingAPI
from api.auth_api import AuthAPI
from models.booking_model import BookingModel
from schemas.booking_schema import (
    CreateBookingResponse,
    GetBookingResponse,
    AuthTokenResponse,
    BookingDates
)


class TestSchemaValidation:
    """Tests de validación de schemas con Pydantic"""
    
    @pytest.mark.smoke
    def test_create_booking_schema(self, booking_api):
        """Valida que response de crear reserva cumple con schema"""
        booking_data = BookingModel.create_default()
        response = booking_api.create_booking(booking_data)
        
        # Validar estructura con Pydantic
        validated_response = CreateBookingResponse(**response.json())
        
        # Assertions adicionales
        assert validated_response.bookingid > 0
        assert validated_response.booking.firstname == "John"
        assert validated_response.booking.totalprice == 150
    
    @pytest.mark.smoke
    def test_get_booking_schema(self, booking_api):
        """Valida que response de obtener reserva cumple con schema"""
        # Crear reserva primero
        booking_data = BookingModel.create_default()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        
        # Obtener reserva
        response = booking_api.get_booking(booking_id)
        
        # Validar estructura con Pydantic
        validated_response = GetBookingResponse(**response.json())
        
        assert validated_response.firstname == "John"
        assert validated_response.totalprice == 150
    
    @pytest.mark.smoke
    def test_auth_token_schema(self, auth_api):
        """Valida que response de auth cumple con schema"""
        token = auth_api.get_token("admin", "password123")
        
        # Validar estructura
        validated_response = AuthTokenResponse(token=token)
        
        assert len(validated_response.token) > 0
    
    @pytest.mark.negative
    def test_invalid_booking_data_type(self, booking_api):
        """Valida que schema rechaza tipos incorrectos"""
        booking_data = BookingModel.create_default()
        response = booking_api.create_booking(booking_data)
        
        # Modificar response para tener tipo incorrecto
        invalid_data = response.json()
        invalid_data["bookingid"] = "STRING_NOT_INT"  # ❌ Debe ser int
        
        # Debe lanzar ValidationError
        with pytest.raises(ValidationError):
            CreateBookingResponse(**invalid_data)
    
    @pytest.mark.negative
    def test_missing_required_field(self):
        """Valida que schema rechaza campos faltantes"""
        incomplete_data = {
            "bookingid": 123
            # Falta campo "booking" (requerido)
        }
        
        with pytest.raises(ValidationError):
            CreateBookingResponse(**incomplete_data)
    
    @pytest.mark.regression
    def test_booking_dates_schema(self):
        """Valida schema de fechas de reserva"""
        dates = {
            "checkin": "2024-01-01",
            "checkout": "2024-01-10"
        }
        
        validated_dates = BookingDates(**dates)
        
        assert validated_dates.checkin == "2024-01-01"
        assert validated_dates.checkout == "2024-01-10"
    
    @pytest.mark.regression
    def test_totalprice_must_be_positive(self):
        """Valida que totalprice debe ser positivo"""
        invalid_booking = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": -100,  # ❌ Negativo no válido
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-10"
            }
        }
        
        with pytest.raises(ValidationError) as exc_info:
            from schemas.booking_schema import Booking
            Booking(**invalid_booking)
        
        # Verificar que el error es sobre totalprice
        assert "totalprice" in str(exc_info.value)
        
        