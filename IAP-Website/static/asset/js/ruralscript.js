const hamburger = document.querySelector(".hamburger");
const navlist = document.querySelector(".nav-list-item");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navlist.classList.toggle("active");
})

document.querySelectorAll(".navbar-link").forEach(n => n.
addEventListener("click", () =>{
    hamburger.classList.remove("active");
    navlist.classList.remove("active");
}) )