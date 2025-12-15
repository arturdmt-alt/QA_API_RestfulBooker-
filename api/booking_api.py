from api.base_api import BaseAPI


class BookingAPI(BaseAPI):
    """Maneja operaciones CRUD de reservas"""
    
    def create_booking(self, data):
        """Crea una nueva reserva"""
        response = self.post("/booking", data=data)
        return response
    
    def get_booking(self, booking_id):
        """Obtiene una reserva por ID"""
        response = self.get(f"/booking/{booking_id}")
        return response
    
    def get_all_bookings(self):
        """Obtiene todas las reservas"""
        response = self.get("/booking")
        return response
    
    def update_booking(self, booking_id, data, token):
        """Actualiza una reserva completa (PUT)"""
        headers = {"Cookie": f"token={token}"}
        response = self.put(f"/booking/{booking_id}", data=data, headers=headers)
        return response
    
    def partial_update_booking(self, booking_id, data, token):
        """Actualiza parte de una reserva (PATCH)"""
        headers = {"Cookie": f"token={token}"}
        response = self.patch(f"/booking/{booking_id}", data=data, headers=headers)
        return response
    
    def delete_booking(self, booking_id, token):
        """Borra una reserva"""
        headers = {"Cookie": f"token={token}"}
        response = self.delete(f"/booking/{booking_id}", headers=headers)
        return response
    