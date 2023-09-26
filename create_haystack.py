#! usr/bin/env python
"""
This is a script to create a "Haystack" text file
The text file consists of "hay" ('X' characters)
And may/may not consist of "needles" ('|' characters)
____________
Input:
    --nrows (-n)  = number of rows in the haystack (int)
                    default = 100
    --nsites (-i) = number of sites per row in the haystack (int)
                    default = 100
    --prob (-p)   = probability of a character being a needle = 1/prob (int)
                    default = 99999
    
Output:
    haystack.txt = text file with haystack
____________
Example:
    python create_haystack.py
    python create_haystack.py -n 500
    python create_haystack.py -n 100 -i 1000 -p 99
"""

import sys
import random
import argparse

def make_hay_row(mhr_prob, mhr_len):
    row = []
    row_len = mhr_len
    for i in range(1,row_len):
        x = random.randrange(0,mhr_prob)
        if x >= (mhr_prob - 1):
            needle = "|"
        else:
            needle = "X"
        row.append(needle)
    return row

def make_haystack(mh_nrows, mh_nsites, mh_prob, mh_outfile):
    for i in range(1, mh_nrows + 1):
        row = make_hay_row(mh_prob, mh_nsites)
        mh_outfile.write("".join(row) + "\n")

def main(m_nrows, m_nsites, m_prob, m_outfile):
    make_haystack(m_nrows, m_nsites, m_prob, m_outfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nrows',
            type = int,
            default = 100,
            help = 'Number of rows in haystack.')
    parser.add_argument('-i', '--nsites',
            type = int,
            default = 100,
            help = 'Number of sites in each row.')
    parser.add_argument('-p', '--prob',
            type = int,
            default = 9999,
            help = 'Probability of a character being a needle is 1 / prob ')
    parser.add_argument('-o', '--outf',
            type = str,
            default = 'haystack.txt',
            help = 'outfile name.')
    args = parser.parse_args()
    print(args)
    with open(args.outf, "w") as outfile:
        main(args.nrows, args.nsites, args.prob, outfile)

