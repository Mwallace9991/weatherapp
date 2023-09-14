#Matthew Wallace
#weather app
import requests
import config

def getCoords():
   city_name = input("Enter city: ")
   state_code = input("State code: ")
   country_code = input ("Country: ")
   base_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={config.appid}"
  
   response = requests.get(base_url)
   data = response.json()
   lat = data[0]["lat"]
   lon = data[0]["lon"]

   return (lat,lon)

def getweather(lat,lon):
    print()
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.appid}&units=imperial"
    response = requests.get(base_url)
    data = response.json() 
    temp = data['main']['temp']
    return (temp)



def main():
    lat,lon = getCoords()
    temp = getweather(lat,lon)
    print("Temperature",temp)





if __name__=="__main__":
    main()