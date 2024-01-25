// Corrected event listener to call revealContent function
// document.getElementById('clickToReveal').addEventListener('click', revealContent);

function revealContent() {
  var hiddenContent = document.getElementById('hiddenContent');
  var clickToReveal = document.getElementById('clickToReveal');

  if (hiddenContent.style.display === 'none' || hiddenContent.style.display === '') {
    // Show the hidden content
    hiddenContent.style.display = 'block';
    clickToReveal.textContent = 'Click again to hide content.';
  } else {
    // Hide the content
    hiddenContent.style.display = 'none';
    clickToReveal.textContent = 'Click me to reveal content!';
  }
}
