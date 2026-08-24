const API_URL = "http://127.0.0.1:5000";


// =========================
// Register
// =========================

async function register() {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;


    const response = await fetch(
        `${API_URL}/api/auth/register`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })
        }
    );


    const data = await response.json();


    document.getElementById("message").textContent =
        data.message;
}



// =========================
// Login
// =========================

async function login() {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;


    const response = await fetch(
        `${API_URL}/api/auth/login`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })
        }
    );


    const data = await response.json();


    document.getElementById("message").textContent =
        data.message;


    if (data.success) {

        console.log("Logged in!");

        console.log(data.user);

    }

}