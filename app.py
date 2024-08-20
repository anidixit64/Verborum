from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///verborum.db'
db = SQLAlchemy(app)

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(200), nullable=False)
    back = db.Column(db.String(200), nullable=False)

# Create a new flashcard
@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    new_flashcard = Flashcard(front=data['front'], back=data['back'])
    db.session.add(new_flashcard)
    db.session.commit()
    return jsonify({"message": "Flashcard created!"}), 201

# Get all flashcards
@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    flashcards = Flashcard.query.all()
    return jsonify([{'id': f.id, 'front': f.front, 'back': f.back} for f in flashcards])

# Update a flashcard
@app.route('/flashcards/<int:id>', methods=['PUT'])
def update_flashcard(id):
    flashcard = Flashcard.query.get_or_404(id)
    data = request.get_json()
    flashcard.front = data['front']
    flashcard.back = data['back']
    db.session.commit()
    return jsonify({"message": "Flashcard updated!"})

# Delete a flashcard
@app.route('/flashcards/<int:id>', methods=['DELETE'])
def delete_flashcard(id):
    flashcard = Flashcard.query.get_or_404(id)
    db.session.delete(flashcard)
    db.session.commit()
    return jsonify({"message": "Flashcard deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
