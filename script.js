function btn(name) {
    alert("زر " + name + " اشتغل 👍");
}

// مثال: فتح الميزات المستقبلية بعد 5 ثواني
setTimeout(() => {
    document.getElementById("future-features").style.display = "block";
}, 5000);
// تحديث حالة البوت عشوائي للتجربة
const statuses = ["متصل", "غير متصل", "مشغول", "قريبًا"];
document.getElementById("bot-status").innerText = statuses[Math.floor(Math.random() * statuses.length)];
function sendMessage() {
  const input = document.getElementById("userInput");
  const msg = input.value.trim();
  if (!msg) return;

  addMessage(msg, "user");
  input.value = "";

  let found = false;

  for (let item of knowledgeBase) {
    if (
      item.title.includes(msg) ||
      item.keywords.some(k => msg.includes(k))
    ) {
      addMessage(item.content, "bot");
      found = true;
      break;
    }
  }

  if (!found) {
    addMessage("حالياً ما عندي جواب، سيتم إضافة المعلومة قريباً 🌚", "bot");
  }
}

function addMessage(text, type) {
  const box = document.getElementById("hyper-messages");
  const div = document.createElement("div");
  div.className = type;
  div.textContent = text;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}