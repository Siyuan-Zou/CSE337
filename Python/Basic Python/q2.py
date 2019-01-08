import time
import csv

price_dict = {}

with open("prices_sample.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        t1 = time.gmtime(int(row[0]))
        t1_converted = time.strftime('%w, %Y-%m-%d', t1)
        if int(t1_converted[0]) == 0:
            offset = 518400
        else:
            offset = int(t1_converted[0])*24*3600 - 86400
        t2 = time.gmtime(int(row[0])-offset)
        t2_converted = time.strftime('%Y-%m-%d', t2)

        if t2_converted in price_dict:
            price_dict[t2_converted].append(row[1])
        else:
            price_dict.setdefault(t2_converted, []).append(row[1])

computatedlst = list()
for key in price_dict:
    average = 0
    max = int(price_dict[key][0])
    min = int(price_dict[key][0])
    for ele in price_dict[key]:
        if int(ele)>max:
            max = int(ele)
        if int(ele)<min:
            min = int(ele)
        average += int(ele)
    average = average/len(price_dict[key])
    lst = list()
    lst.append(key)
    lst.append(max)
    lst.append(min)
    lst.append(average)
    computatedlst.append(lst)

with open("q2_weekly.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(computatedlst)