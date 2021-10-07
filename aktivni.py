import COVID19Py
import matplotlib.pyplot as plt

covid19 = COVID19Py.COVID19()

states = ['AD', 'AF', 'AG', 'AL', 'AU', 'BA', 'BB', 'BO', 'BR', 'DZ']
states_cases = []

ad = covid19.getLocationByCountryCode("AD", timelines=True)
ad_confirmed = ad[0]['timelines']['confirmed']['timeline']
ad_deaths = ad[0]['timelines']['deaths']['timeline']
ad_recovered = ad[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in ad_confirmed.items():
    confirmed.append(values)
for keys, values in ad_recovered.items():
    recovered.append(values)
for keys, values in ad_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
ad_cases = x-y-z
states_cases.append(ad_cases)

af = covid19.getLocationByCountryCode("AF", timelines=True)
af_confirmed = af[0]['timelines']['confirmed']['timeline']
af_deaths = af[0]['timelines']['deaths']['timeline']
af_recovered = af[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in af_confirmed.items():
    confirmed.append(values)
for keys, values in af_recovered.items():
    recovered.append(values)
for keys, values in af_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
af_cases= x-y-z
states_cases.append(af_cases)

ag = covid19.getLocationByCountryCode("AG", timelines=True)
ag_confirmed = ag[0]['timelines']['confirmed']['timeline']
ag_deaths = ag[0]['timelines']['deaths']['timeline']
ag_recovered = ag[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in ag_confirmed.items():
    confirmed.append(values)
for keys, values in ag_recovered.items():
    recovered.append(values)
for keys, values in ag_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
ag_cases = x-y-z
states_cases.append(ag_cases)

al = covid19.getLocationByCountryCode("AL", timelines=True)
al_confirmed = al[0]['timelines']['confirmed']['timeline']
al_deaths = al[0]['timelines']['deaths']['timeline']
al_recovered = al[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in al_confirmed.items():
    confirmed.append(values)
for keys, values in al_recovered.items():
    recovered.append(values)
for keys, values in al_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
al_cases =x-y-z
states_cases.append(al_cases)

au = covid19.getLocationByCountryCode("AU", timelines=True)
au_confirmed = au[0]['timelines']['confirmed']['timeline']
au_deaths = au[0]['timelines']['deaths']['timeline']
au_recovered = au[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in au_confirmed.items():
    confirmed.append(values)
for keys, values in au_recovered.items():
    recovered.append(values)
for keys, values in au_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
au_cases = x-y-z
states_cases.append(au_cases)

bih = covid19.getLocationByCountryCode("BA", timelines=True)
bih_confirmed = bih[0]['timelines']['confirmed']['timeline']
bih_deaths = bih[0]['timelines']['deaths']['timeline']
bih_recovered = bih[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in bih_confirmed.items():
    confirmed.append(values)
for keys, values in bih_recovered.items():
    recovered.append(values)
for keys, values in bih_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
bih_cases = x-y-z
states_cases.append(bih_cases)

bb = covid19.getLocationByCountryCode("BB", timelines=True)
bb_confirmed = bb[0]['timelines']['confirmed']['timeline']
bb_deaths = bb[0]['timelines']['deaths']['timeline']
bb_recovered = bb[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in bb_confirmed.items():
    confirmed.append(values)
for keys, values in bb_recovered.items():
    recovered.append(values)
for keys, values in bb_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
bb_cases = x-y-z
states_cases.append(bb_cases)

bo = covid19.getLocationByCountryCode("BO", timelines=True)
bo_confirmed = bo[0]['timelines']['confirmed']['timeline']
bo_deaths = bo[0]['timelines']['deaths']['timeline']
bo_recovered = bo[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in bo_confirmed.items():
    confirmed.append(values)
for keys, values in bo_recovered.items():
    recovered.append(values)
for keys, values in bo_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
bo_cases = x-y-z
states_cases.append(bo_cases)

br = covid19.getLocationByCountryCode("BR", timelines=True)
br_confirmed = br[0]['timelines']['confirmed']['timeline']
br_deaths = br[0]['timelines']['deaths']['timeline']
br_recovered = br[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in br_confirmed.items():
    confirmed.append(values)
for keys, values in br_recovered.items():
    recovered.append(values)
for keys, values in br_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
br_cases = x-y-z
states_cases.append(br_cases)

dz = covid19.getLocationByCountryCode("DZ", timelines=True)
dz_confirmed = dz[0]['timelines']['confirmed']['timeline']
dz_deaths = dz[0]['timelines']['deaths']['timeline']
dz_recovered = dz[0]['timelines']['recovered']['timeline']

confirmed = []
deaths = []
recovered = []
for keys, values in dz_confirmed.items():
    confirmed.append(values)
for keys, values in dz_recovered.items():
    recovered.append(values)
for keys, values in dz_deaths.items():
    deaths.append(values)
x = confirmed[len(confirmed)-1]
y = deaths[len(deaths)-1]
z = recovered[len(recovered)-1]
dz_cases = x-y-z
states_cases.append(dz_cases)

plt.bar(states,states_cases)
plt.xlabel('Drzave')
plt.ylabel('Broj aktivnih slucajeva na danasnji dan')
plt.show()