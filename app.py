from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "testapp"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Show story template"""

    return render_template('home.html', stories=stories.values())


@app.route('/ml_form')
def show_ml():
    """Shows Madlibs form"""
    
    story_id = request.args["template"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("ml_form.html",
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)
    
   

@app.route('/story')
def show_story():
    """Displays story from Madlibs form"""
    
    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html",
                           title=story.title,
                           text=text)