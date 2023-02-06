import datetime 
import time

end_time=datetime.datetime(2023,1,8) # till which date site should be blocked
site_block=["https://www.udemy.com/","https://www.facebook.com/"] #sites which you want to block
host_path="C:/Windows/System32/drivers/etc/hosts" #host address
redirect="127.0.0.1" #local host ip address

while True:
    if datetime.datetime.now()<end_time:
        print("Start Blocking")
        with open(host_path,"r+") as host_file:
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect+" "+website+"\n")
                else:
                    pass    
             #we are using file handling
    else:
        
        with open(host_path,"r+") as host_file:
            content=host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
                    
            host_file.truncate()  
        time.sleep(5)          
                    
        
    
    