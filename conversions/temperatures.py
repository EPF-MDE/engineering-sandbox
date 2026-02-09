#Conversions for temperatures : Celsius, Farenheit and Kelvin
def celsius_to_fahrenheit(c: float):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float):
    return c + 273.15


def kelvin_to_celsius(k: float):
    return k - 273.15


def fahrenheit_to_kelvin(f: float):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k: float):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))
