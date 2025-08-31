document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');

    // Check if there's a query parameter from home page
    const urlParams = new URLSearchParams(window.location.search);
    const initialQuery = urlParams.get('q');
    if (initialQuery) {
        userInput.value = initialQuery;
        sendMessage();
    }

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');
        userInput.value = '';

        // Show loading
        const loadingDiv = addMessage('Thinking...', 'ai', true);

        // Send to backend
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: message })
        })
        .then(response => response.json())
        .then(data => {
            // Remove loading message
            loadingDiv.remove();
            
            if (data.error) {
                addMessage('Sorry, I encountered an error: ' + data.error, 'ai');
            } else {
                addMessage(data.response, 'ai');
            }
        })
        .catch(error => {
            // Remove loading message
            loadingDiv.remove();
            addMessage('Sorry, I encountered a connection error.', 'ai');
            console.error('Error:', error);
        });
    }

    function addMessage(text, sender, isLoading = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = sender === 'user' ? 'user-message' : 'ai-message';
        
        const bubbleDiv = document.createElement('div');
        bubbleDiv.className = sender === 'user' ? 'message-bubble user-bubble' : 'message-bubble ai-bubble';
        bubbleDiv.textContent = text;
        
        if (isLoading) {
            bubbleDiv.classList.add('loading');
        }
        
        messageDiv.appendChild(bubbleDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return messageDiv;
    }
});
