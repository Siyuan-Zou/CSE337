import csv
import time
import math

#Part 1
price_dict = {}

with open("prices_sample.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        t1 = time.gmtime(int(row[0]))
        t1_converted = time.strftime('%Y-%m-%d %H:%M:%S', t1)
        date_str = t1_converted.split(" ")[0]
        if date_str in price_dict:
            price_dict[date_str].append(row[1])
        else:
            price_dict.setdefault(date_str, []).append(row[1])

f = open("price_file.txt", "w")
for key in price_dict:
    f.write(key +": "+ ','.join(price_dict.get(key))+'\n')
f.close()

#Part 2
vdict = {}
f = open("price_file.txt")
for line in f:
    lst = line.split(": ")
    lst2 = lst[1].split('\n')
    lst3 = lst2[0].split(',')
    lst4 = list(map(int, lst3))
    vdict.setdefault(lst[0], []).extend(lst4)

value = list()
for key in vdict:
    value.extend(vdict.get(key))

value.sort()
q1 = value[math.ceil(len(value)*0.25)-1]
q2 = value[math.ceil(len(value)*0.50)-1]
q3 = value[math.ceil(len(value)*0.75)-1]
print('25th percentile:', q1)
print('50th percentile:', q2)
print('75th percentile:', q3)

mean = sum(value)/len(value)
i = 0
var_sum = 0.0
while i<len(value):
    var_sum += math.pow(value[i]-mean, 2)
    i += 1
variance = var_sum/len(value)
print("Variance:", variance)


for x in range(0,5):

    farthest_abs = -1
    farthest_value = 0
    for key in list(vdict):
        i = 0
        while i < len(vdict[key]):
            if math.fabs(vdict[key][i] - mean) > farthest_abs:
                farthest_abs = math.fabs(vdict[key][i] - mean)
                farthest_value = vdict[key][i]
            i += 1

    date_of_farthest_value = ''
    for key in list(vdict):
        for ele in vdict[key]:
            if ele == farthest_value:
                date_of_farthest_value = key
                vdict.pop(date_of_farthest_value, None)
                continue

    print("Farthest", x+1, "-", date_of_farthest_value + ":", farthest_value)
