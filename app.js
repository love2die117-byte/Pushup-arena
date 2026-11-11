window.state = {
  userName: "Kayden",
  heroClass: "Vanguard",
  age: 20,
  weight: 140,
  maxReps: 15,
  aiTargetReps: 18,
  gold: 250,
  gems: 25,
  themeColor: "#38bdf8",
  totalReps: 0,
  enemiesDefeated: 0,
  sRanksAchieved: 0,
  currentReps: 0,
  routineFormat: "cycle",
  selectedTypes: ["standard", "diamond"],
  formStrictness: "standard",
  unlockedChapter: 1,
  unlockedLevel: 1,
  campaignProgress: {},
  signedIn: false,
  photoURL: ""
};

window.storyChapters = [
  {
    id: 1,
    name: "Whispering Crypts",
    desc: "Awaken your core strength amidst decaying catacombs.",
    bosses: [
      { name: "Undead Warden", reps: 15 },
      { name: "Skeletal Vanguard", reps: 18 },
      { name: "Crypt Ghoul Lord", reps: 20 },
      { name: "Banshee of Sorrows", reps: 22 },
      { name: "Lich King Malakor", reps: 25 }
    ]
  },
  {
    id: 2,
    name: "Sunken Obsidian Citadel",
    desc: "Molten chambers testing lower-body and core endurance.",
    bosses: [
      { name: "Magma Golem", reps: 25 },
      { name: "Obsidian Knight", reps: 28 },
      { name: "Flame Pyromancer", reps: 30 },
      { name: "Cinder Drake", reps: 35 },
      { name: "Ignis Titan", reps: 40 }
    ]
  },
  {
    id: 3,
    name: "Celestial Spire",
    desc: "Ascend into the divine clouds where form precision is absolute.",
    bosses: [
      { name: "Acolyte of Light", reps: 35 },
      { name: "Solar Guardian", reps: 40 },
      { name: "Astral Valkyrie", reps: 45 },
      { name: "Seraphim Sentinel", reps: 50 },
      { name: "Archangel Michael", reps: 60 }
    ]
  }
];

let currentSlide = 1;
const totalSlides = 5;

function loginWithGoogle() {
  window.signInWithPopup(window.firebaseAuth, window.firebaseProvider)
    .catch((error) => {
      alert("Google Sign-In Error: " + error.message);
    });
}

function selectHeroClass(className, colorHex) {
  window.state.heroClass = className;
  window.state.themeColor = colorHex;
  document.querySelectorAll('.class-card').forEach(c => c.classList.remove('selected'));
  if (className === 'Vanguard') {
    const el = document.getElementById('class-vanguard');
    if (el) el.classList.add('selected');
  } else {
    const el = document.getElementById('class-berserker');
    if (el) el.classList.add('selected');
  }
  updateThemeColor(colorHex);
}

function postLoginInit() {
  runAiTargetCalculation();
  document.getElementById('header-gold-val').innerText = window.state.gold;
  document.getElementById('header-gems-val').innerText = window.state.gems;
  document.getElementById('header-user-name').innerText = window.state.userName;

  const lvlEl = document.getElementById('header-user-level');
  if (lvlEl) lvlEl.innerText = `${window.state.heroClass || "Vanguard"} Knight`;

  const avatarEl = document.getElementById('avatar');
  if (window.state.photoURL) {
    avatarEl.innerHTML = `<img src="${window.state.photoURL}" alt="Avatar">`;
  } else {
    avatarEl.innerText = window.state.userName.charAt(0).toUpperCase();
  }

  document.getElementById('account-name-input').value = window.state.userName;
  document.getElementById('account-age-input').value = window.state.age;
  document.getElementById('account-weight-input').value = window.state.weight;
  document.getElementById('account-max-reps-input').value = window.state.maxReps;

  updateStatsDisplay();
  renderStoryCampaignMap();
  drawPixelHelmet();
}

function renderStoryCampaignMap() {
  const container = document.getElementById('campaign-map-container');
  if(!container) return;
  container.innerHTML = "";

  window.storyChapters.forEach((chap) => {
    let html = `
      <div class="chapter-card">
        <div class="chapter-title">Chapter ${chap.id}: ${chap.name}</div>
        <p style="color:var(--subtext); font-size:0.8rem;">${chap.desc}</p>
        <div class="levels-grid">
    `;

    chap.bosses.forEach((boss, idx) => {
      let lvlNum = idx + 1;
      let isUnlocked = chap.id < window.state.unlockedChapter || (chap.id === window.state.unlockedChapter && lvlNum <= window.state.unlockedLevel);
      let rank = window.state.campaignProgress[chap.id]?.[lvlNum] || "-";
      let nodeClass = isUnlocked ? (rank !== "-" ? "level-node completed" : "level-node unlocked") : "level-node";

      html += `
        <div class="${nodeClass}" ${isUnlocked ? `onclick="startCampaignLevel(${chap.id}, ${lvlNum})"` : ''}>
          <div class="level-node-num">${chap.id}-${lvlNum}</div>
          <div class="level-node-rank">${rank}</div>
        </div>
      `;
    });

    html += `</div></div>`;
    container.innerHTML += html;
  });
}

function runAiTargetCalculation() {
  let base = parseInt(window.state.maxReps) || 15;
  window.state.aiTargetReps = Math.max(10, Math.round(base * 1.2));
  const goalTitle = document.getElementById('hero-goal-title');
  const goalDesc = document.getElementById('hero-goal-desc');
  if(goalTitle) goalTitle.innerText = `Chapter ${window.state.unlockedChapter} Raid`;
  if(goalDesc) goalDesc.innerText = `AI tailored target: ${window.state.aiTargetReps} Reps per wave.`;
}

function recalculateAiGoals() {
  window.state.age = parseInt(document.getElementById('account-age-input').value) || 20;
  window.state.weight = parseInt(document.getElementById('account-weight-input').value) || 140;
  window.state.maxReps = parseInt(document.getElementById('account-max-reps-input').value) || 15;
  runAiTargetCalculation();
  saveState();
}

function togglePushupType(typeKey) {
  const idx = window.state.selectedTypes.indexOf(typeKey);
  if (idx > -1) {
    if (window.state.selectedTypes.length > 1) window.state.selectedTypes.splice(idx, 1);
  } else {
    window.state.selectedTypes.push(typeKey);
  }
  syncTypePillsUI();
  saveState();
}

function syncTypePillsUI() {
  ['standard', 'diamond', 'wide', 'decline'].forEach(t => {
    const el = document.getElementById(`type-${t}`);
    if (el) el.classList.toggle('selected', window.state.selectedTypes.includes(t));
  });
}

function saveStrictnessSetting() {
  window.state.formStrictness = document.getElementById('form-strictness-select').value;
  saveState();
}

function saveRoutineSettings() {
  window.state.routineFormat = document.getElementById('routine-format-select').value;
  saveState();
}

function switchTab(tabName) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.sub-screen').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));

  if (tabName === 'home') {
    document.getElementById('home-screen').classList.add('active');
    document.getElementById('nav-home').classList.add('active');
  } else if (tabName === 'story') {
    document.getElementById('story-screen').classList.add('active');
    document.getElementById('nav-story').classList.add('active');
    renderStoryCampaignMap();
  } else if (tabName === 'types') {
    document.getElementById('types-screen').classList.add('active');
    document.getElementById('nav-types').classList.add('active');
  } else if (tabName === 'stats') {
    document.getElementById('stats-screen').classList.add('active');
    document.getElementById('nav-stats').classList.add('active');
    updateStatsDisplay();
  } else if (tabName === 'account') {
    document.getElementById('account-screen').classList.add('active');
    document.getElementById('nav-account').classList.add('active');
  } else if (tabName === 'leaderboard') {
    document.getElementById('leaderboard-screen').classList.add('active');
    document.getElementById('nav-leaderboard').classList.add('active');
    renderLeaderboard();
  }
}

function updateStatsDisplay() {
  document.getElementById('stats-total-reps').innerText = window.state.totalReps;
  document.getElementById('stats-enemies-killed').innerText = window.state.enemiesDefeated;
  document.getElementById('stats-s-ranks').innerText = window.state.sRanksAchieved;
  document.getElementById('header-gold-val').innerText = window.state.gold;
  document.getElementById('header-gems-val').innerText = window.state.gems;
}

function updateAccountName(val) {
  window.state.userName = val || "Kayden";
  document.getElementById('header-user-name').innerText = window.state.userName;
  document.getElementById('avatar').innerText = window.state.userName.charAt(0).toUpperCase();
  saveState();
}

function updateSlideUI() {
  for (let i = 1; i <= totalSlides; i++) {
    const sEl = document.getElementById(`slide-${i}`);
    const pEl = document.getElementById(`p-step-${i}`);
    if (sEl) sEl.classList.toggle('active', i === currentSlide);
    if (pEl) pEl.classList.toggle('active', i <= currentSlide);
  }
  const backBtn = document.getElementById('back-btn');
  const nextBtn = document.getElementById('next-btn');
  if (backBtn) backBtn.style.display = currentSlide === 1 ? 'none' : 'block';
  if (nextBtn) nextBtn.innerText = currentSlide === totalSlides ? 'Enter Realm' : 'Next';
}

function nextSlide() {
  if (currentSlide < totalSlides) {
    currentSlide++;
    updateSlideUI();
  } else {
    completeOnboarding();
  }
}

function prevSlide() {
  if (currentSlide > 1) {
    currentSlide--;
    updateSlideUI();
  }
}

function completeOnboarding() {
  window.state.userName = document.getElementById('signup-name').value || "Kayden";
  window.state.age = parseInt(document.getElementById('signup-age').value) || 20;
  window.state.weight = parseInt(document.getElementById('signup-weight').value) || 140;
  window.state.maxReps = parseInt(document.getElementById('signup-max-reps').value) || 15;

  const strictEl = document.getElementById('signup-strictness');
  if (strictEl) window.state.formStrictness = strictEl.value;

  document.getElementById('onboarding-modal').classList.remove('active');
  saveState();
  postLoginInit();
}

function triggerSignOut() {
  window.signOut(window.firebaseAuth).then(() => {
    location.reload();
  });
}

function updateThemeColor(hex) {
  window.state.themeColor = hex;
  document.documentElement.style.setProperty('--primary', hex);
  document.documentElement.style.setProperty('--primary-glow', hex + '55');
  saveState();
  drawPixelHelmet();
}

function drawPixelHelmet() {
  const cvs = document.getElementById('helmet-canvas');
  if(!cvs) return;
  const ctx = cvs.getContext('2d');
  ctx.fillStyle = window.state.themeColor || "#38bdf8";
  ctx.fillRect(16, 8, 32, 12);
  ctx.fillRect(12, 20, 40, 32);
  ctx.fillStyle = "#0a0b0e";
  ctx.fillRect(20, 28, 24, 8);
}

function saveState() {
  const user = window.firebaseAuth.currentUser;
  const key = user ? 'pushup_realm_state_' + user.uid : 'pushup_realm_state_guest';
  localStorage.setItem(key, JSON.stringify(window.state));
}

function openArmory() {
  alert(`🛡️ ARMORY & ARTIFACT SHOP\nGold: 🪙 ${window.state.gold} | Gems: 💎 ${window.state.gems}\n\nLegendary Gear Unlocked!`);
}

function renderLeaderboard() {
  const container = document.getElementById('leaderboard-list-container');
  if(!container) return;
  container.innerHTML = `
    <div class="setting-item" style="flex-direction: row; justify-content: space-between;">
      <div><strong>1. ${window.state.userName} (You)</strong></div>
      <div style="color:var(--rank-s); font-weight:900;">👑 SSS Ranks: ${window.state.sRanksAchieved}</div>
    </div>
  `;
}

window.onload = () => {
  drawPixelHelmet();
  let progress = 0;
  const interval = setInterval(() => {
    progress += 25;
    const pBar = document.getElementById('loading-progress');
    if (pBar) pBar.style.width = progress + '%';
    if (progress >= 100) {
      clearInterval(interval);
      const lScreen = document.getElementById('loading-screen');
      if (lScreen) {
        lScreen.style.opacity = '0';
        setTimeout(() => { lScreen.style.display = 'none'; }, 300);
      }
    }
  }, 80);
};

window.loginWithGoogle = loginWithGoogle;
window.selectHeroClass = selectHeroClass;
window.postLoginInit = postLoginInit;
window.recalculateAiGoals = recalculateAiGoals;
window.togglePushupType = togglePushupType;
window.saveRoutineSettings = saveRoutineSettings;
window.saveStrictnessSetting = saveStrictnessSetting;
window.switchTab = switchTab;
window.updateAccountName = updateAccountName;
window.updateSlideUI = updateSlideUI;
window.nextSlide = nextSlide;
window.prevSlide = prevSlide;
window.triggerSignOut = triggerSignOut;
window.updateThemeColor = updateThemeColor;
window.openArmory = openArmory;
window.saveState = saveState;
