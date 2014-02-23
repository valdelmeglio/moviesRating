moviesRating
============
A python web app that pulls the current movies on BBC iPlayer (http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json or .xml), fetches
ratings for those movies from the Movie database (http://www.themoviedb.org/) and presents it
in a single page app.

## Technologies Used

* Python
* Flask
* Requests
* Json
* HTML5/Css
* Javascript
* Bootstrap
* Jinja2
* MarkupSafe
* Werkzeug
* itsdangerous
* wsgiref
 
## Setup
Install Python, Flask, Requests in your environment following the official guides: 

* [http://www.python.org][1]
* [http://flask.pocoo.org/docs/installation/#installation][2]
* [http://docs.python-requests.org/en/latest/user/install/#install][3]

Once downloaded the moviesRating project, open a terminal window and move to the project folder, then type: 
``` Bash
python moviesRating.py
``` 
You should see the following output:
``` Bash
* Running on http://127.0.0.1:5000/
* Restarting with reloader
``` 
Open a web browser and move to http://127.0.0.1:5000/ to make the app work


[1]: http://www.python.org
[2]: http://flask.pocoo.org/docs/installation/#installation
[3]: http://docs.python-requests.org/en/latest/user/install/#install