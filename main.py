import subprocess
import os

# Directory where the OpenVPN configuration files are stored
config_dir = "/path/to/ovpn/files"

# Available countries and their corresponding ovpn files
vpn_servers = {
    "USA": "usa.ovpn",
    "UK": "uk.ovpn",
    "Germany": "germany.ovpn",
    "Turkey": "turkey.ovpn"
}

def connect_vpn(country):
    if country in vpn_servers:
        config_file = os.path.join(config_dir, vpn_servers[country])
        try:
            # Start the OpenVPN connection
            subprocess.run(["sudo", "openvpn", "--config", config_file])
        except Exception as e:
            print(f"Failed to connect to VPN: {e}")
    else:
        print(f"No VPN server found for {country}.")

def main():
    print("Select the country you want to connect to:")
    for country in vpn_servers:
        print(f"- {country}")
    
    selected_country = input("Country: ").strip()
    connect_vpn(selected_country)

if __name__ == "__main__":
    main()
