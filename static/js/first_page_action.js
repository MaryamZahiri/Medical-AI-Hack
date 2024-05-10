// Function to handle button click
document.getElementById("analyseButton").addEventListener("click", function() {
    // Get the form data
    var formData = new FormData(document.getElementById("uploadForm"));

    // Send a POST request to upload the file
    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Extracted text and word count
        var extractedText = data.split("\nTotal words in the document: ")[0];
        var wordCount = data.split("\nTotal words in the document: ")[1];

        // Update the HTML elements with extracted text and word count
        document.getElementById("extractedText").textContent = extractedText;
        document.getElementById("wordCount").textContent = "Total words in the document: " + wordCount;

        // Show the extracted text container
        document.getElementById("extractedTextContainer").style.display = "block";

        // Hide the first page box
        document.getElementById("firstPageBox").style.display = "none";
    })
    .catch(error => console.error("Error:", error));
});