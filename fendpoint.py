import sys
import requests
import re
import argparse

class TextColors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

endpoint_url = []
endpoint_dir = []
endpoint_const = []
pattern = r"^[a-zA-Z0-9_/:&?%.\-=\+!@$#^*_]*$"

def parse_endpoint(file_path):
    try:
        with open(file_path, 'r') as f:
            for l_no, line in enumerate(f, start=1):
                words = line.strip().split('"')
                #print(f"Words: {words}")
                for i in words:
                    if re.match(pattern, i):
                        if i.startswith("/") or i.startswith("./"):
                            if i not in endpoint_dir:
                                endpoint_dir.append(i)
                        if i.startswith("https://") or i.startswith("http://"):
                            if i not in endpoint_url:
                                endpoint_url.append(i)
        if endpoint_url:
           print("\n" + TextColors.BLUE +  "--- URL endpoints ---" + TextColors.RESET)
        for url in endpoint_url:
                try:
                    r = requests.get(url)
                    if r.status_code == 200:
                        print(f"{url}    Status code: " + TextColors.GREEN + "200 OK" + TextColors.RESET)
                    else:
                        print (f"{url}   Status code: " + TextColors.RED + f"{r.status_code}" + TextColors.RESET)
                except:
                    continue
        if endpoint_dir:
            print("\n" + TextColors.BLUE + "--- Application endpoints ---" + TextColors.RESET)
        for directory in endpoint_dir:
                print(f"{directory}")
    except:
        print("error")

        
def main():
    banner()
    parser = argparse.ArgumentParser(
                    prog='python3 fendpoint.py [options]',
                    description='Endpoint finder',
                    epilog='pamoutaf')
    parser.add_argument('-f', '--file', help="Add the target file to be scanned", required=True)
    args = parser.parse_args()

    if args.file:
        parse_endpoint(args.file)
def banner():
    banner = r"""
   __             _           _     _   
  / _|___ _ _  __| |_ __  ___(_)_ _| |_ 
 |  _/ -_) ' \/ _` | '_ \/ _ \ | ' \  _|
 |_| \___|_||_\__,_| .__/\___/_|_||_\__|
                   |_|                                                             
 by pamoutaf"""
    
    print(banner)   
    print("\n")

if __name__ == "__main__":
    main()
#parse_endpoint("/home/kali/fendpoint/text.txt")

