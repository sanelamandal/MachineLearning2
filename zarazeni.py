import COVID19Py
import matplotlib.pyplot as plt

covid19 = COVID19Py.COVID19()

states = ['AD', 'AF', 'AG', 'AL' , 'AU', 'BA', 'BB', 'BO', 'BR', 'DZ']

bih = covid19.getLocationByCountryCode("BA", timelines=True)
bih_confirmed = bih[0]['timelines']['confirmed']['timeline']

al = covid19.getLocationByCountryCode("AL", timelines=True)
al_confirmed = al[0]['timelines']['confirmed']['timeline']

af = covid19.getLocationByCountryCode("AF", timelines=True)
af_confirmed = af[0]['timelines']['confirmed']['timeline']

br = covid19.getLocationByCountryCode("BR", timelines=True)
br_confirmed = br[0]['timelines']['confirmed']['timeline']

dz = covid19.getLocationByCountryCode("DZ", timelines=True)
dz_confirmed = dz[0]['timelines']['confirmed']['timeline']

ad = covid19.getLocationByCountryCode("AD", timelines=True)
ad_confirmed = ad[0]['timelines']['confirmed']['timeline']

ag = covid19.getLocationByCountryCode("AG", timelines=True)
ag_confirmed = ag[0]['timelines']['confirmed']['timeline']

bb = covid19.getLocationByCountryCode("BB", timelines=True)
bb_confirmed = bb[0]['timelines']['confirmed']['timeline']

bo = covid19.getLocationByCountryCode("BO", timelines=True)
bo_confirmed = bo[0]['timelines']['confirmed']['timeline']

au = covid19.getLocationByCountryCode("AU", timelines=True)
au_confirmed = au[0]['timelines']['confirmed']['timeline']

#BROJ ZARAZENIH PO DRZAVAMA NA DANASNJI DAN!
dates = []
confirmed = []
confirmed_by_date = []
states_confirmed = []

previous = 0
for keys, values in ad_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
ad_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(ad_current)

confirmed_by_date = []
previous = 0
for keys, values in af_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
af_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(af_current)

confirmed_by_date = []
previous = 0
for keys, values in ag_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
ag_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(ag_current)

confirmed_by_date = []
previous = 0
for keys, values in al_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
al_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(al_current)

confirmed_by_date = []
previous = 0
for keys, values in au_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
au_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(au_current)

confirmed_by_date = []
previous = 0
for keys, values in bih_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
bih_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(bih_current)

confirmed_by_date = []
previous = 0
for keys, values in bb_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
bb_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(bb_current)

confirmed_by_date = []
previous = 0
for keys, values in bo_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
bo_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(bo_current)

confirmed_by_date = []
previous = 0
for keys, values in br_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
br_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(br_current)

confirmed_by_date = []
previous = 0
for keys, values in dz_confirmed.items():
    dates.append(keys)
    confirmed.append(values)
    confirmed_by_date.append(values-previous)
    previous = values
dz_current = confirmed_by_date[len(confirmed_by_date)-1]
states_confirmed.append(dz_current)

print(states_confirmed)
plt.bar(states,states_confirmed)
plt.xlabel('Drzave')
plt.ylabel('Broj potvrdjenih slucajeva na danasnji dan')
plt.show()
