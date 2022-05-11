from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "testapp"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows Madlibs form"""

    return render_template('home.html',prompts=story.prompts)

@app.route('/story')
def show_story():
    """Displays story from Madlibs form"""
    madlib_keys = request.args
    madlib_story = story.generate(madlib_keys)

    return render_template('story.html', madlib_story=madlib_story)    