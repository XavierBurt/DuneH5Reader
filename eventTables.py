import pandas as pd

# import eventDisplay

import h5py

f = h5py.File('selftrigger_2022_08_05_05_06_01_PDT_evd.h5')

eventData = f['charge']['events']['data']

hitData = f['charge']['hits']['data']


def hitDataPerEvent(event):
    t0 = event['ts_start']
    tf = event['ts_end']

    eventMask = (hitData['ts'] >= t0) & (hitData['ts'] < tf)

    events = hitData[eventMask]

    px = events['px']
    py = events['py']
    ts = events['ts']
    q = events['q']
    data = {
        'x': px,
        'y': py,
        't': ts,
        'q': q
    }
    print(pd.DataFrame(data))


i = 0
for event in eventData:
    i = i + 1
    nHits = event['nhit']
    strr = "Hits: " + str(nHits)
    print(strr)
    hitDataPerEvent(event)
    input("Type any key for the next graph.")
