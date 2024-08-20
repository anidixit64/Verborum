from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///verborum.db'
db = SQLAlchemy(app)

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(200), nullable=False)
    back = db.Column(db.String(200), nullable=False)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Get all flashcards
@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    flashcards = Flashcard.query.all()
    return jsonify([{'id': fc.id, 'front': fc.front, 'back': fc.back} for fc in flashcards])

# Create a new flashcard
@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    new_flashcard = Flashcard(front=data['front'], back=data['back'])
    db.session.add(new_flashcard)
    db.session.commit()
    return jsonify({'message': 'Flashcard created successfully!'})

# Delete a flashcard
@app.route('/flashcards/<int:id>', methods=['DELETE'])
def delete_flashcard(id):
    flashcard = Flashcard.query.get(id)
    if flashcard:
        db.session.delete(flashcard)
        db.session.commit()
        return jsonify({'message': 'Flashcard deleted successfully!'})
    else:
        return jsonify({'message': 'Flashcard not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
