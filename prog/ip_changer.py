import argparse
from subprocess import getoutput
from json import load
from random import random
from time import sleep
from urllib.error import URLError
from urllib.request import urlopen
from _thread import start_new_thread

from stem import Signal
from stem.control import Controller
import requests
import socks
import socket


class Switcher:
    def __init__(self, host, port, password, time_interval):
        self.host = host
        self.port = port
        self.password = password
        self.time_interval = time_interval
        self.ident = random()

    def start(self):
        print("TOR Switcher starting.")
        start_new_thread(self.newnym, ())

    def newnym(self):
        key = self.ident
        try:
            with Controller.from_port(address=self.host, port=self.port) as controller:
                controller.authenticate(password=self.password)
                print("AUTHENTICATE accepted.")
                
                while key == self.ident:
                    controller.signal(Signal.NEWNYM)
                    print("Sent signal NEWNYM")

                    try:
                        my_new_ident = load(urlopen("https://check.torproject.org/api/ip"))["IP"]
                    except (URLError, ValueError):
                        my_new_ident = getoutput("wget -qO - ifconfig.me")

                    print(f"Your IP is {my_new_ident}")
                    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050) # 9050 is default TOR SOCKS
                    socket.socket = socks.socksocket
                    response = requests.get("https://check.torproject.org/api/ip")
                    print(f"Your IP through TOR is {response.text}") # Your IP adress through TOR network
                    sleep(self.time_interval)
        except Exception as e:
            print(f"There was an error here: {e}")
            import traceback
            traceback.print_exc()
            print("Quitting.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="TOR IP Switcher")
    parser.add_argument("--host", default="127.0.0.1", help="The host of the TOR service")
    parser.add_argument("--port", default=9051, type=int, help="The port number of the TOR service")
    parser.add_argument("--password", required=True, help="The password for the TOR service")
    parser.add_argument("--time", default=30.0, type=float, help="Time interval between IP switches")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    switcher = Switcher(args.host, args.port, args.password, args.time)
    switcher.start()
    input("Press Enter to exit...")

