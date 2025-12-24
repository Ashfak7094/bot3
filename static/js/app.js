// ===== BOT TOGGLE =====
function toggleBot() {
    const status = document.getElementById("bot-status");
    if (status.innerText === "OFF") {
        status.innerText = "ON";
        status.className = "status-on";
    } else {
        status.innerText = "OFF";
        status.className = "status-off";
    }
}

// ===== COPY REFERRAL =====
function copyReferral(id) {
    const text = document.getElementById(id).innerText;
    navigator.clipboard.writeText(text);
    alert("Referral link copied!");
}

// ===== GAS ALERT =====
function gasAlert(gas) {
    if (gas < 0.5) {
        alert("⚠️ Low Gas! Bot stopped automatically.");
    }
}

// ===== FAKE LIVE EFFECT (UI ONLY) =====
setInterval(() => {
    const el = document.getElementById("live-price");
    if (!el) return;
    let price = parseFloat(el.innerText);
    let change = (Math.random() * 0.2 - 0.1).toFixed(2);
    el.innerText = (price + parseFloat(change)).toFixed(2);
}, 1500);

// ===== MENU TOGGLE =====
function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}
