function sendMessage() {
  const input = document.getElementById('userInput');
  const message = input.value.trim();
  if (!message) return;

  appendToChat("You: " + message);
  input.value = "";

  fetch('/get-response', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: message})
  })
  .then(res => res.json())
  .then(data => {
    appendToChat("Bot: " + data.response);
  });
}

function appendToChat(msg) {
  const log = document.getElementById('chatLog');
  log.innerHTML += `<div>${msg}</div>`;
  log.scrollTop = log.scrollHeight;
}
