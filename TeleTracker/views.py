from flask import render_template
from TeleTracker import TeleTracker

@TeleTracker.route('/')
def index():
	return render_template('index.html')
