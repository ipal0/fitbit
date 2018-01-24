#!/usr/bin/python3
""" This script collects all the 24 attributes of the hdf file fitbit.h5 and plot them. """
import h5py as h5
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f = h5.File('fitbit.h5', 'r')
Dates = [i for i in f['/HR']]  # find all the dates
A = [i for i in f['/HR/' + Dates[0]].attrs]  # find all the attributes
A.sort()
D = pd.DataFrame(columns=A)  # Create an empty dataframe
for i in Dates:
    try:
        d = {}
        for a in A:
            d.update({a: f['/HR/' + i].attrs[a]})
        D0 = pd.DataFrame(d, index=[pd.to_datetime(i[1:], format='%Y%m%d')])
        D = D.append(D0)
    except Exception as E:
        print(i, E)
f.close()
C = D.corr()
plt.figure(figsize=(20, 10))
plt.pcolormesh(C)
plt.colorbar()
plt.show(block=False)
print([i for i in enumerate(A)])
plt.figure(figsize=(20, 40))
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] * 3
cnt = 0
D = D.rolling(int(len(D) / 30)).mean()
for a in A:
    cnt += 1
    plt.subplot(8, 3, cnt)
    plt.plot(np.array(D[a]), color[(cnt - 1) % 7])
    plt.title(a, fontsize='large')
    if cnt < 22:
        plt.tick_params(labelbottom='off')
plt.show()
print("Date Range is from %s to %s" % (D.index[0].date(), D.index[-1].date()))
