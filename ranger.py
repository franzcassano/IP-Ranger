#!/usr/bin/python
# -- coding: utf-8 -

from colorama import Fore, init

wh = Fore.WHITE
gr = Fore.LIGHTGREEN_EX
re = Fore.LIGHTRED_EX
cy = Fore.LIGHTCYAN_EX


def  scan(ips):
    try:
     ur = ips.rstrip()
     ch = ips.split('\n')[0].split('.')
     in1 = ch[0]
     in2 = ch[1]
     in3 = ch[2]
     gat = str(in1) + '.' + str(in2) + '.' +str(in3) + '.'
     i = -1
     while i <= 254:
         i += 1
         
         print(re + "Ranging IP : " + cy +str(gat) + gr + str(i))
         open('ranged.txt', 'a').write(str(gat) + str(i) + '\n')
         
    except:
    	pass

nam = input(cy + 'List Ips  :')
with open(nam) as f:
    for ips in f:
        scan(ips)