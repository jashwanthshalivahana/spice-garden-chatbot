from flask import Flask, request, jsonify
from groq import Groq

# YOUR API KEY
GROQ_API_KEY = "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"

app = Flask(__name__)
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are a helpful assistant for Spice Garden Restaurant, Hyderabad.
Hours: 11 AM - 11 PM daily. Location: Road No. 36, Jubilee Hills.
Specialties: Biryani, Kebabs, Haleem.
For reservations, ask for name and phone — say team confirms in 30 minutes.
Keep replies friendly, under 100 words, always in English unless asked."""

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Spice Garden — AI Chat</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0f0d0b;--surface:#1a1612;--card:#211e19;--border:#2e2820;
  --accent:#e8821a;--accent-light:#f5a94e;--text:#f0ebe3;--muted:#8a8070;
  --user-bg:#e8821a;--bot-bg:#2a2520;--radius:18px;
}
body{
  background:var(--bg);font-family:'DM Sans',sans-serif;color:var(--text);
  min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;
  background-image:radial-gradient(ellipse at 20% 50%,rgba(232,130,26,.06) 0%,transparent 60%),
                   radial-gradient(ellipse at 80% 20%,rgba(232,130,26,.04) 0%,transparent 50%);
}
.chat-wrapper{
  width:100%;max-width:480px;height:680px;background:var(--surface);
  border:1px solid var(--border);border-radius:24px;display:flex;
  flex-direction:column;overflow:hidden;
  box-shadow:0 32px 80px rgba(0,0,0,.6),0 0 0 1px rgba(232,130,26,.08);
}
.chat-header{
  background:var(--card);border-bottom:1px solid var(--border);
  padding:18px 22px;display:flex;align-items:center;gap:14px;
}
.logo{font-size:32px;line-height:1}
.header-text h1{font-family:'Playfair Display',serif;font-size:18px;color:var(--accent-light);line-height:1.2}
.header-text span{font-size:12px;color:var(--muted)}
.status-dot{
  width:9px;height:9px;background:#4ade80;border-radius:50%;margin-left:auto;
  box-shadow:0 0 8px rgba(74,222,128,.6);animation:pulse 2s ease-in-out infinite;
}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
.chat-messages{
  flex:1;overflow-y:auto;padding:20px 16px;display:flex;
  flex-direction:column;gap:12px;scrollbar-width:thin;scrollbar-color:var(--border) transparent;
}
.chat-messages::-webkit-scrollbar{width:4px}
.chat-messages::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
.message{display:flex;animation:fadeUp .25s ease-out}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.message.user{justify-content:flex-end}
.message.bot{justify-content:flex-start}
.bubble{max-width:78%;padding:12px 16px;border-radius:var(--radius);font-size:14px;line-height:1.55}
.message.user .bubble{background:var(--user-bg);color:#fff;border-bottom-right-radius:4px;font-weight:500}
.message.bot .bubble{background:var(--bot-bg);color:var(--text);border:1px solid var(--border);border-bottom-left-radius:4px}
.typing-indicator .bubble{display:flex;gap:5px;align-items:center;padding:14px 18px}
.typing-indicator .bubble span{
  width:7px;height:7px;background:var(--muted);border-radius:50%;
  animation:bounce 1.2s ease-in-out infinite;
}
.typing-indicator .bubble span:nth-child(2){animation-delay:.2s}
.typing-indicator .bubble span:nth-child(3){animation-delay:.4s}
@keyframes bounce{0%,80%,100%{transform:translateY(0);opacity:.5}40%{transform:translateY(-5px);opacity:1}}
.chat-input-area{
  border-top:1px solid var(--border);padding:14px 16px;
  display:flex;gap:10px;background:var(--card);
}
.chat-input-area input{
  flex:1;background:var(--bg);border:1px solid var(--border);border-radius:12px;
  padding:11px 16px;font-family:'DM Sans',sans-serif;font-size:14px;color:var(--text);
  outline:none;transition:border-color .2s;
}
.chat-input-area input::placeholder{color:var(--muted)}
.chat-input-area input:focus{border-color:var(--accent)}
.chat-input-area input:disabled{opacity:.5;cursor:not-allowed}
.chat-input-area button{
  width:44px;height:44px;background:var(--accent);border:none;border-radius:12px;
  color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:background .2s,transform .1s;flex-shrink:0;
}
.chat-input-area button:hover{background:var(--accent-light)}
.chat-input-area button:active{transform:scale(.95)}
.chat-input-area button:disabled{opacity:.4;cursor:not-allowed;transform:none}
@media(max-width:520px){
  body{padding:0;align-items:flex-end}
  .chat-wrapper{height:100vh;max-width:100%;border-radius:0}
}
</style>
</head>
<body>
<div class="chat-wrapper">
  <div class="chat-header">
    <div class="logo">&#127859;</div>
    <div class="header-text">
      <h1>Spice Garden</h1>
      <span>Jubilee Hills, Hyderabad &middot; Ask me anything</span>
    </div>
    <div class="status-dot"></div>
  </div>
  <div class="chat-messages" id="chatMessages">
    <div class="message bot">
      <div class="bubble">Welcome to Spice Garden! &#127798;&#65039; I can help with our menu, timings, specialties, or reservations. How can I assist you today?</div>
    </div>
  </div>
  <div class="chat-input-area">
    <input type="text" id="userInput" placeholder="Ask about menu, hours, or book a table..." autocomplete="off"/>
    <button id="sendBtn" onclick="sendMessage()">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
        <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
      </svg>
    </button>
  </div>
</div>
<script>
const input = document.getElementById('userInput');
const messagesDiv = document.getElementById('chatMessages');

input.addEventListener('keydown', e => { if(e.key==='Enter') sendMessage(); });

function appendMessage(text, sender) {
  const div = document.createElement('div');
  div.className = 'message ' + sender;
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.textContent = text;
  div.appendChild(bubble);
  messagesDiv.appendChild(div);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function showTyping() {
  const div = document.createElement('div');
  div.className = 'message bot typing-indicator';
  div.id = 'typingIndicator';
  div.innerHTML = '<div class="bubble"><span></span><span></span><span></span></div>';
  messagesDiv.appendChild(div);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function removeTyping() {
  const el = document.getElementById('typingIndicator');
  if(el) el.remove();
}

async function sendMessage() {
  const msg = input.value.trim();
  if(!msg) return;
  appendMessage(msg, 'user');
  input.value = '';
  input.disabled = true;
  document.getElementById('sendBtn').disabled = true;
  showTyping();
  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: msg})
    });
    const data = await res.json();
    removeTyping();
    if (data.reply) {
      appendMessage(data.reply, 'bot');
    } else {
      appendMessage('Error: ' + (data.error || 'Unknown error'), 'bot');
    }
  } catch(err) {
    removeTyping();
    appendMessage('Network error: ' + err.message, 'bot');
  } finally {
    input.disabled = false;
    document.getElementById('sendBtn').disabled = false;
    input.focus();
  }
}
</script>
</body>
</html>"""

@app.route('/')
def home():
    return HTML

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400
    msg = data.get('message', '').strip()
    if not msg:
        return jsonify({'error': 'Empty message'}), 400
    try:
        print(f"[DEBUG] Sending to Groq: {msg}")
        print(f"[DEBUG] API key starts with: {GROQ_API_KEY[:10]}...")
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": msg}
            ],
            max_tokens=200
        )
        reply = res.choices[0].message.content
        print(f"[DEBUG] Got reply: {reply[:50]}")
        return jsonify({'reply': reply})
    except Exception as e:
        print(f"[ERROR] Groq failed: {type(e).__name__}: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
