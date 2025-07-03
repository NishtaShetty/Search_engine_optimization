let currentPage = 0;

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    const start = currentPage * 10;
    const end = start + 10;
    const pageResults = results.slice(start, end);

    // Display results in styled boxes
    pageResults.forEach(doc => {
        const resultBox = document.createElement('div');
        resultBox.className = 'result-item';
        resultBox.textContent = doc;
        resultsDiv.appendChild(resultBox);
    });

    const moreButton = document.getElementById('moreButton');
    moreButton.style.display = results.length > 10 ? 'block' : 'none';
}

document.getElementById('searchButton').addEventListener('click', function() {
    const query = document.getElementById('searchQuery').value;
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
        currentPage = 0;
        if (data.results.length === 0) {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<p>No results found for "' + query + '".</p>';
        } else {
            displayResults(data.results);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '<p>An error occurred while searching. Please try again later.</p>';
    });
});

document.getElementById('moreButton').addEventListener('click', function() {
    currentPage++;
    const query = document.getElementById('searchQuery').value;
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data.results);
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('resetButton').addEventListener('click', function() {
    document.getElementById('searchQuery').value = '';
    document.getElementById('results').innerHTML = '';
});
