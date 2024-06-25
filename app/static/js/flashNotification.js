function showNotification(color, text) {
    // Create notification container
    const notificationContainer = document.createElement('div');
    notificationContainer.classList.add("hidden", "fixed", "bottom-5", "right-5", `bg-${color}-500`, "text-white", "p-4", "rounded-lg", "shadow-lg");

    // Create notification text element
    const notificationText = document.createElement("p");
    notificationText.textContent = text;
    notificationContainer.appendChild(notificationText);

    // Append notification container to the document body
    document.body.appendChild(notificationContainer);

    // Remove 'hidden' class and add 'fade-in' for animation
    notificationContainer.classList.remove('hidden');
    notificationContainer.classList.add("fade-in");

    // Set timeout to fade out and hide notification
    setTimeout(() => {
        notificationContainer.classList.remove("fade-in");
        notificationContainer.classList.add('fade-out');
    }, 2500);

    // Set timeout to hide notification completely
    setTimeout(() => {
        notificationContainer.classList.add('hidden');
    }, 3000);
}