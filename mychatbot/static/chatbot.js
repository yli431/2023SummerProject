const chatboxMessageWrapper = document.querySelector('.chatbox-message-content')


const checkHistoryUrl = '/mychatbot/chat_history/';
fetch(checkHistoryUrl, {
      method: 'GET',
      headers: {
      },
  }).then(response => {
      response.json().then(data => {
        renderHistory(data.history);
      })
  });
  function renderHistory(history) {
    for (let i=0; i < history.length; i++) {
      if (i % 2 === 0) {
        let question_text = `
        <div class="chatbox-message-item sent">
          <span class="chatbox-message-item-text">
            ${history[i]}
          </span>
        </div>`
        chatboxMessageWrapper.insertAdjacentHTML('beforeend', question_text);
      } else {
        let answer_text = `
        <div class="chatbox-message-item received">
          <span class="chatbox-message-item-text">
            ${history[i]}
          </span>
        </div>`
        chatboxMessageWrapper.insertAdjacentHTML('beforeend', answer_text);
        scrollBottom()
      }
    }
  }


// MESSAGE INPUT
  const textarea = document.querySelector('.chatbox-message-input')
  const chatboxForm = document.querySelector('.chatbox-message-form')

  textarea.addEventListener('input', function () {
    let line = textarea.value.split('\n').length

    if(textarea.rows < 6 || line < 6) {
      textarea.rows = line
    }

    if(textarea.rows > 1) {
      chatboxForm.style.alignItems = 'flex-end'
    } else {
      chatboxForm.style.alignItems = 'center'
    }
  })

  // TOGGLE CHATBOX
  const chatboxToggle = document.querySelector('.chatbox-toggle')
  const chatboxClose = document.querySelector('.chatbot-close')
  const chatboxMessage = document.querySelector('.chatbox-message-wrapper')

  chatboxToggle.addEventListener('click', function () {
    chatboxMessage.classList.toggle('show')
  })
  chatboxClose.addEventListener('click', function () {
    chatboxMessage.classList.toggle('show')
  })

  // CHATBOX MESSAGE
  const chatboxNoMessage = document.querySelector('.chatbox-message-no-message')

  chatboxForm.addEventListener('submit', function (e) {
    e.preventDefault()

    if(isValid(textarea.value)) {
      writeMessage()
    }
  })



  function addZero(num) {
    return num < 10 ? '0'+num : num
  }

  function writeMessage() {
    const today = new Date()
    let message = `
      <div class="chatbox-message-item sent">
        <span class="chatbox-message-item-text">
          ${textarea.value.trim().replace(/\n/g, '<br>\n')}
        </span>
        <span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
      </div>
    `

    const textarea_value_backup = textarea.value.trim().replace(/\n/g, '<br>\n')
    chatboxMessageWrapper.insertAdjacentHTML('beforeend', message)
    textarea.value = ''
    textarea.focus()
    chatboxForm.style.alignItems = 'center'
    textarea.rows = 1
    chatboxNoMessage.style.display = 'none'
    scrollBottom()

    const internalUrl = '/mychatbot/mychatbot/';
    const url = `${internalUrl}?ai_question=${textarea_value_backup}`;

    fetch(url, {
        method: 'GET',
        headers: {
        },
    }).then(response => {
        response.json().then(data => {
          autoReply(data.ai_response);
        })
    });

  }

  function autoReply(response_message) {
    const today = new Date()
    let message = `
      <div class="chatbox-message-item received">
        <span class="chatbox-message-item-text">
          ${response_message}
        </span>
        <span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
      </div>
    `
    chatboxMessageWrapper.insertAdjacentHTML('beforeend', message)
    scrollBottom()
  }

  function scrollBottom() {
    chatboxMessageWrapper.scrollTo(0, chatboxMessageWrapper.scrollHeight)
  }

  function isValid(value) {
    let text = value.replace(/\n/g, '')
    text = text.replace(/\s/g, '')

    return text.length > 0
  }
