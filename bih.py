import COVID19Py
import matplotlib.pyplot as plt

covid19 = COVID19Py.COVID19()

bih = covid19.getLocationByCountryCode("BA", timelines=True)
bih_confirmed = bih[0]['timelines']['confirmed']['timeline']
bih_recovered = bih[0]['timelines']['recovered']['timeline']
bih_deaths = bih[0]['timelines']['deaths']['timeline']


confirmed = []
recovered = []
deaths = []

for keys, values in bih_confirmed.items():
    confirmed.append(values)
for keys, values in bih_recovered.items():
    recovered.append(values)
for keys, values in bih_deaths.items():
    deaths.append(values)

print(confirmed)
print(recovered)
print(deaths)

zarazeni = confirmed[len(confirmed)-1]
oporavljeni = recovered[len(recovered)-1]
preminuli = deaths[len(deaths)-1]
aktivni = zarazeni - oporavljeni - preminuli


print(zarazeni, oporavljeni, preminuli)

x = [75,4,21]
la = ['Recovered', 'Deaths', 'Active']
plt.pie(x,labels=la)
plt.xlabel('Bosnia and Herzegovina')
plt.show()