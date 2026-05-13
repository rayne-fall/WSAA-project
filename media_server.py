from flask import Flask, jsonify
#https://www.geeksforgeeks.org/websites-apps/cross-origin-resource-sharing-cors/
from flask_cors import CORS, cross_origin
from DAO import mediaDAO

app = Flask(__name__)
cors = CORS(app) # allow cross-origin resource sharing

app = Flask(__name__, static_url_path='', static_folder='.')

# 127.0.0.1:5000/
@app.route('/')
@cross_origin()
def index():
    return 'Welcome to the Media Server'

# 127.0.0.1:5000/tvshows
@app.route('/tvshows')
@cross_origin()
def getAlltvShows():
    results=mediaDAO().getAlltv()
    return jsonify(results)

# 127.0.0.1:5000/tvshows/<int:id>
@app.route('/tvshows/<int:id>')
@cross_origin()
def findTVById(id):
    foundTV = mediaDAO().findTVByID(id)
    return jsonify(foundTV)

# add a new tv show
@app.route('/tvshows', methods=['POST'])
@cross_origin()
def createTV():
    if not request.json:
        abort(400)
    tvshow = {
        "title": request.json['title'],
        "genre": request.json['genre'],
        "year": request.json['year'],
    }
    addedshow = mediaDAO.create(tvshow)
    return jsonify(addedshow)

# update one of the tv shows in the database
@app.route('/tvshows/<int:id>', methods=['PUT'])
@cross_origin()
def updateTV(id):
    foundShow= mediaDAO.findTVByID(id)
    if not foundShow:
        abort(404)
    if not request.json:
        abort(400)
    reqJson= request.json
    if 'year' in reqJson and type(reqJson['year']) is not int:
        abort(400)
    if 'title' in reqJson:
        foundShow['title'] = reqJson['title']
    if 'genre'in reqJson:
        foundShow['genre'] = reqJson['genre']
    if 'year' in reqJson:
        foundShow['year'] = reqJson['year']
    mediaDAO.update(id,foundShow)
    return jsonify(foundShow)

# delete a tv show
@app.route('/tvshows/<int:id>', methods=['DELETE'])
@cross_origin()
def deleteTV(id):
    mediaDAO.delete(id)
    return jsonify({"done":True})

# 127.0.0.1:5000/videogames
@app.route('/videogames')
@cross_origin()
def getAllvideogames():
    results=mediaDAO().getAllVideoGames()
    return jsonify(results)

# 127.0.0.1:5000/videogames/<int:id>
@app.route('/videogames/<int:id>')
@cross_origin()
def findVGById(id):
    foundVideogame = mediaDAO().findVideoGameByID(id)
    return jsonify(foundVideogame)

# add a new video game
@app.route('/videogames', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)
    video_game = {
        "title": request.json['title'],
        "genre": request.json['genre'],
        "year": request.json['year'],
    }
    addedgame = mediaDAO.create(video_game)
    return jsonify(addedgame)

# update one of the video games in the database
@app.route('/videogames/<int:id>', methods=['PUT'])
@cross_origin()
def updateVideogame(id):
    foundGame= mediaDAO.findVideoGameByID(id)
    if not foundGame:
        abort(404)
    if not request.json:
        abort(400)
    reqJson= request.json
    if 'year' in reqJson and type(reqJson['year']) is not int:
        abort(400)
    if 'title' in reqJson:
        foundGame['title'] = reqJson['title']
    if 'genre'in reqJson:
        foundGame['genre'] = reqJson['genre']
    if 'year' in reqJson:
        foundGame['year'] = reqJson['year']
    mediaDAO.update(id,foundGame)
    return jsonify(foundGame)

# delete a video game
@app.route('/tvshows/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    mediaDAO.delete(id)
    return jsonify({"done":True})

# run the server with the debugger
if __name__=='__main__':
    app.run(debug=True)