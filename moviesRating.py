from flask import Flask, render_template
import urllib2, requests, json


app = Flask(__name__)

bbc_url = "http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json"
movieDb_api = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'
key = '935be2f95e54dddddc67f6ee8953c6c0'
poster_url='http://image.tmdb.org/t/p/original{url_to_poster}'

# Changing the behavior of dicts, creating a subclass that  
# automatically store duplicated values in lists under the same key.
class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


@app.route("/")
def movieInfoFinder():
    rating=Dictlist(dict())
    bbc_json_request=requests.get(bbc_url)
    bbc_json=bbc_json_request.json()
    
    # Iterating through the movie titles to get all the infos 
    # needed from the movieDb API and the bbc json
    for i in range(len(bbc_json['episodes'])):
 
        title = bbc_json['episodes'][i]['programme']['title']
        movie_db = json.load(urllib2.urlopen(movieDb_api.format(key=key,title=urllib2.quote(title))))
        plot = bbc_json['episodes'][i]['programme']['short_synopsis']

        if movie_db['results']:
            rating[title] = movie_db['results'][0]['vote_average']
            rating[title] = plot
            rating[title] = poster_url.format(url_to_poster=movie_db['results'][0]['poster_path'])
            
        # If the movie title is not found in the movieDb    
        else:
            rating[title] = 'Not found in the db' 
            rating[title] = plot 

    return render_template('index.html', rating=rating)
    
if __name__ == '__main__':
    app.run(debug=True)   