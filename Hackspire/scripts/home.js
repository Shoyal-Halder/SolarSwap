document.addEventListener("DOMContentLoaded", () => {
    const heading = document.getElementById("solarSwap");
    setTimeout(() => {
        heading.style.animation = "slideUp 2s ease-out forwards";
        document.querySelector(".content").style.display = "block";
    }, 2000);
});
