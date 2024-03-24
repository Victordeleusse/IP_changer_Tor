# IP_changer_Tor
Program for changing IP addresses at desired intervals using the TOR network.

The HTTP requests made to check the IP address are routed through Tor, thanks to the configuration of PySocks and requests to use Tor's SOCKS proxy. This anonymizes these requests, and the IP address reported by check.torproject.org corresponds to that of a Tor exit node, which changes when you send the NEWNYM signal through Tor's ControlPort.

	- Usage of PySocks and SOCKS Proxy Configuration: socks.set_default_proxy() and socket.socket = socks.socksocket globally configure Python sockets to use Tor as a SOCKS proxy. This is essential for ensuring your outgoing requests pass through Tor.

	- Usage of requests after PySocks Configuration: Importing and using requests after configuring the SOCKS proxy ensures that HTTP requests made via requests are routed through Tor, thereby altering the external visible IP address.

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
