const apiBaseUrl = 'http://localhost:8000/api/book';

async function createBook() {
    const title = document.getElementById('createTitle').value;
    const author = document.getElementById('createAuthor').value;
    const description = document.getElementById('createDescription').value;
    const publishedYear = document.getElementById('createPublishedYear').value;

    const response = await fetch(`${apiBaseUrl}/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, author, description, published_year: publishedYear })
    });

    if (response.ok) {
        alert('Book created successfully!');
    } else {
        alert('Error creating book.');
    }
}

async function getAllBooks() {
    const response = await fetch(apiBaseUrl, {
        method: 'GET'
    });

    if (response.ok) {
        const books = await response.json();
        document.getElementById('allBooks').innerText = JSON.stringify(books, null, 2);
    } else {
        alert('Error fetching all books.');
    }
}

async function getBook() {
    const bookId = document.getElementById('readBookId').value;

    const response = await fetch(`${apiBaseUrl}/${bookId}`, {
        method: 'GET'
    });

    if (response.ok) {
        const book = await response.json();
        document.getElementById('bookDetails').innerText = JSON.stringify(book, null, 2);
    } else {
        alert('Error fetching book.');
    }
}

async function updateBook() {
    const bookId = document.getElementById('updateBookId').value;
    const title = document.getElementById('updateTitle').value;
    const author = document.getElementById('updateAuthor').value;
    const description = document.getElementById('updateDescription').value;
    const publishedYear = document.getElementById('updatePublishedYear').value;

    const data = {};
    if (title) data.title = title;
    if (author) data.author = author;
    if (description) data.description = description;
    if (publishedYear) data.published_year = parseInt(publishedYear);

    const response = await fetch(`${apiBaseUrl}/${bookId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    if (response.ok) {
        alert('Book updated successfully!');
    } else {
        alert('Error updating book.');
    }
}

async function deleteBook() {
    const bookId = document.getElementById('deleteBookId').value;

    const response = await fetch(`${apiBaseUrl}/${bookId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        alert('Book deleted successfully!');
    } else {
        alert('Error deleting book.');
    }
}