async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  const chatBox = document.getElementById("chat-box");

  if (!message.trim()) return;

  chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
  input.value = "";

  const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  const botReply = data.response;
  chatBox.innerHTML += `<p><strong>Bot:</strong> ${botReply}</p>`;
  chatBox.scrollTop = chatBox.scrollHeight;

  // ✅ Speak the response aloud
  const utterance = new SpeechSynthesisUtterance(botReply);
  utterance.lang = "en-US"; // set language/accent
  speechSynthesis.speak(utterance);
}
