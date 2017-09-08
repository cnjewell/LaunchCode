
@app.route("/")
def index():
    
    encoded_error = request.args.get("error")
    return render_template('edit.html', watchlist=get_current_watchlist(logged_in_user().id), error=encoded_error and cgi.escape(encoded_error, quote=True))

def get_current_watchlist(current_user_id):
    return Movie.query.filter_by(watched=False, owner_id=current_user_id).all()

def get_watched_movies(current_user_id):
    return Movie.query.filter_by(watched=True, owner_id=current_user_id).all()



@app.route("/add", methods=['POST'])
def add_movie():
    new_movie_name = request.form['new-movie']

    if (not new_movie_name) or (new_movie_name.strip() == ""):
        error = "Please specify the movie you want to add."
        return redirect("/?error=" + error)

    if new_movie_name in terrible_movies:
        error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie_name)
        return redirect("/?error=" + error)

    movie = Movie(new_movie_name, logged_in_user())
    db.session.add(movie)
    db.session.commit()
    return render_template('add-confirmation.html', movie=movie)

@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie_id = request.form['crossed-off-movie']

    crossed_off_movie = Movie.query.get(crossed_off_movie_id)
    if not crossed_off_movie:
        return redirect("/?error=Attempt to watch a movie unknown to this database")

    crossed_off_movie.watched = True
    db.session.add(crossed_off_movie)
    db.session.commit()
    return render_template('crossoff.html', crossed_off_movie=crossed_off_movie)

@app.route("/ratings", methods=['GET'])
def movie_ratings():
    return render_template('ratings.html', movies = get_watched_movies(logged_in_user().id))

@app.route("/rating-confirmation", methods=['POST'])
def rate_movie():
    movie_id = request.form['movie_id']
    rating = request.form['rating']

    movie = Movie.query.get(movie_id)
    if movie not in get_watched_movies(logged_in_user().id):
        error = "'{0}' is not in your Watched Movies list, so you can't rate it!".format(movie)
        return redirect("/?error=" + error)

    movie.rating = rating
    db.session.add(movie)
    db.session.commit()
    return render_template('rating-confirmation.html', movie=movie, rating=rating)