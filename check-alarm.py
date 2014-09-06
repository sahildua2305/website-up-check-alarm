import requests # module for makign HTTP request to SPOJ website
import winsound # module for making beep like noise once website is up
from time import sleep # module for putting a desired delay to reduce load on computer system

count=0 # variable to keep track of number of times the website was checked after running the script
while(1):
    response = requests.get('http://spoj.com/') # making GET request to spoj.com website to know it's status
    count+=1
    if len(response.content) != 231: # since SPOJ website is down for maintenance, so HTTP request will not show any error code but it will return the content of the webpage. The length of webpage content when it's not UP is 231, that's what I used here.
        # 1st argument - frequency of the sound
        # 2nd argument - number of milliseconds that sound will be played
        winsound.Beep(200,5000)
        print "Number of times checked: "+str(count)
        break # stop sending GET requests once the website is up
    print "Number of times checked: "+str(count)
    sleep(10) # used to put delay of 10 seconds between 2 consecutive requests to spoj website
