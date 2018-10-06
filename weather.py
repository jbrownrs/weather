"""
Usage:
    weather.py (-h | --help)
    weather.py [--country=COUNTRY] <city>
    weather.py --version

Options:
    -h, --help          Show a brief usage summary.
    --country=COUNTRY   Restrict cities to an ISO 3166 country code.
    --version           Shows version

An OpenWeatherMap API key MUST be provided via the OPENWEATHERMAP_KEY
environment variable.
"""
import sys
import os
import requests
from docopt import docopt


# create url and get API response (metric values)
def url_response(argv):

    if "OPENWEATHERMAP_KEY" in os.environ:
        pass
    else:
        print("Error: OPENWEATHERMAP_KEY environment variable is not set")
        raise SystemExit(1)
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    key_url = base_url + "APPID=" + os.environ['OPENWEATHERMAP_KEY'] + "&q=" + sys.argv[1]
    country = arguments['--country']
    if country is not None and len(country) > 1:
        complete_url = key_url + "," + country + "&units=metric"
    else:
        complete_url = key_url + "&units=metric"
    # os.environ['OPENWEATHERMAP_KEY'] 
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    # convert response into python format
    x = response.json()
    return x


# return weather data
def api_data(x):

    if x["cod"] == 200:

        # store the value of "main" key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y (Celsius)
        current_temperature = y["temp"]

        # store the value of "weather" key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # store the value of "sys" key in variable a
        a = x["sys"]

        # store the value corresponding
        # to the "country" key of a
        country = a["country"]

        # store the value corresponding
        # to the "name" key of x 
        city = x["name"]
        
        # print following values
        print("Temperature for " + city + ", " + country +
              ": {:.1f}".format(current_temperature) + u"\u2103")
        print("Weather description for " + city + ", " + country + ": " + weather_description)

    elif x["cod"] == 401:
        print("Error 401: " + x["message"])

    else:
        print("Error 404: City Not Found")


if __name__ == '__main__':
    arguments = docopt(__doc__, version="Version 1.0")
    api_data(url_response(sys.argv[1]))
