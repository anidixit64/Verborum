document.addEventListener('DOMContentLoaded', function() {
    const flashcardsContainer = document.getElementById('flashcards-container');
    const createFlashcardForm = document.getElementById('create-flashcard-form');

    // Fetch and display all flashcards
    fetch('/flashcards')
        .then(response => response.json())
        .then(data => {
            data.forEach(flashcard => {
                const flashcardDiv = document.createElement('div');
                flashcardDiv.className = 'flashcard';
                flashcardDiv.innerHTML = `
                    <strong>${flashcard.front}</strong><br>
                    ${flashcard.back}<br>
                    <button onclick="deleteFlashcard(${flashcard.id})">Delete</button>
                `;
                flashcardsContainer.appendChild(flashcardDiv);
            });
        });

    // Create a new flashcard
    createFlashcardForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const front = document.getElementById('front').value;
        const back = document.getElementById('back').value;

        fetch('/flashcards', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ front, back })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            location.reload(); // Reload the page to see the new flashcard
        });
    });
});

// Delete a flashcard
function deleteFlashcard(id) {
    fetch(`/flashcards/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload(); // Reload the page to see the updated list of flashcards
    });
}
