#!/usr/bin/python3
""" This script saves the json files to HDF5 database file named fitbit.h5 """
from glob import glob
import json
import numpy as np
import h5py as h5

FileList = glob('HR*.json')
FileList.sort()
f = h5.File('fitbit.h5')
for File in FileList:
    F = json.load(open(File))
    Date = F['activities-heart'][0]['dateTime']
    Date = ''.join(Date.split('-'))
    a = F['activities-heart-intraday']['dataset']
    l = []
    for i in range(len(a)):
        time = ':'.join(a[i]['time'].split(':')[:-1])
        l.append((time, a[i]['value']))
    A = np.array(l, dtype=[('time', 'S5'), ('bpm', 'i2')])
    D = f.create_dataset('HR/D' + Date, A.shape, data=A)
# add attrs
    F = json.load(open(File.replace('HR', 'AV')))
    try:
        D.attrs['RestingHeartRate'] = F['summary']['restingHeartRate']
    except Exception: print("Resting Heart Rate for %s is not found" %Date)
    D.attrs['CaloriesBMR'] = F['summary']['caloriesBMR']
    D.attrs['CaloriesOut'] = F['summary']['caloriesOut']
    D.attrs['CaloriesActivity'] = F['summary']['activityCalories']
    D.attrs['ActiveVeryMins'] = F['summary']['veryActiveMinutes']
    D.attrs['ActiveFairlyMins'] = F['summary']['fairlyActiveMinutes']
    D.attrs['ActiveLightlyHrs'] = round(
        F['summary']['lightlyActiveMinutes'] / 60, 3)
    D.attrs['Elevation'] = F['summary']['elevation']
    D.attrs['Floors'] = F['summary']['floors']
    D.attrs['Steps'] = F['summary']['steps']
    D.attrs['Distance'] = F['summary']['distances'][0]['distance']
    D.attrs['SedentaryHrs'] = round(F['summary']['sedentaryMinutes'] / 60, 3)
    D.attrs['ZoneRestHrs'] = round(
        F['summary']['heartRateZones'][0]['minutes'] / 60, 3)
    D.attrs['ZoneFatburnHrs'] = round(
        F['summary']['heartRateZones'][1]['minutes'] / 60, 3)
    D.attrs['ZoneCardioMins'] = F['summary']['heartRateZones'][2]['minutes']
    D.attrs['ZonePeakMins'] = F['summary']['heartRateZones'][3]['minutes']
    D.attrs['ZoneRestCals'] = F['summary']['heartRateZones'][0]['caloriesOut']
    D.attrs['ZoneFatburnCals'] = F['summary']['heartRateZones'][1]['caloriesOut']
    D.attrs['ZoneCardioCals'] = F['summary']['heartRateZones'][2]['caloriesOut']
    D.attrs['ZonePeakCals'] = F['summary']['heartRateZones'][3]['caloriesOut']
    D.attrs['_BPM_Min'] = D['bpm'].min()
    D.attrs['_BPM_Mean'] = round(D['bpm'].mean(), 3)
    D.attrs['_BPM_Max'] = D['bpm'].max()
    D.attrs['_BPM_Std'] = round(D['bpm'].std(), 3)
f.close()
