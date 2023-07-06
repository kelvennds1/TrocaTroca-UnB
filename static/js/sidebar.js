const hamburgerIcon = document.getElementById("hamburgerIcon");
const sidebar = document.querySelector(".sidebar");

hamburgerIcon.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});
