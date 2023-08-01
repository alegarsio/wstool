import os , socket , sys , colorama , requests , webbrowser , ipaddress , subprocess , datetime
from colorama import Back , Fore , Style
colorama.init(autoreset=True)
import http.server
user = socket.gethostname()
addr = socket.gethostbyname(user)
print(Fore.LIGHTCYAN_EX +  f"""          
                 __                 __            
__  _  __ ______/  |_  ____   ____ |  |   https://github.com/alegarsio/  
\ \/ \/ //  ___/   __\/ __ \ / __ \|  |   Address : {addr} OS : {sys.platform}
 \     / \___ \ |  | (  \_\ )  \_\ )  |__ 
  \/\_/ /____  \|__|  \____/ \____/|____/  
             \/                         

{Fore.LIGHTGREEN_EX}Usage : Python3 wstool.py | Package : [urllib3 , sys , requests , scapy , colorama]
"""f"\n{Fore.LIGHTRED_EX}Welcome to Wstool , type [-h] to help [enum , scrap , request]\n")
if sys.platform.startswith('win'.lower()) : print(f'{Back.LIGHTRED_EX} Some feuture may not available !')
else : pass
import colorama
from colorama import Back , Fore , Style
colorama.init(autoreset=True) 

def __wstoll__(def_command  , command_line , file_command):
    import socket , sys
    def_command = ["start",
                   "ch",
                   "scrap",
                   "request",
                   "enum",
                   "-h"]
    command_line = {def_command[0] : "http [required] , addr [required] , port [required]",
                    def_command[1] : "network address [requiered], network/subnet [requiered]",
                    def_command[2] : "host [required] , as/none [required] , file name [required]",
                    def_command[3] : "host [required]",
                    def_command[4] : "host [required]",
                    }
    if sys.argv[1].startswith('-h') :
        file = open('help.txt','r')
        print(file.read())
    # sys handle Error
    if (sys.argv[1] not in def_command ) : print(f"Error syntax {sys.argv[1]}")
    # file setting only for windows user
    if sys.argv[1].startswith(def_command[1]): 
        import scapy.all as scapy
        import re , sys , colorama 
        from colorama import Fore
        colorama.init(autoreset= True)
        ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
        while True:
            ip_s = sys.argv[2]
            ip_s = sys.argv[3]
            if ip_add_range_pattern.search(ip_s):
                print(Fore.LIGHTGREEN_EX + f'{ip_s} is valid')
                break
        scapy.arping(ip_s)
    # function starts
    if sys.argv[1].startswith(def_command[0]): 
        usage = ["http","a"]
        if sys.argv[2].startswith(usage[0]):
            try:
                addr = sys.argv[3]
                port = sys.argv[4]
                if addr.startswith(usage[1]):
                    addr = socket.gethostbyname(socket.gethostname())
                elif port.startswith(usage[1]) : 
                    port = "9000"
                os.system(f'python -m http.server {port} -b {addr}')
            except IndexError:print(command_line.get(def_command[0]))
    elif sys.argv[1].startswith(def_command[2]):
        save_as = ["as","none"]
        try:
            req = requests.get(sys.argv[2])
            html = req.text
            print(html)
            if sys.argv[3].startswith(save_as[0].lower()):
                file = open(sys.argv[4],'w')
                file.write(html)
        except IndexError:print(command_line.get(def_command[2].lower()))
        except UnicodeEncodeError: print(F'Can not collect info')
    elif sys.argv[1].startswith(def_command[3]):
        import urllib3 as oreon 
        import colorama
        from colorama import Back
        colorama.init(autoreset=True)
        https_site = sys.argv[2]
        try:
            url = f'{https_site}'
            http = oreon.PoolManager()
            response = http.request("GET",url)
            r = response.status
            print(f'status code {response.status}')
            data = response.data
            print(f'data length : {len(data)}')
        except ConnectionError: print('Connection offline')
        except IndexError: print(command_line.get(def_command[3]))
    elif sys.argv[1].startswith(def_command[4]):
        import dns.resolver
        record_types = ["A","AAAA","NS","CNAME","MX","PTR","SOA","TXT"]
        domain = sys.argv[2]
        for records in record_types:
            try:
                answer = dns.resolver.resolve(domain , records)
                print(f'\n {records} Record')
                print(f'-'*30)
                for server in answer:
                    print(server.to_text())
            except dns.resolver.NoAnswer:pass
            except dns.resolver.LifetimeTimeout: print('Time out [Error]')
            except dns.resolver.NXDOMAIN : print('Invalid host/website [CTRL + C] to stop')
            except IndexError:print(command_line.get(def_command[4]))
try:    
    __wstoll__('def_command','command_line','file_command')
except KeyboardInterrupt: pass 
except IndexError : pass 
except ModuleNotFoundError : 
    os.system('pip install urllib3')
    os.system('pip install sys')
    os.system('pip install colorama')
    os.system('pip install requests')
