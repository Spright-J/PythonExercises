class Temperature:
    def __init__(self):
        self._kelvin = 0.0  # Initialize the temperature in Kelvin
    
    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, value):
        self._kelvin = value

    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15

    @property
    def fahrenheit(self):
        return (self._kelvin - 273.15) * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._kelvin = (value - 32) * 5/9 + 273.15


t1 = Temperature()
print("Kelvin:", t1.kelvin)  # 0.0
print("Celsius:", t1.celsius)  # -273.15
print("Fahrenheit:", t1.fahrenheit)  # -459.67