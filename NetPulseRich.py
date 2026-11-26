#!/usr/bin/env python3
import os
import subprocess
import time
import webbrowser

def clear_screen():
    os.system("clear || cls")

def NetPulse_Main():
    while True:
        clear_screen()
        print("=" * 40)
        print("               NetPulse")
        print("=" * 40)
        print("1. Check the internet connection's menu")
        print("2. Check the ports menu")
        print("3. Nmap usage mode (nmap)")
        print("4. Exit NetPulse")
        
        print("\n5. Open mraz0tix's site")

        main_choice = input("\nSelect a menu option (1-5): > ")
         
        if main_choice == "1":
            Internet_menu()
        elif main_choice == "2":
            Ports_menu()
        elif main_choice == "3":
            nmap_mode()
        elif main_choice == "4":
            print("\n[+] Bye Bye!")
            break
        
        elif main_choice == "5":
            Site()
        
        else:
            print("\nNetPulse >> [!] Invalid choice. Please try again.")
            input("\nNetPulse >> Press Enter to continue...")

def Internet_menu():       
    while True:
        clear_screen()
        print("=" * 40)
        print("              Internet Menu")
        print("=" * 40)
        print("1. Run ping test (8.8.8.8)")
        print("2. Ping custom website or IP")  
        print("3. Back to main menu")
        print("0. Connect via ssh (Security Shell)")

        choice_internet = input("\nSelect a menu option (0-3): > ")  

        if choice_internet == "1":
            Internet_check_default()  
        elif choice_internet == "2":
            Internet_check_custom()   
        elif choice_internet == "3":
            break
        elif choice_internet == "0":
            conection_via_ssh()
        else:
            print("\nNetPulse >> [!] Invalid choice. Please try again.")
            input("\nNetPulse >> Press Enter to continue...")

def conection_via_ssh():
    while True:
        clear_screen()
        print("=" * 40)
        print("              SSH Conection menu")
        print("=" * 40)
        print("1. Connect with ip adress")
        print("2. Back to main menu")  

        choice_internet = input("\nSelect a menu option (1-2): > ")  
   
        if choice_internet == "1":
            SSH_conection()   
        elif choice_internet == "2":
            break
        else:
            print("\nNetPulse >> [!] Invalid choice. Please try again.")
            input("\nNetPulse >> Press Enter to continue...")

def SSH_conection():
    name = input("\nEnter username on system > ")
    target = input("\nEnter IP of server > ")
    if target:
        time.sleep(0.5)
        try:
            subprocess.run(["kitty", "--hold", "ssh", f"{name}@{target}"], check=True)
        except FileNotFoundError:
            print("\nNetPulse >> [!] Error: 'kitty' terminal is not installed.")
    else:
        print("\nNetPulse >> [!] Error: Empty ip or username.")
    input("\nNetPulse >> Press Enter to continue...")

def Internet_check_default():
    print("\nNetPulse >> [+] Okay! Already checking connection...")
    time.sleep(0.5)
    try:
        subprocess.run(["kitty", "--hold", "ping", "-c", "3", "8.8.8.8"], check=True)
        print("[+] Internet connection checked successfully!")
    except FileNotFoundError:
        print("\nNetPulse >> [!] Error: 'kitty' terminal is not installed.")
    input("\nNetPulse >> Press Enter to continue...")

def Internet_check_custom():
    target = input("\nEnter website or IP to ping (e.g., google.com): > ")
    if target: 
        print(f"\nNetPulse >> [+] Pinging {target}...")
        time.sleep(0.5)
        try:
            subprocess.run(["kitty", "--hold", "ping", "-c", "4", target], check=True)
            print("\nNetPulse >> [+] Ping completed successfully!")
        except FileNotFoundError:
            print("\nNetPulse >> [!] Error: 'kitty' terminal is not installed.")
    else:
        print("\nNetPulse >> [!] Error: Empty target.")
    input("\nNetPulse >> Press Enter to continue...")

def Ports_menu():
    while True:
        clear_screen()
        print("=" * 40)
        print("             Menu for ports")
        print("=" * 40)
        print("1. Check your open ports (ss)")
        print("2. Back to main menu")

        main_choice_ports = input("\nSelect a menu option (1-2): > ")
        
        if main_choice_ports == "1":
            print("\nNetPulse >> [+] Okay! Already checking ports...")
            time.sleep(0.5)
            try:
                subprocess.run(["kitty", "--hold", "ss", "-tuln"], check=True)
                print("NetPulse >> [+] Ports checked successfully!")
            except FileNotFoundError:
                print("\nNetPulse >> [!] Error: 'kitty' terminal is not installed.")
            input("\nNetPulse >> Press Enter to continue...")
        elif main_choice_ports == "2":
            break
        else:
            print("\nNetPulse >> [!] Invalid choice. Please try again.")
            input("\nNetPulse >> Press Enter to continue...")

def nmap_mode():
    while True:
        clear_screen()
        print("=" * 40)
        print("            Nmap mode-menu")
        print("=" * 40)
        print("1. View your subnet (Scan custom target)")
        print("0. Back to main menu")

        nmap_choice = input("\nSelect a menu option (0-1): > ")

        if nmap_choice == "1":
            subnet = input("\nEnter target subnet (Default: 192.168.1.0/24): > ")
            if not subnet:
                subnet = "192.168.1.0/24"

            print(f"\n[+] Okay, checking subnet {subnet} via Nmap...")
            
            cmd = ["kitty", "--hold", "sudo", "nmap", "-sS", "-sV", "-O", subnet]
            
            try:
                subprocess.run(cmd, check=True)
            except FileNotFoundError:
                print("\nNetPulse >> [!] Error: 'kitty' terminal emulator or 'nmap' is not installed.")
                input("\nNetPulse >> Press Enter to continue...")
            except subprocess.CalledProcessError:
                print("\nNetPulse >> [!] Scan was interrupted or failed (maybe wrong sudo password?).")
                input("\nNetPulse >> Press Enter to continue...")
                
        elif nmap_choice == "0":
            break
        else:
            print("\nNetPulse >> [!] Invalid choice. Please try again.")
            input("\nNetPulse >> Press Enter to continue...")



def Site():
    print("NetPulse >> Okay!")
    webbrowser.open("https://mraz0tix-code.github.io/")
    input("\nNetPulse >> Press Enter to continue...")
    clear_screen()

if __name__ == "__main__":
    NetPulse_Main()
