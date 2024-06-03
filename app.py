from flask import Flask, render_template
import logging
from logstash_formatter import LogstashFormatterV1

app = Flask(__name__)
app.static_folder = 'static'

# Данные о музыканте (замените на свои данные)
musician = {
    'name': 'MxrnGate',
    'bio': 'Sound Designer',
    'social_links': {
        'Spotify': 'https://open.spotify.com/artist/0pbgDgbEqlMyXDG6iQ0QHf',
        'Twitter': 'https://www.twitter.com/mxrngate',
        'Instagram': 'https://www.instagram.com/mxrngate',
    }
}

# Настройка логирования
logger = logging.getLogger("flask-logstash-logger")
logger.setLevel(logging.INFO)

logstash_handler = logging.FileHandler('/app/flask_app.log')
logstash_handler.setFormatter(LogstashFormatterV1())

logger.addHandler(logstash_handler)

@app.route('/')
def index():
    logger.info('Page accessed')
    return render_template('index.html', musician=musician)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
