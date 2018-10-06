# Python weather API client
Python script which interacts with the O​penWeatherMap​ API to retrieve the current temperature for a city.

## Getting Started
To use the script requires an OpenWeatherMap API key. To obtain a key:
1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to create a free account. 
2. Log in and navigate to [API keys](https://home.openweathermap.org/api_keys) to get a free API key.
NB: It may take a few minutes for the API key to become active

Once you have a key you can run this in docker as:
`docker run -e OPENWEATHERMAP_KEY=​{key}​ ​{username}​/weather {city}` 
on a fresh VM with Docker installed, replacing “​{key}”​ with an OpenWeatherMap API key and “​{username}”​ with your Docker hub username and {city} with your chosen city.

## References
*[OpenWeatherMap website](https://openweathermap.org)
*[OpenWeatherMap web API docs](https://openweathermap.org/api)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
