--------------------
# Movie API - frameworkless
Simple REST API allowing requesting information about movies (but not necessarily limited to that).


Works the same as Movie API but does not use any external libraries nor frameworks.
  
  
## Prerequisites
(if you do not wish to install anything use the attached *docker-compose* file.):
* Python 3.9
* Pipenv

optionally: 
* Docker


## Installing Movie API - frameworkless

To install File system API, follow these steps:
* Clone the repository and create a virtual environment with pipenv to install all the needed libraries
```
$ pipenv install
```
Create the following environmental variables or edit them in *docker-compose.yml*:
```
XML_API_URI=https://www.omdbapi.com/?r=xml&apikey=<your api key> - tagert server address !! remeber to update your API key
API_KEY=<applications key>
```

## Using Movie API - frameworkless

To use Movie API simply start it with:
```
python run.py 
```
Or use the provided `docker-compose.yml`:
```
docker-compose build
docker-compose up
```