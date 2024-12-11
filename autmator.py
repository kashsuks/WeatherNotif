from datetime import datetime
from threading import Timer
from getWeatherData import getWeather

x=datetime.today()
y=x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

f = open("location.txt", "r")

t = Timer(secs, getWeather(f))
t.start()