from flask import request, redirect, render_template, session, flash
from app import app, db
from models import User, Post
from werkzeug.routing import BaseConverter
from hashutils import check_pw_hash, make_salt, make_pw_hash
import cgi, re
import caesar

###############################################
############### GENERAL TODOS #################
###############################################

# TODO: Update validation errors to mark form fields as well as a flash message
# TODO: Move RegexConverter to app.py after I'm used to setting up regex routes

###############################################
############## ROUTING HELPER #################
###############################################

# For regex routing
# Found on StackOverflow

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter


# EXAMPLE #

# @app.route('/<regex("[abcABC0-9]{4,6}"):uid>-<slug>/')
# def example(uid, slug):
#     return "uid: %s, slug: %s" % (uid, slug)

# this URL should return with 200: http://localhost:5000/abc0-foo/
# this URL should will return with 404: http://localhost:5000/abcd-foo/


###############################################
################## USER AUTH ##################
###############################################

login_not_needed = ['login', 'register', 'blog', 'wuwei', 'web_caesar']
# TODO: Sessions were acting up on me. Including the logout route helped. Diagnose
# login_not_needed = ['login', 'register', 'blog', 'wuwei', 'web_caesar', 'logout']

@app.before_request
def require_login():
    if not ('user' in session or request.endpoint in login_not_needed):
        return redirect("/login")

def logged_in_user():
    return User.query.filter_by(email=session['user']).first()

email_regex = re.compile(r'^[-\w]+@[-\w]+[.][-\w]+$')
def is_email(string):
    if email_regex.match(string):
        return True
    else:
        return False

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']
        
        # VAILDATION #

        if email == '' or password == '':
            flash('Error: One or more fields left blank', category="error")
            return redirect('/register')

        # TODO : test this works properly, I'm skeptical
        users = User.query.filter_by(email=email)
        if users.count() != 1:
            flash('Error: Bad username or password', category="error")
            return redirect("/login")            

        user = users.first()        
        pw_hash, salt = user.pw_hash.split(',')
        test_pw_hash, salt = make_pw_hash(password, salt).split(',')

        if test_pw_hash != pw_hash:
            flash('Error: Bad username or password', category="error")
            return redirect("/login")     
        
        # SUCCESS # 

        session['user'] = user.email
        flash('Welcome Back, '+user.email, category="message")
        return redirect("/")



@app.route("/register", methods=['GET', 'POST'])
def register():
    
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        # VALIDATION #

        if email == '' or password == '' or verify == '':
            flash('Error: One or more fields left blank', category="error")
            return redirect('/register')

        if not is_email(email):
            flash('Error: Entered email is not formatted like an email address', category="error")
            return redirect('/register')
        
        email_db_count = User.query.filter_by(email=email).count()
        if email_db_count > 0:
            flash('Error: Email is already taken.', category="error")
            return redirect('/register')

        if len(email) < 3 or len(password) < 3:
            flash('Error: Email or password is too short', category="error")
            return redirect('/register')            

        if password != verify:
            flash('Error: Passwords entered do not match.', category="error")
            return redirect('/register')

        # SUCCESS #

        pw_hash = make_pw_hash(password)
        user = User(email=email, pw_hash=pw_hash)
        db.session.add(user)
        db.session.commit()
        
        session['user'] = user.email
        flash('Successfully registered, '+user.email, category="message")
        return redirect("/")

@app.route("/logout")
def logout():
    user = session['user']
    del session['user']
    flash('Successfully logged out of '+user.email, category="message")
    return redirect("/")



###############################################
##################### BLOG ####################
###############################################

# TODO: BLOGZ reqs
    # 1 - posts by author page
    # 2 - author listed in posts
    # 3 - link to posts-by-author from post
    # 4 - link to registration form login page

# TODO: IF I WANT BLOG/USER IN URL
    # - add username to User object.
    # - recreate tables for User.
    # - add username to registration view-func
    # - add username to reg.html form

@app.route("/blog")
def blog():
    
    post_id = request.args.get("id")
    if post_id:
        postlist = Post.query.filter_by(id=post_id).all()
    else:
        postlist = Post.query.order_by(Post.id.desc()).all()
        # TODO (limit this query.all() somehow... Include pagination?)
    return render_template("blog.html", postlist=postlist)


@app.route("/newpost", methods=['GET', 'POST'])
def newpost():
    if request.method == "GET":
        return render_template("newpost.html", title='', body='')
    
    if request.method == "POST":
        
        # TODO: Implement slugs and slugifier

        title = request.form['title']
        body = request.form['body']
        
        if title == '' or body == '':
            flash("Title and Body fields cannot be left blank", category="error")
            return render_template("newpost.html", title=title, body=body)
        
        new_post = Post(title, body, logged_in_user())
        db.session.add(new_post)
        db.session.commit()
        flash("Success: New blog post published.", category="message")
        return render_template('blog.html', postlist=Post.query.filter_by(id=new_post.id).all())



###############################################
##################### MISC ####################
###############################################

@app.route("/")
def index():
    return render_template('index.html')
    # Explaination of my multi-assignment conglomeration here

@app.route("/wuwei")
def wuwei():
    return render_template('wuwei.html')

@app.route("/web_caesar", methods=['GET', 'POST'])
def web_caesar():
    
    text = ''
    rot = 0
    
    if request.method == 'POST':
        text = request.form['text']
        rot = request.form['rot']
        
        if text == '' or rot == '':
            flash('Enter required values. Either rot or text area is blank.', category="error")
            return render_template('web_caesar.html', text=text, rot=rot)

        try:
            text = caesar.encrypt(text, rot)
        except ValueError:
            flash('Numbers only for rotation value.', category="error")

    return render_template('web_caesar.html', text=text, rot=rot)


if __name__ == "__main__":
    app.run()