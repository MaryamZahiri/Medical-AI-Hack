// Function to handle button click to jump to video section
document.getElementById("jumpToVideoButton").addEventListener("click", function() {
    // Get the top offset of the video section
    const videoSection = document.getElementById('video-section');
    const videoSectionTop = videoSection.offsetTop;

    // Smooth scroll to the video section
    window.scrollTo({
        top: videoSectionTop,
        behavior: 'smooth'
    });

    // Get the video element
    var video = document.getElementById("tutorialVideo");

    // Play the video
    video.play();
});

// Function to handle button click
document.getElementById("playButton").addEventListener("click", function() {
    // Get the video element
    var video = document.getElementById("tutorialVideo");
    
    // Play the video
    video.play();
});