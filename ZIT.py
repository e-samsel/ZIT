import socket
import time
import pyautogui

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file_ports=open("ports.txt", "r")
temp = file_ports.read().splitlines()
target = input('Podaj adres hosta, który chcesz skanować: ')

target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

def port_scan(port):
	try:
		s.connect((target_ip, port))
		return True
	except:
		return False

def scanning():
    for ports in temp:
        if port_scan(int(ports)):
            pyautogui.alert("Port "+ports+" jest otwarty",title="Alert Bezpieczeństwa")
        
while True:
    scanning()          
    time.sleep(10)

#sprawdzanie formatu adresu 
#zrobic cos zeby dzialal kilkukrotnie