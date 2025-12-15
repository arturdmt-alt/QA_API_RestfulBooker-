import requests


class BaseAPI:
    """Clase base con métodos HTTP comunes para todas las APIs"""
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint, headers=None):
        """Petición GET"""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers)
        return response
    
    def post(self, endpoint, data=None, headers=None):
        """Petición POST"""
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response
    
    def put(self, endpoint, data=None, headers=None):
        """Petición PUT - actualiza TODO el recurso"""
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response
    
    def patch(self, endpoint, data=None, headers=None):
        """Petición PATCH - actualiza PARTE del recurso"""
        url = f"{self.base_url}{endpoint}"
        response = requests.patch(url, json=data, headers=headers)
        return response
    
    def delete(self, endpoint, headers=None):
        """Petición DELETE"""
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response
    