from api.base_api import BaseAPI


class AuthAPI(BaseAPI):
    """Maneja autenticación y tokens"""
    
    def get_token(self, username, password):
        """
        Obtiene token de autenticación
        
        Args:
            username: Usuario (ej: "admin")
            password: Contraseña (ej: "password123")
        
        Returns:
            str: Token de autenticación
        """
        data = {
            "username": username,
            "password": password
        }
        
        response = self.post("/auth", data=data)
        
        if response.status_code == 200:
            return response.json()["token"]
        else:
            raise Exception(f"Error al obtener token: {response.status_code}")
        