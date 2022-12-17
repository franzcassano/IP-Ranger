#!/usr/bin/python
# -- coding: utf-8 -

import os, time, random, sys
from colorama import Fore, init

BLUE = Fore.BLUE
RED = Fore.LIGHTRED_EX
CYAN = Fore.LIGHTCYAN_EX
WHITE = Fore.LIGHTWHITE_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
MAGENTA = Fore.LIGHTMAGENTA_EX

os.system("")
init(autoreset=True)

def scan(ips):
	try:
		ch = ips.split('\n')[0].split('.')
		in1 = ch[0]
		in2 = ch[1]
		in3 = ch[2]
		gat = f'{str(in1)}.{str(in2)}.{str(in3)}.'
		i = 0
		while i <= 255:
			i += 1
     		
			print(f'{RED}Ranging IP : {CYAN} {str(gat)}{GREEN}{str(i)}')
			f = open('ranged.txt', 'a', encoding='utf-8')
			f.write(f'{str(gat)}{str(i)}\n')
			f.close()
     
	except KeyboardInterrupt:
		sys.exit(f'{RED}\n\nShutdown Button Detected\nFinishing Program...!!!!\n')
	except PermissionError:
		if not os.path.isfile('ranged.txt'):
			raise
	else:
		pass

def main():
	color = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLUE]
	ban =  ('''    ________        ____                             
   /  _/ __ \      / __ \____ _____  ____ ____  _____
   / // /_/ /_____/ /_/ / __ `/ __ \/ __ `/ _ \/ ___/
 _/ // ____/_____/ _, _/ /_/ / / / / /_/ /  __/ /    
/___/_/         /_/ |_|\__,_/_/ /_/\__, /\___/_/     
                                  /____/             
IPS-Ranger By Franz Lennon Cassano
Contact For More Information.
Telegram: https://t.me/franzlc7
Whatsapp: https://wa.me/message/XCDZUUHYN6G5M1\n''')
	ran = random.choice(color)
	time.sleep(0.1)
	if(os.name == 'posix'):
		os.system('clear')
	else:
		os.system('cls')
	print(ran+ban)
	try:
		nam = open(input(f'{CYAN}List Ips  :'), 'r').read().splitlines()
		for ip in nam:
			scan(ip)
	except KeyboardInterrupt:
		sys.exit(f'{RED}\n\nShutdown Button Detected\nFinishing Program...!!!!\n')
	except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
		sys.exit(f'{RED}\n\nCheck Your Connection And Try Again\nShutdown Program...!!!!\n')
	except FileNotFoundError:
		print(f'{RED}Please Input Valid File!!!')
	else:
		pass
		
if __name__ == '__main__':
	main()