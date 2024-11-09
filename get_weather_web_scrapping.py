import requests 
from bs4 import BeautifulSoup
from datetime import datetime
import pync


#get the current time
c_time = datetime.now()
curr_time_parse = c_time.strftime('%H:%M:%S')


#To get the weather
def getWeather(url):
  req = requests.get(url)
  if req.status_code ==200:
    print("Find it !")
  return req.text


curr_weather = getWeather("https://weather.com/fr-FR/temps/aujour/l/d2a540efb4e9604b3c1d01b7851a1d9d2ab4c7b3ba428e5799936ac54404c035")
soup = BeautifulSoup(curr_weather , 'html.parser')  #give the html webpage and parser it


#find the weather using webscrapping in span where the value is store
morning_indication= soup.find("span",
                             dir="ltr").contents
aternoon_indication = soup.find_all("span",
                                    dir="ltr")[1].contents
evening_indication = soup.find_all("span", 
                                   dir="ltr")[2].contents

morning_temp = (str(morning_indication))
aternoon_temp = (str(aternoon_indication))
evening_temp = (str(evening_indication))



morning_temp_str = f'This morning the temperature is : {morning_temp[2:4]}°C '
afternoon_temp_str = f'This afternoon the temperature is : {aternoon_temp[2:4]}°C 🌥️'
evening_temp_str = f'This evening the temperature is : {evening_temp[2:4]}°C ☁️'



#Notification package for macOs 
def displayMorningTemp():
  pync.notify(morning_temp_str , title="Morning weather 🌅")

def displayAfterNoonTemp():
  pync.notify(afternoon_temp_str , title="Afternoon weather 🌇")
  
def displayEveningTemp():
  pync.notify(evening_temp_str , title="Night weather 🌉")
  
parse_time = int(curr_time_parse[:2])#The time parse in integer


# display the temperature according to the time of the day
if (parse_time in [19,20,21,22,23,0,1,2,3,4,5]):
  displayEveningTemp()
elif (parse_time in list(range(6,13))):
  displayMorningTemp()
else :
  displayAfterNoonTemp()
    

  