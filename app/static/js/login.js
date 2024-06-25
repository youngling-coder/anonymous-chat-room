document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    // TODO: Implement flash messages via JS
    // TODO: Implement 404 error page
    // TODO: Implement static js files
    
    if(password && username) {
        try {
            const formData = new URLSearchParams();
            // formData.append('grant_type', 'password');
            formData.append('username', username);
            formData.append('password', password);

            const response = await fetch(`${window.location.origin}/auth/login`, {
                method: "POST",
                body: formData
            });
            if (response.ok) {
                const data = await response.json();

                window.localStorage.setItem("anonChatRoom", `${data.access_token}`);
                
                const profilePageUrl = profilePageUrlTemplate.replace('__USERNAME__', data.user.username);
                window.location.href = profilePageUrl;

                const errData = await response.json();
                alert(`Error: ${errData.detail}`);
            }
            
        } catch (error) {
            alert(`${error}`);
        }
    } else {
        alert("Enter username and password!");
    }
});