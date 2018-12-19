#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway
import urllib.request
import numpy as np
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib as mpl
response = urllib.request.urlopen('http://localhost:8080/')
resp = response.read().decode()
time =[]
temp=[]
head = ET.fromstring(resp)
for reading in head.findall('reading'):
    time.append(reading.find('time').text)
    temp.append(int(reading.find('temperature').text))
plt.title("Temperature and Timing Graph")
plt.xlabel("Timing")
plt.ylabel("Temperature")
plt.grid(True)
plt.plot(time,temp,'k')
plt.show()
