document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("myForm");
    var submittedImage = document.getElementById("submittedImage");
    var thankYouMessage = document.getElementById("thankYouMessage");

    form.addEventListener("submit", function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Show the thank you message
        thankYouMessage.textContent = "Your symptom tracker";
        
        // Show the submitted image
        submittedImage.style.display = "block";
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("myForm2");
    var submittedImage = document.getElementById("submittedImage2");
    var thankYouMessage = document.getElementById("thankYouMessage2");

    form.addEventListener("submit", function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Show the thank you message
        thankYouMessage.textContent = "Your insulin tracker";
        
        // Show the submitted image
        submittedImage.style.display = "block";
    });
});