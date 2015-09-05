import dataset
from subprocess import check_output
import datetime
import time

db = dataset.connect('sqlite:///database.db')

while 1:
    table = db['temperaturevalues']
    currentTemperature = check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"])
    currentTime = unicode(datetime.datetime.now())
    value = dict(time=currentTime, temperature=currentTemperature)
    table.insert(value)
    print value
    time.sleep(1);
