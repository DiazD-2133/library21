var dropdown = document.getElementsByClassName("dropdown-icon");
var auto_dropdown = document.getElementsByClassName("open");
const navMenu = document.querySelector("#navMenu");
const modal = document.querySelector(".modal");


navMenu.addEventListener( "click", () => {
    navMenu.previousElementSibling.classList.toggle("active");
    navMenu.classList.toggle("active");
    navMenu.nextElementSibling.classList.toggle("active");
});


modal.addEventListener( "click", () => {
    modal.classList.toggle("active");
    navMenu.classList.toggle("active");
    navMenu.nextElementSibling.classList.toggle("active");
});


var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.parentElement.classList.toggle("active");
    this.previousElementSibling.classList.toggle("active");
    this.classList.toggle("active");
    var dropdownContent = this.parentElement.nextElementSibling;
    if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
    } else {
        dropdownContent.style.display = "block";
    }
  });
}

var i;

for (i = 0; i < auto_dropdown.length; i++) {
    if (auto_dropdown[i].style.display === "block") {
        dropdown.style.display = "none";
    } else {
        auto_dropdown[i].style.display = "block";
    }
}

