document.getElementById("signupForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    fetch("http://localhost:5000/signup", {
        method: "POST",
        body: formData,
    }).then(() => {
        window.location.href = "dashboard.html";
    });
});

function redirectToDashboard() {
    window.location.href = "dashboard.html";
}
