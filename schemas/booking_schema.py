from pydantic import BaseModel, Field
from typing import Optional


class BookingDates(BaseModel):
    """Schema para fechas de check-in y check-out"""
    checkin: str = Field(..., description="Check-in date in YYYY-MM-DD format")
    checkout: str = Field(..., description="Check-out date in YYYY-MM-DD format")


class Booking(BaseModel):
    """Schema para datos de una reserva"""
    firstname: str = Field(..., min_length=1, description="Guest first name")
    lastname: str = Field(..., min_length=1, description="Guest last name")
    totalprice: int = Field(..., gt=0, description="Total price (must be positive)")
    depositpaid: bool = Field(..., description="Deposit payment status")
    bookingdates: BookingDates = Field(..., description="Check-in and check-out dates")
    additionalneeds: Optional[str] = Field(None, description="Additional needs (optional)")


class CreateBookingResponse(BaseModel):
    """Schema para response de crear reserva"""
    bookingid: int = Field(..., description="Unique booking ID")
    booking: Booking = Field(..., description="Booking details")


class GetBookingResponse(BaseModel):
    """Schema para response de obtener reserva (hereda de Booking)"""
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None


class AuthTokenResponse(BaseModel):
    """Schema para response de autenticación"""
    token: str = Field(..., min_length=1, description="Authentication token")
    
    