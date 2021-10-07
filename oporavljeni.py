import COVID19Py
import matplotlib.pyplot as plt

covid19 = COVID19Py.COVID19()

states = ['AD', 'AF', 'AG', 'AL' , 'AU', 'BA', 'BB', 'BO', 'BR', 'DZ']

bih = covid19.getLocationByCountryCode("BA", timelines=True)
bih_recovered = bih[0]['timelines']['recovered']['timeline']

al = covid19.getLocationByCountryCode("AL", timelines=True)
al_recovered = al[0]['timelines']['recovered']['timeline']

af = covid19.getLocationByCountryCode("AF", timelines=True)
af_recovered = af[0]['timelines']['recovered']['timeline']

br = covid19.getLocationByCountryCode("BR", timelines=True)
br_recovered = br[0]['timelines']['recovered']['timeline']

dz = covid19.getLocationByCountryCode("DZ", timelines=True)
dz_recovered = dz[0]['timelines']['recovered']['timeline']

ad = covid19.getLocationByCountryCode("AD", timelines=True)
ad_recovered = ad[0]['timelines']['recovered']['timeline']

ag = covid19.getLocationByCountryCode("AG", timelines=True)
ag_recovered = ag[0]['timelines']['recovered']['timeline']

bb = covid19.getLocationByCountryCode("BB", timelines=True)
bb_recovered = bb[0]['timelines']['recovered']['timeline']

bo = covid19.getLocationByCountryCode("BO", timelines=True)
bo_recovered = bo[0]['timelines']['recovered']['timeline']

au = covid19.getLocationByCountryCode("AU", timelines=True)
au_recovered = au[0]['timelines']['recovered']['timeline']

#BROJ OPORAVLJENIH PO DRZAVAMA NA DANASNJI DAN!
dates = []
recovered = []
recovered_by_date = []
states_recovered = []

previous = 0
for keys, values in ad_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
ad_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(ad_current)

recovered_by_date = []
previous = 0
for keys, values in af_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
af_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(af_current)

recovered_by_date = []
previous = 0
for keys, values in ag_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
ag_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(ag_current)

recovered_by_date = []
previous = 0
for keys, values in al_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
al_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(al_current)

recovered_by_date = []
previous = 0
for keys, values in au_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
au_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(au_current)

recovered_by_date = []
previous = 0
for keys, values in bih_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
bih_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(bih_current)

recovered_by_date = []
previous = 0
for keys, values in bb_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
bb_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(bb_current)

recovered_by_date = []
previous = 0
for keys, values in bo_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
bo_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(bo_current)


recovered_by_date = []
previous = 0
for keys, values in br_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
br_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(br_current)

recovered_by_date = []
previous = 0
for keys, values in dz_recovered.items():
    dates.append(keys)
    recovered.append(values)
    recovered_by_date.append(values-previous)
    previous = values
dz_current = recovered_by_date[len(recovered_by_date)-1]
states_recovered.append(dz_current)


plt.bar(states,states_recovered)
plt.xlabel('Drzave')
plt.ylabel('Broj oporavljenih slucajeva na danasnji dan')
plt.show()