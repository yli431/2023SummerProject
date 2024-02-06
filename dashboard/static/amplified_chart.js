
const chartAmplify = document.querySelector('.icon-block') 
chartAmplify.addEventListener('click', function () {
    amplifyChart('mortgage_rate');
});


function amplifyChart(chartId) {
    // Get the chart canvas element
    var chartCanvas = document.getElementById(chartId);

    // Clone the chart content
    var chartContent = chartCanvas.cloneNode(true);

    // Get the amplified chart container
    var amplifiedContainer = document.getElementById('amplifiedChart');

    // Clear previous content
    amplifiedContainer.innerHTML = '';

    // Set the content of the amplified chart container
    amplifiedContainer.appendChild(chartContent);

    // Display the amplified chart container
    amplifiedContainer.style.display = 'block';
  }