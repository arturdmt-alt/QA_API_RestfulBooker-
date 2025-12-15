import pytest


class TestAuth:
    """Tests de autenticación"""
    
    def test_get_token_success(self, auth_api):
        """Verifica que se obtiene token con credenciales válidas"""
        token = auth_api.get_token("admin", "password123")
        
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
    
    def test_get_token_invalid_credentials(self, auth_api):
        """Verifica que falla con credenciales inválidas"""
        with pytest.raises(Exception):
            auth_api.get_token("invalid", "invalid")
            