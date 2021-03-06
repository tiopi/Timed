import requests, json, re
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt
% matplotlib inline

airport = "ATL"
j = requests.get('https://demo30-test.apigee.net/v1/hack/tsa?airport='+ airport+'&apikey=wc7Tmyx7JGCAMPiPtrE01U8LAzSJXTb7')
mjason = json.loads(j.text)

ar = [str(i['waitTime'])for i in mjason['WaitTimeResult']]
dates = [str(i['createdDatetime'])for i in mjason['WaitTimeResult']]
dates1 = [j.split('/')[1:] for j in dates]
a1 = []
for i in range(len(dates1)):
    c = [int(s) for s in re.findall(r'\d+', dates1[i][1])]
    # for dates int(dates1[i][0]) instead of 0
    a1.append(0 + (c[1] if dates1[i][1][len(dates1[i][1])-2:] != "PM" else c[1] + 12)/float(24))

a = []
times_per_day = defaultdict(int)
for j in ar:
    b = [int(s) for s in re.findall(r'\d+', j)]
    a.append(b[1 if len(b)>1 else 0])
for j in range(len(a)):
    times_per_day[a1[j]] += a[j]


fit = np.polyfit(a1,a,1)
fit_fn = np.poly1d(fit)

fit_fn(input())