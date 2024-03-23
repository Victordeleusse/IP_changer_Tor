# IP_changer_Tor
Program for changing IP addresses at desired intervals using the TOR network.

## Set-up

1. Install Tor
2. Start the service ```(brew) service tor (re)start```
3. Run the command ```tor --hash-password "YOUR_PASSWORD"``` to generate your proper service password. By default : ```--host 127.0.0.1``` ```--port 9051``` ```--time 30```
4. Modify your Tor config. file **/tor/torrc**
	- uncomment **Control Port 9051**
	- uncomment and modify **HashedControlPassword**

## Run

* Start running **toripatables.py** to route all services and traffic including DNS through the tor network.

* Get into *mon_env* by running **source mon_env/bin/activate** and ensure that **stem** package is well installed. Then run **ip_changer.py**
