#!/usr/bin/python3
""" This script gets the data from Fitbit Server. You need to login and get the code string from site - https://dev.fitbit.com/login """
import argparse
import urllib.request
from time import sleep
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument("-y", dest="Year", type=int,
                    help="Starting Year, Default=Current Year", default=datetime.now().year)
parser.add_argument("-m", dest="Month", type=int,
                    help="Starting Month, Default=Current Month", default=datetime.now().month)
parser.add_argument("-d", dest="Day", type=int,
                    help="Starting Day, Default=Yesterday", default=datetime.now().day - 1)
parser.add_argument("-nh", dest="Heart", help="No Heart Data if called",
                    default=True, action="store_false")
parser.add_argument("-na", dest="Activity",
                    help="No Activity Data if called", default=True, action="store_false")
parser.add_argument("-c", dest="Code", help="Code String for Header",
                    default='***Put your code string obtained from fitbit website***')
args = parser.parse_args()

header_key = 'Authorization'
header_value = 'Bearer ' + args.Code
st = datetime.date(datetime(args.Year, args.Month, args.Day))

while st < datetime.date(datetime.now()):
    date = st.strftime("%Y-%m-%d")
    if args.Heart:
        req = urllib.request.Request(
            'https://api.fitbit.com/1/user/-/activities/heart/date/%s/1d.json' % date)
        req.add_header(header_key, header_value)
        R = urllib.request.urlopen(req)
        open("HR_" + date + '.json', 'w').write(R.read().decode('utf8'))
        print("Recd Heart Data for %s" % date)
        sleep(1)
    if args.Activity:
        req = urllib.request.Request(
            'https://api.fitbit.com/1/user/-/activities/date/%s.json' % date)
        req.add_header(header_key, header_value)
        R = urllib.request.urlopen(req)
        open("AV_" + date + '.json', 'w').write(R.read().decode('utf8'))
        print("Recd Activity Data for %s" % date)
        sleep(1)
    st = st + timedelta(days=1)
