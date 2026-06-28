// Function to trigger file input when clicking on upload container
function triggerFileInput() {
    document.getElementById('fileInput').click();
}

// Function to handle image selection
function handleImageSelection(event) {
    const file = event.target.files[0];
    if (file) {
        displayImage(file);
        // Show the result section immediately when image is selected
        document.getElementById('result').style.display = 'block';
        // Hide the guidelines
        document.getElementById('guidelines').style.display = 'none';
        // Clear previous prediction
        document.getElementById('prediction').textContent = '';
        document.getElementById('confidence').textContent = '';
    }
}

// Function to handle drag and drop
function allowDrop(event) {
    event.preventDefault();
}

function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
        displayImage(file);
        // Show the result section immediately when image is dropped
        document.getElementById('result').style.display = 'block';
        // Hide the guidelines
        document.getElementById('guidelines').style.display = 'none';
        // Clear previous prediction
        document.getElementById('prediction').textContent = '';
        document.getElementById('confidence').textContent = '';
    }
}

// Function to display selected image
function displayImage(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = document.getElementById('uploadedImage');
        img.src = e.target.result;
        img.style.display = 'block';
    };
    reader.readAsDataURL(file);
}

// Function to classify the image
function classifyImage() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select an image first');
        return;
    }

    // Show loading bar
    document.getElementById('loadingBar').style.display = 'block';
    
    const formData = new FormData();
    formData.append('image', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading bar
        document.getElementById('loadingBar').style.display = 'none';
        
        if (data.error) {
            alert('Error: ' + data.error);
            return;
        }

        // Display results
        document.getElementById('prediction').textContent = data.prediction;
        document.getElementById('confidence').textContent = data.confidence;
    })
    .catch(error => {
        document.getElementById('loadingBar').style.display = 'none';
        alert('Error: ' + error);
    });
}

// Function to toggle details section
function toggleDetails() {
    const details = document.getElementById('slidingDetails');
    const button = document.getElementById('seeMoreButton');
    
    if (details.style.display === 'block') {
        details.style.display = 'none';
        button.textContent = 'See More';
    } else {
        details.style.display = 'block';
        button.textContent = 'See Less';
    }
} 