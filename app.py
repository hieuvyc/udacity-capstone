from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from database.models import setup_db, Movie, Actor, database_path
from auth.auth import requires_auth

app = Flask(__name__)
setup_db(app, database_path)
CORS(app)

@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(payload):
    try:
        actors = Actor.query.all()
        return jsonify({
            "success": True,
            "actors": [actor.format() for actor in actors]
        })
    except Exception as e:
        print(e)

@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies(payload):
    try:
        movies = Movie.query.all()
        return jsonify({
            "success": True,
            "movies": [movie.format() for movie in movies]
        })
    except Exception as e:
        print(e)

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actor(payload):
    body = request.get_json()

    if not body or not body.get('name') or not body.get('age') or not body.get('gender'):
        abort(400, description="Missing required fields")

    try:
        actor = Actor(name=body['name'], age=body['age'], gender=body['gender'])
        actor.insert()
        return jsonify({
            "success": True,
            "actor": actor.format()
        })
    except Exception as e:
        print(e)

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movie(payload):
    body = request.get_json()

    if not body or not body.get('title') or not body.get('release_date'):
        abort(400, description="Missing required fields")

    try:
        movie = Movie(title=body['title'], release_date=body['release_date'])
        movie.insert()
        return jsonify({
            "success": True,
            "movie": movie.format()
        })
    except Exception as e:
        print(e)

@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(payload, actor_id):
    body = request.get_json()
    actor = Actor.query.get(actor_id)

    if not actor:
        abort(404)

    try:
        if 'name' in body:
            actor.name = body['name']
        if 'age' in body:
            actor.age = body['age']
        if 'gender' in body:
            actor.gender = body['gender']

        actor.update()
        return jsonify({
            "success": True,
            "actor": actor.format()
        })
    except Exception as e:
        print(e)

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movie(payload, movie_id):
    body = request.get_json()
    movie = Movie.query.get(movie_id)

    if not movie:
        abort(404)

    try:
        if 'title' in body:
            movie.title = body['title']
        if 'release_date' in body:
            movie.release_date = body['release_date']

        movie.update()
        return jsonify({
            "success": True,
            "movie": movie.format()
        })
    except Exception as e:
        print(e)

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(payload, actor_id):
    actor = Actor.query.get(actor_id)

    if not actor:
        abort(404)

    try:
        actor.delete()
        return jsonify({
            "success": True,
            "delete": actor_id
        })
    except Exception as e:
        print(e)

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(payload, movie_id):
    movie = Movie.query.get(movie_id)

    if not movie:
        abort(404)

    try:
        movie.delete()
        return jsonify({
            "success": True,
            "delete": movie_id
        })
    except Exception as e:
        print(e)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": error.description
    }), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
    }), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    app.run(debug=True)
