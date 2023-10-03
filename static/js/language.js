
window.addEventListener("load", function () {
  setTimeout(function () {
    var loaderContainer = document.querySelector(".loader-container");
    loaderContainer.style.opacity = "0";
    setTimeout(function () {
      loaderContainer.style.display = "none";
    }, 500); // Adjust the timeout value as needed
  }, 1000); // Adjust the timeout value as needed
});
