import os
import requests

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def resolve_cfx_re_join(cfx_code):
    if "cfx.re/join/" not in cfx_code:
        print("Invalid cfx.re/join link format. Please provide a valid link.")
        return
    
    server_code = cfx_code.split("/")[-1]
    
        try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        response = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{server_code}", headers=headers)
        
        if response.status_code == 200:
            server_data = response.json()
            if 'error' in server_data:
                print(f"Error: {server_data['error']}")
            else:
                server_hostname = server_data['Data']['hostname']
                server_owner = server_data['Data']['ownerName']
                server_ip = server_data['Data']['connectEndPoints'][0]
                server_port = server_ip.split(":")[-1]
                server_ip = server_ip.split(":")[0]
                server_players = server_data['Data']['clients']
                
                print("\nServer Information:")
                print(f"  Name:    {server_hostname}")
                print(f"  Owner:   {server_owner}")
                print(f"  IP:      {server_ip}")
                print(f"  Port:    {server_port}")
                print(f"  Players: {server_players}")
        else:
            print(f"Failed to fetch data from FiveM API. Status code: {response.status_code}")
    
    except requests.RequestException as e:
        print(f"Error making request to FiveM API: {str(e)}")

def main():
    clear_screen()
    print("Enter the cfx.re/join link to resolve:")
    cfx_link = input("> ").strip()
    resolve_cfx_re_join(cfx_link)

if __name__ == "__main__":
    main()
