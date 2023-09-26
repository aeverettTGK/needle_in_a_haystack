#! /usr/bin/env python

import sys
import matplotlib.pyplot as plt

needles = {}

with open(sys.argv[1], "r") as infile:
    needle_count = 0
    line_num = 0
    for line in infile:
        line_num = line_num + 1
        needle_check = line.find("|")
        if needle_check != -1:
            sites = [sites for sites, char in enumerate(line) if char == "|"]
            for site in sites:
                key = str(site) + "," + str(line_num)
                needles[key] = [site, line_num]
            needle_count = needle_count + len(sites)
    print("total needles: " + str(needle_count))
    print("needles: " + str(needles))

x = []
y = []
for key in needles:
    x.append(needles[key][0])
    y.append(needles[key][1])
print("keys: " + str(x) + ", len: " + str(len(x)))
print("values: " + str(y) + ", len: " + str(len(y)))

plt.hist(y, bins=50)
plt.savefig("hist.pdf", format="pdf")
plt.close()
            
plt.scatter(x, y)
ax = plt.gca()
ax.invert_yaxis()
plt.savefig("scatter.pdf", format="pdf")
plt.close()


            

