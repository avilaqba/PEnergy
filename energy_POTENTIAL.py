# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 14:25:30 2018

@author: Asus
"""
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""
datalist = []

for i in range(51,501):
    datalist.append('loop_%d.out'%i)

for data in datalist:
    log = open(data)
    lines = log.readlines()
#print lines[0]
"""


log = open('loop_51.out')
lines = log.readlines()
dVAVGlist = []
POTENTIALlist = []
DIHEDlist = []
STEPdate =[]
STEPlist = []
for index, line in enumerate (lines, start = 1):
    
    if line.startswith('ACCELERATED') is True:
        
        DATA = line.split()
        
        dVAVGlist.append(float(DATA[7]))
        DIHEDlist.append(float(DATA[13]))
        POTENTIALlist.append(float(DATA[-1]))
        STEPdate.append(datetime.fromtimestamp(float(DATA[3])))

df = pd.DataFrame(
        {'STEP' : STEPdate,
         'dVAVG' :  dVAVGlist,
         'DIHED' : DIHEDlist,
         'POTENTIAL': POTENTIALlist
                })
                              

df = df.set_index('STEP')
mdf = df.resample('500S').mean()

# each timestep is 2fs so;
#FirstTime = 50*2*1000000 = 10^8 fs = 100 ns

Slist = []
#      It will be 900001 for total data!
for m in range(2001):
    Slist.append(100 + 0.001*m)

#lst = np.arange(len(Slist))

mdf['INDEX'] = pd.Series(Slist, index=mdf.index)

plt.scatter(mdf.INDEX, mdf.POTENTIAL, s = 200)
plt.xticks(fontsize = 50)
plt.yticks(fontsize = 50)
plt.xlabel('Time (ns)', fontsize = 50)
plt.ylabel('POTENTIAL')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(80, 60)
plt.savefig("energy_POTENTIAL.png", dpi=100)
