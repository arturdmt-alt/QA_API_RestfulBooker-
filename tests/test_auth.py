import pytest
from api.auth_api import AuthAPI


class TestAuth:
    """Tests de autenticación con parametrización"""
    
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
    
    # ✨ NUEVO: Test parametrizado con múltiples escenarios
    @pytest.mark.parametrize("username,password,should_pass", [
        ("admin", "password123", True),           # Valid credentials
        ("admin", "wrongpassword", False),        # Wrong password
        ("wronguser", "password123", False),      # Wrong username
        ("", "", False),                          # Empty credentials
        ("admin", "", False),                     # Empty password
        ("", "password123", False),               # Empty username
    ])
    def test_login_scenarios(self, auth_api, username, password, should_pass):
        """Test múltiples escenarios de login con parametrización"""
        if should_pass:
            # Should succeed
            token = auth_api.get_token(username, password)
            assert token is not None
            assert isinstance(token, str)
            assert len(token) > 0
        else:
            # Should fail
            with pytest.raises(Exception):
                auth_api.get_token(username, password)
                