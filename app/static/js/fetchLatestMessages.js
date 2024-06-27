let timestamp = Date.now()

async function fetchLatestMessages() {
    try {
        let utc = new Date(timestamp).toISOString();
        let token = localStorage.getItem("anonChatRoom");
        let response = await fetch(`${window.location.origin}/messages/get_latest?timestamp=${utc}`, {
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            }
        });

        if (response.status === 204) {
            return [];
        }

        let messages = await response.json();

        if (messages.length > 0) {
            messages.forEach(message => {
                addMessageToUI(message.content, message.owner.username, false);
            });
        }

    } catch (error) {
        console.error(error);
    } finally {
        timestamp = Date.now();
        setTimeout(fetchLatestMessages, 1000);
    }
}
