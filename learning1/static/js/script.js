document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("fileInput");
  const fileLabel = document.querySelector(".custom-file-label");
  const fileNameSpan = document.querySelector(".file-name");

  fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
      fileNameSpan.textContent = fileInput.files[0].name;
    } else {
      fileNameSpan.textContent = "No file chosen";
    }
  });

  document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById("exampleTextarea");
    // Set the cursor to the beginning
    textarea.setSelectionRange(0, 0);
  });

  const form = document.getElementById("myForm");
  form.addEventListener("submit", function (event) {
    form.querySelectorAll("input").forEach(function (input) {
      input.setCustomValidity("");

      if (!input.validity.valid) {
        switch (input.type) {
          case "text":
            input.setCustomValidity("Please enter your name.");
            break;
          case "email":
            input.setCustomValidity("Please enter a valid email address.");
            break;
          case "password":
            input.setCustomValidity("Please enter a password.");
            break;
          case "file":
            input.setCustomValidity("Please choose a file.");
            break;
          default:
            input.setCustomValidity("Please fill out this field.");
        }
      }
    });
  });
});
