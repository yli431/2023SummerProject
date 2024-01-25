function addQuestionMark() {
    // Find the target element by its ID
    var targetElement = document.getElementById('myselfstarget');

    if (targetElement) {
        // Add a question mark to the end of the element's text content
        targetElement.textContent += '?';
    } else {
        console.error('Target element not found!');
    }
};


let clicked_times = 0;

function countClickedTimes() {

//   var targetElement2 = document.getElementById('num2target');
    var clickCountElement = document.getElementById('clickCount');

    if (clickCountElement) {
        clicked_times++;

        clickCountElement.textContent = clicked_times;

        console.log('Clicked ' + clicked_times + ' times');
    }
    else {
        console.error('Something wrong happened.');
    }

  return clicked_times;
}

