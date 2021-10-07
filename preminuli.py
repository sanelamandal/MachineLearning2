import COVID19Py
import matplotlib.pyplot as plt

covid19 = COVID19Py.COVID19()

states = ['AD', 'AF', 'AG', 'AL' , 'AU', 'BA', 'BB', 'BO', 'BR', 'DZ']

bih = covid19.getLocationByCountryCode("BA", timelines=True)
bih_deaths = bih[0]['timelines']['deaths']['timeline']

al = covid19.getLocationByCountryCode("AL", timelines=True)
al_deaths = al[0]['timelines']['deaths']['timeline']

af = covid19.getLocationByCountryCode("AF", timelines=True)
af_deaths = af[0]['timelines']['deaths']['timeline']

br = covid19.getLocationByCountryCode("BR", timelines=True)
br_deaths = br[0]['timelines']['deaths']['timeline']

dz = covid19.getLocationByCountryCode("DZ", timelines=True)
dz_deaths = dz[0]['timelines']['deaths']['timeline']

ad = covid19.getLocationByCountryCode("AD", timelines=True)
ad_deaths = ad[0]['timelines']['deaths']['timeline']

ag = covid19.getLocationByCountryCode("AG", timelines=True)
ag_deaths = ag[0]['timelines']['deaths']['timeline']

bb = covid19.getLocationByCountryCode("BB", timelines=True)
bb_deaths = bb[0]['timelines']['deaths']['timeline']

bo = covid19.getLocationByCountryCode("BO", timelines=True)
bo_deaths = bo[0]['timelines']['deaths']['timeline']

au = covid19.getLocationByCountryCode("AU", timelines=True)
au_deaths = au[0]['timelines']['deaths']['timeline']

#BROJ PREMINULIH PO DRZAVAMA NA DANASNJI DAN!
dates = []
deaths = []
deaths_by_date = []
states_deaths = []

previous = 0
for keys, values in ad_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
ad_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(ad_current)

deaths_by_date = []
previous = 0
for keys, values in af_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
af_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(af_current)

deaths_by_date = []
previous = 0
for keys, values in ag_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
ag_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(ag_current)

deaths_by_date = []
previous = 0
for keys, values in al_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
al_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(al_current)

deaths_by_date = []
previous = 0
for keys, values in au_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
au_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(au_current)

deaths_by_date = []
previous = 0
for keys, values in bih_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
bih_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(bih_current)

deaths_by_date = []
previous = 0
for keys, values in bb_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
bb_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(bb_current)

deaths_by_date = []
previous = 0
for keys, values in bo_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
bo_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(bo_current)


deaths_by_date = []
previous = 0
for keys, values in br_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
br_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(br_current)

deaths_by_date = []
previous = 0
for keys, values in dz_deaths.items():
    dates.append(keys)
    deaths.append(values)
    deaths_by_date.append(values-previous)
    previous = values
dz_current = deaths_by_date[len(deaths_by_date)-1]
states_deaths.append(dz_current)


plt.bar(states,states_deaths)
plt.xlabel('Drzave')
plt.ylabel('Broj smrtnih slucajeva na danasnji dan')
plt.show()