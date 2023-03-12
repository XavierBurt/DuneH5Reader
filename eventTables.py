import pandas as pd

# import eventDisplay

import h5py

f = h5py.File('selftrigger_2022_08_05_05_06_01_PDT_evd.h5')

eventData = f['charge']['events']['data']

hitData = f['charge']['hits']['data']


def hit_data_per_event(evt):
    t0 = evt['ts_start']  # Grab the start and end of the event
    tf = evt['ts_end']

    event_mask = (hitData['ts'] >= t0) & (hitData['ts'] < tf)  # use bitwise and to select only hit data
    # for this specific event's timeframe. (an array of all the times)

    events = hitData[event_mask]  # get the data for each entry given the 'ts' values.
    # (an array of all the events)

    px = events['px']  # get the x and y
    py = events['py']
    ts = events['ts']  # Potentially redundant, but the eventDisplay did this.
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
    hit_data_per_event(event)
    input("Type any key for the next graph.")
