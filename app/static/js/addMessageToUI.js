async function performMessageRequest(content) {
    const token = localStorage.getItem("anonChatRoom");

    // TODO: try to use this request to implement hiding the chat page from unauthenticated users
    const response = await fetch(`${window.location.origin}/messages/create`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ content: content })
    });

    if (!response.ok) {
        showFlashNotification("red", "Could not authenticate user!");
    }

    const data = await response.json();
    return data;
}

async function createMessage(messageText) {
    try {
        const msg = await performMessageRequest(messageText);

        addMessageToUI(msg.content, msg.owner.username, true)
        timestamp = Date.now();
    } catch (error) {
        console.error('Error:', error);
    }
}

function addMessageToUI(messageText, messageOwner, inputClear) {
    if (inputClear === undefined) {
        inputClear = true;
    }
    const messageContainer = document.getElementById('messageContainer');
    const messageWrapper = document.createElement('div');
    messageWrapper.className = "mb-2";
    const messageUsername = document.createElement('div');
    messageUsername.className = "text-xs text-gray-500";
    messageUsername.textContent = messageOwner;
    const messageElement = document.createElement('div');
    messageElement.className = "p-2 bg-blue-100 rounded";
    messageElement.textContent = messageText;
    
    messageWrapper.appendChild(messageUsername);
    messageWrapper.appendChild(messageElement);
    
    messageContainer.appendChild(messageWrapper);
    if (inputClear === true) {
        messageInput.value = "";
    }
    messageContainer.scrollTop = messageContainer.scrollHeight;
}