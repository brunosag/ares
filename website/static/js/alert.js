var alert = document.querySelector(".alert")
var alertClose = document.querySelector(".alert-close")

alertClose.addEventListener("click", () => {
    alert.classList.remove("show")
})