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