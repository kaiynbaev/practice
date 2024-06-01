document.addEventListener('DOMContentLoaded', function() {
    const messageElement = document.getElementById('message');
    const imageElement = document.getElementById('room-image');

    if (messageElement && imageElement) {
        fetch('http://localhost:8000/api/data')
            .then(response => response.json())
            .then(data => {
                messageElement.innerText = data.message;
                imageElement.src = data.image_url;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                messageElement.innerText = 'Failed to load data';
            });
    } else {
        console.error('Required DOM elements not found');
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const messageElement = document.getElementById('message2');
    const imageElement = document.getElementById('room-image2');

    if (messageElement && imageElement) {
        fetch('http://localhost:8000/api/data2')
            .then(response => response.json())
            .then(data => {
                messageElement.innerText = data.message;
                imageElement.src = data.image_url;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                messageElement.innerText = 'Failed to load data';
            });
    } else {
        console.error('Required DOM elements not found');
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const messageElement = document.getElementById('message3');
    const imageElement = document.getElementById('room-image3');

    if (messageElement && imageElement) {
        fetch('http://localhost:8000/api/data3')
            .then(response => response.json())
            .then(data => {
                messageElement.innerText = data.message;
                imageElement.src = data.image_url;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                messageElement.innerText = 'Failed to load data';
            });
    } else {
        console.error('Required DOM elements not found');
    }
});



