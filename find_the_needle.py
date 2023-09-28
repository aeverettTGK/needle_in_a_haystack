# usr/bin/env python

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def find_the_needle(haystack):
    needle_present = False
    needle_count = 0
    needle_places = []
    with open(haystack, "r") as hayfile:
        line_number = 1
        for line in hayfile:
            column_number = 1
            for char in line:
                if char == "|":
                    needle_present = True
                    needle_count += 1
                    position = (line_number, column_number)
                    needle_places.append(position)
                column_number += 1
            line_number += 1
    print(needle_present)
    print("{} needles found in the haystack!".format(needle_count))
    return needle_places

def plot_needles(needle_places):
    x = []
    y = []
    for needle in needle_places:
        x.append(needle[0])
        y.append(needle[1])
    plt.scatter(x,y)
    plt.xlabel("Line")
    plt.ylabel("Column")
    plt.savefig("needles_in_haystack.png")

if __name__=="__main__":
    haystack = sys.argv[1]
    needle_places = find_the_needle(haystack)
    plot_needles(needle_places)
