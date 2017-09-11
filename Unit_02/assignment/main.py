from app import app, db
from flask import request, redirect, render_template, session, flash
from werkzeug.routing import BaseConverter
import cgi, re


from models import User, Post
from hashutils import check_pw_hash, make_salt, make_pw_hash
import caesar

###############################################
############## ROUTING HELPER #################
###############################################

# For regex routing
# Found on StackOverflow

# TODO: Move RegexConverter to app.py after I'm used to setting up regex routes

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

login_needed = ['newpost', 'logout']

@app.before_request
def require_login():
    if ('user' not in session or request.endpoint in login_needed):
        flash('Login required to access certain pages.', category='error')
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

        # TODO : Test this works properly, I'm skeptical

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
    # Usernames
    # - add username to User model
    # - add username to /registration view
    # - validate usernames:
        # - are not empty strings
        # - are greater than 3 characters
        # - alpha-numeric, hyphens, underscores
    # - refactor username into templates where email was used before
    # - reinitalize database for updated User model

    # Authors
    # - posts by author page
    # - authors.html, list of all the authors
    # - Include author's username in all posts by that author
    # - Author's name links to post-by-author page, add to templates

    # Posts
    # - post title links to individual post in templates
    # - add DateTime to Post model
        # - add datetime to templates displaying posts
        # - reinitalize database for updated Post model

# TODO: /blog                   display all authors
# TODO: /blog/username          display all posts by single author, pagination included
# TODO: /blog/posts             display all posts, pagination included
# TODO: /blog/posts/post_id     display a single post

@app.route("/blog", methods=['GET'])
@app.route("/blog/<username>", methods=['GET'])
def blog(username=None):
    # TODO: Sanitize <username> else risk a SQL injection! GAH! 
    if username:
        # TODO: Wait! This query is wrong. I need to change the model relationships I think.
        postlist = Post.query.filter_by(owner=username).all()
        return render_template("blog.html", postlist=postlist)
    else:
        authors = User.query.all()
        return render_template("authors.html", authors=authors)


@app.route('/blog/posts/', methods=['GET'])
@app.route('/blog/posts/<int:post_id>', methods=['GET'])
def blog_posts(post_id=None):
    if post_id:
        postlist = Post.query.filter_by(id=post_id).all()
    else:
        postlist = Post.query.order_by(Post.id.desc()).all()
    return render_template("blog.html", postlist=postlist)


@app.route("/blog/newpost", methods=['GET', 'POST'])
def newpost():
    if request.method == "GET":
        return render_template("newpost.html", title='', body='')
    
    if request.method == "POST":
        
        # TODO: Implement slugs and slugifier?

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