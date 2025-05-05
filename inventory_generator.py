#!/usr/bin/python3

import csv

with open('working_vco.csv') as vco_list:
    read_all_vco = csv.reader(vco_list)
    next(read_all_vco)
    for row in read_all_vco:
        print(f'{row[0].replace(" ","_").lower()} ansible_host={row[5]} ansible_port=44222 description="{row[3]}"')
