class BookingModel:
    """Modelo de datos para una reserva"""
    
    @staticmethod
    def create_booking(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds=None):
        """Crea un booking con datos personalizados"""
        booking = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            }
        }
        
        if additionalneeds:
            booking["additionalneeds"] = additionalneeds
        
        return booking
    
    @staticmethod
    def create_default():
        """Crea un booking con datos de prueba por defecto"""
        return BookingModel.create_booking(
            firstname="John",
            lastname="Doe",
            totalprice=150,
            depositpaid=True,
            checkin="2024-01-01",
            checkout="2024-01-05",
            additionalneeds="Breakfast"
        )
        