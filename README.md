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
XML_API_URI=https://www.omdbapi.com/?r=xml&apikey=<your api key> - tagert server address with
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

The API has only one endpoint `/`.
Endpoint's description for default settings:
```
security:
  - bearerAuth: [ ]
paths:
  /:
    get:
      summary: "Retrieve movie information"
      parameters:
        - name: "title"
          in: query
          description: "Movie title"
          schema:
            type: "string"
            example: "Lost"
      responses:
        "200":
          description: "Data retrieved properly"
          content:
            application/json:
              schema:
                type: "object"
                example: {"title": "Lost",
                          "year": "2004–2010",
                          "rated": "TV-14",
                          "released": "22 Sep 2004",
                          "runtime": "44 min",
                          "genre": "Adventure, Drama, Fantasy, Mystery, Sci-Fi, Thriller",
                          "director": "N/A",
                          "writer": "J.J. Abrams, Jeffrey Lieber, Damon Lindelof",
                          "actors": "Jorge Garcia, Josh Holloway, Yunjin Kim, Evangeline Lilly",
                          "plot": "The survivors of a plane crash are forced to work together in order to survive on a seemingly deserted tropical island.",
                          "language": "English, Portuguese, Spanish, Arabic, French, Korean, German, Latin, Russian, Japanese",
                          "country": "USA",
                          "awards": "Won 1 Golden Globe. Another 112 wins &amp; 398 nominations.",
                          "poster": "https://m.media-amazon.com/images/M/MV5BNzhlY2E5NDUtYjJjYy00ODg3LWFkZWQtYTVmMzU4ZWZmOWJkXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
                          "metascore": "N/A",
                          "imdbRating": "8.3",
                          "imdbVotes": "498,563",
                          "imdbID": "tt0411008",
                          "type": "series"}
        "400":
          description: "Request validation error"
        "401":
          description: "Token validation error"
        "404":
          description: "Movie not found"
        "500":
          description: "Server Error"
```