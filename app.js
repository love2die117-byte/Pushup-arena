window.state = {
  userName: "Kayden",
  age: 20,
  weight: 140,
  maxReps: 15,
  aiTargetReps: 18,
  gold: 150,
  themeColor: "#38bdf8",
  totalReps: 0,
  enemiesDefeated: 0,
  bossesSlain: 0,
  currentReps: 0,
  routineFormat: "cycle",
  selectedTypes: ["standard", "diamond"],
  storyStage: 1,
  signedIn: false,
  photoURL: ""
};

let currentSlide = 1;
const totalSlides = 4;

function loginWithGoogle() {
  window.signInWithPopup(window.firebaseAuth, window.firebaseProvider)
    .catch((error) => {
      alert("Google Sign-In Error: " + error.message);
    });
}

function postLoginInit() {
  runAiTargetCalculation();
  updateThemeColor(window.state.themeColor);
  document.getElementById('header-gold-val').innerText = window.state.gold;
  document.getElementById('header-user-name').innerText = window.state.userName;

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
  document.getElementById('ai-target-reps-input').value = window.state.aiTargetReps;

  updateStatsDisplay();
  drawPixelHelmet();
}

function runAiTargetCalculation() {
  let base = parseInt(window.state.maxReps) || 15;
  let ageFactor = window.state.age < 25 ? 1.2 : (window.state.age > 40 ? 0.9 : 1.1);
  let weightFactor = window.state.weight > 180 ? 0.95 : 1.05;

  let calculated = Math.round(base * 1.2 * ageFactor * weightFactor);
  window.state.aiTargetReps = Math.max(5, calculated);

  document.getElementById('header-user-level').innerText = `AI Goal: ${window.state.aiTargetReps} Reps`;
  document.getElementById('hero-goal-title').innerText = `Target: ${window.state.aiTargetReps} Reps / Wave`;
  document.getElementById('hero-goal-desc').innerText = `AI calibrated for ${window.state.userName} (Max baseline: ${base}).`;
}

function recalculateAiGoals() {
  window.state.age = parseInt(document.getElementById('account-age-input').value) || 20;
  window.state.weight = parseInt(document.getElementById('account-weight-input').value) || 140;
  window.state.maxReps = parseInt(document.getElementById('account-max-reps-input').value) || 15;
  runAiTargetCalculation();
  saveState();
}

function updateAiTargetReps(val) {
  window.state.aiTargetReps = parseInt(val) || 18;
  document.getElementById('header-user-level').innerText = `AI Goal: ${window.state.aiTargetReps} Reps`;
  document.getElementById('hero-goal-title').innerText = `Target: ${window.state.aiTargetReps} Reps / Wave`;
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
  } else if (tabName === 'settings') {
    document.getElementById('settings-screen').classList.add('active');
    document.getElementById('nav-settings').classList.add('active');
  } else if (tabName === 'leaderboard') {
    document.getElementById('leaderboard-screen').classList.add('active');
    document.getElementById('nav-leaderboard').classList.add('active');
    renderLeaderboard();
  }
}

function updateStatsDisplay() {
  document.getElementById('stats-total-reps').innerText = window.state.totalReps;
  document.getElementById('stats-enemies-killed').innerText = window.state.enemiesDefeated;
  document.getElementById('stats-bosses-slain').innerText = window.state.bossesSlain;
  document.getElementById('header-gold-val').innerText = window.state.gold;
}

function updateAccountName(val) {
  window.state.userName = val || "Kayden";
  document.getElementById('header-user-name').innerText = window.state.userName;
  document.getElementById('avatar').innerText = window.state.userName.charAt(0).toUpperCase();
  runAiTargetCalculation();
  saveState();
}

function updateSlideUI() {
  for (let i = 1; i <= totalSlides; i++) {
    document.getElementById(`slide-${i}`).classList.toggle('active', i === currentSlide);
    document.getElementById(`p-step-${i}`).classList.toggle('active', i <= currentSlide);
  }
  document.getElementById('back-btn').style.display = currentSlide === 1 ? 'none' : 'block';
  document.getElementById('next-btn').innerText = currentSlide === totalSlides ? 'Finish & Start' : 'Next';
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

  document.getElementById('onboarding-modal').classList.remove('active');
  saveState();
  postLoginInit();
}

function triggerSignOut() {
  window.signOut(window.firebaseAuth).then(() => {
    location.reload();
  });
}

function drawPixelHelmet() {
  const cvs = document.getElementById('helmet-canvas');
  const ctx = cvs.getContext('2d');
  ctx.fillStyle = window.state.themeColor || "#38bdf8";
  ctx.fillRect(16, 8, 32, 12);
  ctx.fillRect(12, 20, 40, 32);
  ctx.fillStyle = "#0a0b0e";
  ctx.fillRect(20, 28, 24, 8);
}

function updateThemeColor(hex) {
  window.state.themeColor = hex;
  document.documentElement.style.setProperty('--primary', hex);
  document.documentElement.style.setProperty('--primary-glow', hex + '55');
  saveState();
  drawPixelHelmet();
}

function saveState() {
  const user = window.firebaseAuth.currentUser;
  const key = user ? 'pushup_arena_state_' + user.uid : 'pushup_arena_state_guest';
  localStorage.setItem(key, JSON.stringify(window.state));
}

function resetAllData() {
  if (confirm("Are you sure you want to reset all app stats and progress?")) {
    const user = window.firebaseAuth.currentUser;
    const key = user ? 'pushup_arena_state_' + user.uid : 'pushup_arena_state_guest';
    localStorage.removeItem(key);
    location.reload();
  }
}

function openStoryCampaign() {
  if (confirm(`📜 STORY CAMPAIGN\nCurrent Stage: ${window.state.storyStage}\n\nEnter battle?`)) {
    window.startArena('story');
  }
}

function openArmory() {
  alert(`🛡️ HERO ARMORY\nYour Gold: 🪙 ${window.state.gold}`);
}

function renderLeaderboard() {
  const container = document.getElementById('leaderboard-list-container');
  container.innerHTML = `
    <div class="setting-item" style="flex-direction: row; justify-content: space-between;">
      <div><strong>${window.state.userName} (You)</strong></div>
      <div>💪 ${window.state.totalReps} Reps</div>
    </div>
  `;
}

window.onload = () => {
  drawPixelHelmet();
  let progress = 0;
  const interval = setInterval(() => {
    progress += 25;
    document.getElementById('loading-progress').style.width = progress + '%';
    if (progress >= 100) {
      clearInterval(interval);
      document.getElementById('loading-screen').style.opacity = '0';
      setTimeout(() => { document.getElementById('loading-screen').style.display = 'none'; }, 300);
    }
  }, 80);
};

window.loginWithGoogle = loginWithGoogle;
window.postLoginInit = postLoginInit;
window.recalculateAiGoals = recalculateAiGoals;
window.updateAiTargetReps = updateAiTargetReps;
window.togglePushupType = togglePushupType;
window.saveRoutineSettings = saveRoutineSettings;
window.switchTab = switchTab;
window.updateAccountName = updateAccountName;
window.updateSlideUI = updateSlideUI;
window.nextSlide = nextSlide;
window.prevSlide = prevSlide;
window.triggerSignOut = triggerSignOut;
window.updateThemeColor = updateThemeColor;
window.resetAllData = resetAllData;
window.openStoryCampaign = openStoryCampaign;
window.openArmory = openArmory;
window.saveState = saveState;
