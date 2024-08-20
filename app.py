from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config['development'])

db = SQLAlchemy(app)

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Flashcard {self.word}>'

@app.route('/')
def home():
    return "Welcome to Verborum - Your SRS Language Learning App!"

if __name__ == "__main__":
    app.run()

