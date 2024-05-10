// script.js
function toggleChatbot() {
    var chatbotIcon = document.querySelector('.chatbot-icon');
    var chatbotBox = document.getElementById('chatbotBox');
    if (chatbotIcon.getAttribute('data-state') === 'closed') {
        // Open the chatbot and show the close icon
        chatbotIcon.innerHTML = '&#128473;'; // Close icon
        chatbotIcon.setAttribute('data-state', 'open');
        chatbotBox.style.display = 'block';
    } else {
        // Close the chatbot and show the open icon
        chatbotIcon.innerHTML = '&#128512;'; // Chat icon
        chatbotIcon.setAttribute('data-state', 'closed');
        chatbotBox.style.display = 'none';
    }
}

function sendMessage() {
    var message = document.getElementById('userMessage').value;

    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chatbotResponse').innerText = data.response;
    })
    .catch(error => console.error('Error:', error));
}

function displayMessage(message, sender) {
    var chatMessages = document.querySelector('.chat-messages');
    var newMessage = document.createElement('div');
    newMessage.textContent = message;
    if (sender === 'user') {
        newMessage.classList.add('user-message');
    } else {
        newMessage.classList.add('bot-message');
    }
    chatMessages.appendChild(newMessage);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}