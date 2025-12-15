import pytest
from api.auth_api import AuthAPI
from api.booking_api import BookingAPI


BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def auth_api():
    """Fixture para AuthAPI"""
    return AuthAPI(BASE_URL)


@pytest.fixture
def booking_api():
    """Fixture para BookingAPI"""
    return BookingAPI(BASE_URL)


@pytest.fixture
def auth_token(auth_api):
    """Fixture que retorna un token válido"""
    token = auth_api.get_token("admin", "password123")
    return token
