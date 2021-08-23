import requests
import json
from json.decoder import JSONDecodeError

print(''' _             _____ _               _             
(_)           /  __ \ |             | |            
 _ _ __   ___ | /  \/ |__   ___  ___| | _____ _ __ 
| | '_ \ / _ \| |   | '_ \ / _ \/ __| |/ / _ \ '__|
| | |_) | (_) | \__/\ | | |  __/ (__|   <  __/ |   
|_| .__/ \___/ \____/_| |_|\___|\___|_|\_\___|_|   
  | |                                              
  |_|       By:Bikram Kharal(@7H3_M4RK18)           ''')
headers={
'Content-Type': 'application/json'}

id=int(input("Enter the company share id : "))
num=int(input("Enter how many ipo do you want to check : "))
for i in range(num):
    try:
        boid=input("Enter your boid number : ")
        data={"companyShareId":id,"boid":boid}
        response=requests.post('https://iporesult.cdsc.com.np/result/result/check',headers=headers,json=data)
        result=json.loads(response.text)
        if result["success"]==False:
            print(result["message"]+"="+boid)
        else:
            print(result["message"]+",BOID="+boid)

    except JSONDecodeError:
        print("Enter valid Boid Number")
    except KeyboardInterrupt:
        print("\nExiting..........")
        break
        

  
