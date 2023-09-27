from flask import Flask, render_template

app = Flask(__name__)

# Данные о музыканте (замените на свои данные)
musician = {
    'name': 'MxrnGate666',
    'bio': 'Sound Designer',
    'social_links': {
        'Spotify': 'https://open.spotify.com/artist/0pbgDgbEqlMyXDG6iQ0QHf',
        'Twitter': 'https://www.twitter.com/mxrngate',
        'Instagram': 'https://www.instagram.com/mxrngate',
    }
}


@app.route('/')
def index():
    return render_template('index.html', musician=musician)


