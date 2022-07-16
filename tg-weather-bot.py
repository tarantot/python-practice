import pyowm

owm = pyowm.OWM('c94fb94308a70fa7a37d63a0ab280604', language = "eng")

place = input("In which city/country?: ")

observation = owm.weather_at_place('place')
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]
wind = w.get_wind()

print( "The temperature is around " + str(temp) + "°C now in " + place)
print( "The wind speed is around " + str(wind) + "km/h.")
print( "It is " + w.get_detailed_status() + " now in " + place)

if temp < 0:
    print( "It is freezing there! Try to stay indoors today.")
elif temp <10:
    print( "It is still cold, please wear more clothes.")
elif temp <20:
    print( "It is not so warm yet, a jacket will not be excess.")
elif temp <28:
    print( "Finally it is summer! Enjoy it ;-)")
elif temp >28:
    print( "It is heat there like on a fiery pan!")