// Corrected event listener to call revealContent function
// document.getElementById('clickToReveal').addEventListener('click', revealContent);

function revealContent() {
  var hiddenContent = document.getElementById('hiddenContent');
  var clickToReveal = document.getElementById('clickToReveal');
  console.log('0000000000000000')

  if (hiddenContent.style.display === 'none' || hiddenContent.style.display === '') {
    console.log('1111111111111111')
    // Show the hidden content
    hiddenContent.style.display = 'block';
    clickToReveal.textContent = 'Click again to hide content.';
  } else {
    console.log('2222222222222222')
    // Hide the content
    hiddenContent.style.display = 'none';
    clickToReveal.textContent = 'Click me to reveal content!';
  }
}
