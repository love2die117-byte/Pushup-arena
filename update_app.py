import os

# All modular code files and their updated contents
files = {
    "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Push Up Arena: The Iron Oath (S-RANK MASTERY)</title>
  <meta name="app-version" content="v20.0-ultimate-revamp">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#0a0b0e">
  <link rel="stylesheet" href="style.css">

  <!-- MediaPipe Pose & Camera Utils -->
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/pose/pose.js" crossorigin="anonymous"></script>
</head>
<body>

  <!-- Cinematic Loading Screen -->
  <div id="loading-screen">
    <canvas id="helmet-canvas" width="64" height="64" class="helmet-logo"></canvas>
    <div class="loading-title">The Iron Oath</div>
    <div class="loading-sub">Forging Legend Status...</div>
    <div class="progress-bar-bg">
      <div id="loading-progress" class="progress-bar-fill"></div>
    </div>
  </div>

  <!-- App Header Bar -->
  <div class="app-header">
    <div class="user-pill" onclick="switchTab('account')" style="cursor: pointer;">
      <div id="avatar" class="user-avatar">K</div>
      <div>
        <div id="header-user-name" style="font-weight: 900; font-size: 1rem;">Kayden</div>
        <div id="header-user-level" style="font-size: 0.75rem; color: var(--primary); font-weight: 800;">Level 1 Novice</div>
      </div>
    </div>
    <div style="display: flex; gap: 8px; align-items: center;">
      <div class="currency-badge">💎 <span id="header-gems-val">25</span></div>
      <div class="currency-badge">🪙 <span id="header-gold-val">250</span></div>
    </div>
  </div>

  <!-- SCREEN 1: HOME / HUB -->
  <div id="home-screen" class="screen active">
    <div class="menu-content">
      <div class="hero-banner">
        <div class="hero-tag">⚔️ DAILY CAMPAIGN RIFT</div>
        <div class="hero-title" id="hero-goal-title">Chapter 1: Whispering Crypts</div>
        <div class="hero-sub" id="hero-goal-desc">Defeat the Undead Warden to unlock Chapter 2. Form strictness: Standard.</div>
        <button class="btn" onclick="startCampaignLevel(1, 1)">⚔️ CONTINUE QUEST</button>
      </div>

      <div class="modes-grid">
        <div class="mode-card" onclick="switchTab('story')">
          <div class="mode-icon-box">📜</div>
          <div class="mode-info">
            <div class="mode-title">Story Campaign Map</div>
            <div class="mode-desc">5 Chapters, 25 Boss Dungeons, and S-Rank Evaluation Medals.</div>
          </div>
          <div class="mode-action-pill">MAP</div>
        </div>

        <div class="mode-card" onclick="startArena('quick')">
          <div class="mode-icon-box">👹</div>
          <div class="mode-info">
            <div class="mode-title">Quick Raid Arena</div>
            <div class="mode-desc">Instant training mode against randomized tier monsters.</div>
          </div>
          <div class="mode-action-pill">FIGHT</div>
        </div>

        <div class="mode-card" onclick="startArena('endless')">
          <div class="mode-icon-box">💀</div>
          <div class="mode-info">
            <div class="mode-title">Endless Abyss Survival</div>
            <div class="mode-desc">Infinite scaling waves. Earn multiplier gold per rep.</div>
          </div>
          <div class="mode-action-pill" style="background:#1c1f2b; color:#fff;">SURVIVE</div>
        </div>

        <div class="mode-card" onclick="openArmory()">
          <div class="mode-icon-box">🛡️</div>
          <div class="mode-info">
            <div class="mode-title">Armory & Artifact Shop</div>
            <div class="mode-desc">Equip legendary helmets, chest plates, and passive stat auras.</div>
          </div>
          <div class="mode-action-pill" style="background:#1c1f2b; color:#fff;">GEAR</div>
        </div>
      </div>
    </div>
  </div>

  <!-- SCREEN 2: STORY CAMPAIGN MAP -->
  <div id="story-screen" class="sub-screen">
    <div class="screen-header-title">🗺️ The Iron Campaign Map</div>
    <div class="campaign-chapters-container" id="campaign-map-container"></div>
  </div>

  <!-- SCREEN 3: ROUTINE & PUSH-UP TYPES -->
  <div id="types-screen" class="sub-screen">
    <div class="screen-header-title">🔄 Combat Techniques & Routine</div>
    <div class="settings-list">
      <div class="setting-item">
        <label>Set Progression Format</label>
        <select id="routine-format-select" onchange="saveRoutineSettings()">
          <option value="single">Single Form Specialization</option>
          <option value="cycle" selected>Dynamic Form Cycle (Mix Styles per Set)</option>
        </select>
      </div>

      <div class="setting-item">
        <label>Active Push-up Combat Styles</label>
        <div class="type-pill-grid">
          <div class="type-pill selected" id="type-standard" onclick="togglePushupType('standard')">Standard Strike (+1x)</div>
          <div class="type-pill" id="type-diamond" onclick="togglePushupType('diamond')">Diamond Focus (+1.5x Dmg)</div>
          <div class="type-pill" id="type-wide" onclick="togglePushupType('wide')">Wide Vanguard (+1.2x AoE)</div>
          <div class="type-pill" id="type-decline" onclick="togglePushupType('decline')">Decline Crusher (+2x Crit)</div>
        </div>
      </div>

      <div class="setting-item">
        <label>AI Form Strictness Filter</label>
        <select id="form-strictness-select" onchange="saveStrictnessSetting()">
          <option value="lenient">Lenient (90° Elbow Threshold)</option>
          <option value="standard" selected>Standard Vanguard (85° Threshold)</option>
          <option value="master">S-Rank Elite (75° Deep Chest Touch)</option>
        </select>
      </div>
    </div>
  </div>

  <!-- SCREEN 4: HERO STATS -->
  <div id="stats-screen" class="sub-screen">
    <div class="screen-header-title">📊 Hero Combat Analytics</div>
    <div class="stats-dashboard">
      <div class="stat-card">
        <div class="stat-card-icon">💪</div>
        <div id="stats-total-reps" class="stat-card-num">0</div>
        <div class="stat-card-label">Lifetime Reps</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-icon">👹</div>
        <div id="stats-enemies-killed" class="stat-card-num">0</div>
        <div class="stat-card-label">Monsters Slaying</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-icon">🏆</div>
        <div id="stats-s-ranks" class="stat-card-num">0</div>
        <div class="stat-card-label">S-Rank Victories</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-icon">🔥</div>
        <div id="stats-streak" class="stat-card-num">5 Days</div>
        <div class="stat-card-label">Iron Discipline Streak</div>
      </div>
    </div>
  </div>

  <!-- SCREEN 5: ACCOUNT PROFILE -->
  <div id="account-screen" class="sub-screen">
    <div class="screen-header-title">👤 Knight Credentials</div>
    <div class="settings-list">
      <div class="setting-item">
        <label>Knight Name</label>
        <input type="text" id="account-name-input" value="Kayden" onchange="updateAccountName(this.value)">
      </div>
      <div class="setting-item">
        <label>Physical Biomass (Age & Weight)</label>
        <div style="display:flex; gap:10px;">
          <input type="number" id="account-age-input" value="20" placeholder="Age" onchange="recalculateAiGoals()">
          <input type="number" id="account-weight-input" value="140" placeholder="Weight (lbs)" onchange="recalculateAiGoals()">
        </div>
      </div>
      <div class="setting-item">
        <label>Baseline Max Rep Capacity</label>
        <input type="number" id="account-max-reps-input" value="15" onchange="recalculateAiGoals()">
      </div>
      <div class="setting-item">
        <label>Google Cloud Sync</label>
        <button class="btn btn-secondary" style="color: var(--danger);" onclick="triggerSignOut()">Sign Out from Cloud</button>
      </div>
    </div>
  </div>

  <!-- SCREEN 6: LEADERBOARDS -->
  <div id="leaderboard-screen" class="sub-screen">
    <div class="screen-header-title">🏆 Realm S-Rank Rankings</div>
    <div class="settings-list" id="leaderboard-list-container"></div>
  </div>

  <!-- BOTTOM NAVIGATION BAR -->
  <div class="bottom-nav">
    <div class="nav-item active" id="nav-home" onclick="switchTab('home')">
      <span>⚔️</span>
      <span>Hub</span>
    </div>
    <div class="nav-item" id="nav-story" onclick="switchTab('story')">
      <span>📜</span>
      <span>Campaign</span>
    </div>
    <div class="nav-item" id="nav-types" onclick="switchTab('types')">
      <span>🔄</span>
      <span>Styles</span>
    </div>
    <div class="nav-item" id="nav-stats" onclick="switchTab('stats')">
      <span>📊</span>
      <span>Stats</span>
    </div>
    <div class="nav-item" id="nav-account" onclick="switchTab('account')">
      <span>👤</span>
      <span>Knight</span>
    </div>
    <div class="nav-item" id="nav-leaderboard" onclick="switchTab('leaderboard')">
      <span>🏆</span>
      <span>Rank</span>
    </div>
  </div>

  <!-- ARENA CAMERA BATTLE VIEW -->
  <div id="arena-screen" class="screen">
    <div id="video-container">
      <video id="webcam" playsinline muted></video>
      <canvas id="output-canvas"></canvas>

      <div class="top-hud">
        <div class="boss-card">
          <div class="close-btn" onclick="exitArena()">✕</div>
          <div class="boss-lvl" id="arena-boss-title">CHAPTER 1-1: UNDEAD WARDEN</div>
          <div class="boss-name" id="boss-name-txt">HP: 18 / 18 Reps</div>
          <div class="hp-bar-bg">
            <div id="hp-bar" class="hp-bar-fill"></div>
            <div id="hp-txt" class="hp-text">18 Reps Remaining</div>
          </div>
        </div>
      </div>

      <div id="sensor-banner" class="sensor-status-banner">AI Sensor Locked: Lower chest until elbow breaks 85°</div>

      <div class="bottom-hud">
        <div class="stat-box">
          <div id="total-reps-val" class="stat-val">0</div>
          <div class="stat-lbl">Wave Reps</div>
        </div>

        <div id="rep-circle-val" class="rep-circle">0</div>

        <div class="stat-box">
          <div id="elbow-angle-val" class="stat-val">170°</div>
          <div class="stat-lbl">Elbow Angle</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ONBOARDING MODAL -->
  <div id="onboarding-modal" class="modal">
    <div class="onboarding-slide active" id="slide-auth" style="display: flex; flex-direction: column; align-items: center; text-align: center; justify-content: center; height: 100%;">
      <div style="font-size: 3.5rem; margin-bottom: 15px;">🛡️</div>
      <h1 style="font-size: 2rem; font-weight: 900; color: #fff; margin-bottom: 10px;">The Iron Oath</h1>
      <p style="color: var(--subtext); font-size: 0.95rem; margin-bottom: 30px; line-height: 1.5;">Step into the ultimate fitness ARPG. Sign in with Google to record your legendary battles across devices.</p>
      <button class="btn btn-google" onclick="loginWithGoogle()">
        <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.13 0-5.78-2.11-6.73-4.96H1.18v3.15C3.16 21.32 7.23 24 12 24z"/><path fill="#FBBC05" d="M5.27 14.24c-.25-.72-.38-1.49-.38-2.24s.13-1.52.38-2.24V6.6H1.18C.43 8.12 0 9.82 0 12s.43 3.88 1.18 5.4l4.09-3.16z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.23 0 3.16 2.68 1.18 6.6l4.09 3.15c.95-2.85 3.6-4.96 6.73-4.96z"/></svg>
        Sign In with Google Cloud
      </button>
    </div>

    <div class="slide-progress" id="onboarding-progress-bar" style="display: none;">
      <div class="progress-step active" id="p-step-1"></div>
      <div class="progress-step" id="p-step-2"></div>
      <div class="progress-step" id="p-step-3"></div>
      <div class="progress-step" id="p-step-4"></div>
    </div>

    <div class="slide-container" id="onboarding-slides-container" style="display: none;">
      <div class="onboarding-slide" id="slide-1">
        <h2>Choose Your Knight Name</h2>
        <p style="color: var(--subtext); font-size: 0.85rem;">Your moniker will echo across the Realm leaderboard.</p>
        <div style="margin-top: 10px;">
          <input type="text" id="signup-name" value="Kayden" placeholder="Knight Name">
        </div>
      </div>

      <div class="onboarding-slide" id="slide-2">
        <h2>What is your Age?</h2>
        <p style="color: var(--subtext); font-size: 0.85rem;">Calibrates the AI stamina curve.</p>
        <div style="margin-top: 10px;">
          <input type="number" id="signup-age" value="20">
        </div>
      </div>

      <div class="onboarding-slide" id="slide-3">
        <h2>Body Weight (lbs)?</h2>
        <p style="color: var(--subtext); font-size: 0.85rem;">Used to compute workload resistance ratios.</p>
        <div style="margin-top: 10px;">
          <input type="number" id="signup-weight" value="140">
        </div>
      </div>

      <div class="onboarding-slide" id="slide-4">
        <h2>Max Baseline Push-ups in 1 Set?</h2>
        <p style="color: var(--subtext); font-size: 0.85rem;">Determines your starting Chapter difficulty rating.</p>
        <div style="margin-top: 10px;">
          <input type="number" id="signup-max-reps" value="15">
        </div>
      </div>
    </div>

    <div class="slide-nav" id="onboarding-nav-btns" style="display: none; gap: 12px; margin-top: 24px;">
      <button class="btn btn-secondary" id="back-btn" onclick="prevSlide()" style="display: none;">Back</button>
      <button class="btn" id="next-btn" onclick="nextSlide()">Begin Oath</button>
    </div>
  </div>

  <!-- S-RANK VICTORY MODAL -->
  <div id="victory-modal" class="modal" style="justify-content: center; align-items: center; text-align: center;">
    <div style="font-size: 4rem; margin-bottom: 10px;" id="vic-rank-badge">🏆 SSS</div>
    <h1 style="font-size: 2rem; color: #fff; margin-bottom: 6px;" id="vic-title">BOSS SLAIN!</h1>
    <p style="color: var(--subtext); font-size: 0.95rem; margin-bottom: 24px;" id="vic-desc">You completed the wave with stellar precision.</p>
    <div style="background: var(--card-bg); border: 1px solid var(--card-border); padding: 16px; border-radius: 14px; width: 100%; max-width: 320px; margin-bottom: 24px; text-align: left;">
      <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span>Gold Earned:</span> <strong style="color:var(--accent-gold);">🪙 +120</strong></div>
      <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span>Gems Found:</span> <strong style="color:var(--primary);">💎 +5</strong></div>
      <div style="display: flex; justify-content: space-between;"><span>Rating:</span> <strong style="color:var(--rank-s);" id="vic-s-rank">S-RANK</strong></div>
    </div>
    <button class="btn" onclick="closeVictoryModal()">Return to Hub</button>
  </div>

  <!-- JavaScript Modules -->
  <script type="module" src="auth.js"></script>
  <script src="camera.js"></script>
  <script src="app.js"></script>
</body>
</html>""",

    "style.css": """:root {
  --bg: #0a0b0e;
  --card-bg: #13151b;
  --card-border: rgba(255, 255, 255, 0.08);
  --card-border-active: rgba(255, 255, 255, 0.35);
  --primary: #38bdf8;
  --primary-dark: #0284c7;
  --primary-glow: rgba(56, 189, 248, 0.35);
  --text: #f1f5f9;
  --subtext: #8b949e;
  --accent-gold: #fbbf24;
  --rank-s: #f43f5e;
  --danger: #f87171;
  --success: #34d399;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  user-select: none;
  -webkit-user-select: none;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

body {
  background-color: var(--bg);
  color: var(--text);
  overflow: hidden;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
}

.screen {
  display: none;
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  width: 100%; height: 100%;
  z-index: 10;
  background: var(--bg);
  flex-direction: column;
  padding-bottom: 90px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.screen.active { display: flex; }

#loading-screen {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  padding-bottom: 0;
  justify-content: center;
  align-items: center;
  z-index: 200;
  background: radial-gradient(circle at center, #181b24 0%, #0a0b0e 100%);
  display: flex;
  flex-direction: column;
}
.helmet-logo {
  width: 110px;
  height: 110px;
  image-rendering: pixelated;
  margin-bottom: 20px;
  animation: chillFloat 3s infinite ease-in-out;
  filter: drop-shadow(0 0 25px rgba(255,255,255,0.2));
}
@keyframes chillFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
.loading-title {
  font-size: 1.6rem;
  font-weight: 900;
  letter-spacing: 3px;
  color: #fff;
  margin-bottom: 6px;
  text-transform: uppercase;
}
.loading-sub {
  font-size: 0.75rem;
  color: var(--subtext);
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 24px;
  font-weight: 800;
}
.progress-bar-bg {
  width: 250px;
  height: 6px;
  background: rgba(255,255,255,0.06);
  border-radius: 3px;
  overflow: hidden;
  border: 1px solid var(--card-border);
}
.progress-bar-fill {
  height: 100%;
  width: 0%;
  background: #f1f5f9;
  transition: width 0.15s ease;
}

.app-header {
  padding: 44px 20px 14px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(19, 21, 27, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--card-border);
  z-index: 15;
  flex-shrink: 0;
}
.user-pill {
  display: flex;
  align-items: center;
  gap: 12px;
}
.user-avatar {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: #1c1f2b;
  border: 2px solid rgba(255,255,255,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 1.1rem;
  color: #fff;
  overflow: hidden;
}
.user-avatar img { width: 100%; height: 100%; object-fit: cover; }
.currency-badge {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--card-border);
  padding: 6px 12px;
  border-radius: 10px;
  font-family: monospace;
  font-size: 0.8rem;
  font-weight: 900;
  color: #fff;
}

.bottom-nav {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 76px;
  background: #0d0f14;
  backdrop-filter: blur(20px);
  border-top: 1px solid var(--card-border);
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 30;
  padding-bottom: env(safe-area-inset-bottom);
}
.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  color: var(--subtext);
  cursor: pointer;
  font-size: 0.65rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  transition: transform 0.15s ease, color 0.15s ease;
  flex: 1;
  padding: 8px 0;
}
.nav-item span:first-child {
  font-size: 1.2rem;
  font-family: monospace;
  font-weight: 900;
  transition: transform 0.15s ease;
}
.nav-item.active { color: #fff; }
.nav-item.active span:first-child { transform: scale(1.2); }

.menu-content {
  padding: 24px 20px 40px 20px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.hero-banner {
  background: linear-gradient(135deg, #171922 0%, #101219 100%);
  border: 1px solid var(--card-border);
  border-radius: 22px;
  padding: 24px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
.hero-tag {
  font-size: 0.72rem;
  font-weight: 900;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 6px;
}
.hero-title {
  font-size: 1.5rem;
  font-weight: 900;
  color: #fff;
  margin-bottom: 6px;
}
.hero-sub {
  font-size: 0.85rem;
  color: var(--subtext);
  margin-bottom: 20px;
  line-height: 1.45;
}

.modes-grid {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.mode-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 18px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 18px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 6px 20px rgba(0,0,0,0.25);
}
.mode-card:active {
  transform: scale(0.97);
  border-color: rgba(255,255,255,0.4);
}
.mode-icon-box {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: #1c1f2b;
  border: 1px solid var(--card-border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: monospace;
  font-size: 1.25rem;
  font-weight: 900;
  color: #fff;
  flex-shrink: 0;
}
.mode-info { flex: 1; }
.mode-title {
  font-size: 1.15rem;
  font-weight: 900;
  color: var(--text);
  margin-bottom: 4px;
}
.mode-desc {
  font-size: 0.8rem;
  color: var(--subtext);
  line-height: 1.4;
}
.mode-action-pill {
  background: #f1f5f9;
  color: #0a0b0e;
  font-weight: 900;
  font-size: 0.78rem;
  padding: 10px 18px;
  border-radius: 12px;
  flex-shrink: 0;
}

.sub-screen {
  display: none;
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 76px;
  background: var(--bg);
  z-index: 20;
  flex-direction: column;
  padding: 24px 20px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.sub-screen.active { display: flex; }

.screen-header-title {
  font-size: 1.5rem;
  font-weight: 900;
  margin-bottom: 18px;
  color: #fff;
  font-family: monospace;
  letter-spacing: -0.5px;
}

.campaign-chapters-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding-bottom: 50px;
}
.chapter-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 18px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.chapter-title {
  font-size: 1.1rem;
  font-weight: 900;
  color: #fff;
}
.levels-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
}
.level-node {
  background: #1c1f2b;
  border: 1px solid var(--card-border);
  border-radius: 12px;
  padding: 12px 6px;
  text-align: center;
  cursor: pointer;
}
.level-node.unlocked {
  background: rgba(56, 189, 248, 0.1);
  border-color: var(--primary);
}
.level-node.completed {
  background: rgba(52, 211, 153, 0.1);
  border-color: var(--success);
}
.level-node-num { font-weight: 900; font-size: 0.9rem; color: #fff; }
.level-node-rank { font-size: 0.65rem; font-family: monospace; color: var(--rank-s); font-weight: 900; margin-top: 4px; }

.stats-dashboard {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-bottom: 20px;
}
.stat-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 18px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.stat-card-icon { font-family: monospace; font-size: 1.3rem; font-weight: 900; color: var(--subtext); }
.stat-card-num { font-size: 1.6rem; font-weight: 900; color: #fff; }
.stat-card-label { font-size: 0.75rem; color: var(--subtext); text-transform: uppercase; font-weight: 800; }

.settings-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-bottom: 50px;
}
.setting-item {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 18px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

label {
  font-size: 0.85rem;
  color: var(--subtext);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
input, select {
  width: 100%;
  padding: 14px;
  background: #0f1117;
  border: 1px solid var(--card-border);
  border-radius: 12px;
  color: #fff;
  font-size: 1rem;
  outline: none;
  font-weight: 700;
  -webkit-user-select: text;
  user-select: text;
}

.btn {
  width: 100%;
  padding: 16px;
  border-radius: 14px;
  border: none;
  background: #f1f5f9;
  color: #0a0b0e;
  font-weight: 900;
  font-size: 1.05rem;
  cursor: pointer;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.btn:active { transform: scale(0.98); opacity: 0.9; }
.btn-secondary {
  background: #1c1f2b;
  border: 1px solid var(--card-border);
  color: #fff;
}
.btn-google {
  background: #fff;
  color: #000;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  font-weight: 900;
}

.type-pill-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-top: 6px;
}
.type-pill {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--card-border);
  padding: 12px;
  border-radius: 12px;
  text-align: center;
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--subtext);
  cursor: pointer;
}
.type-pill.selected {
  background: rgba(56, 189, 248, 0.12);
  border-color: var(--primary);
  color: var(--primary);
}

.modal {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(10, 11, 14, 0.98);
  z-index: 150;
  display: none;
  flex-direction: column;
  padding: 40px 24px;
  overflow-y: auto;
}
.modal.active { display: flex; }

.slide-progress {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}
.progress-step {
  flex: 1;
  height: 5px;
  background: rgba(255,255,255,0.08);
  border-radius: 3px;
}
.progress-step.active { background: var(--primary); }

.onboarding-slide {
  display: none;
  flex-direction: column;
  gap: 14px;
}
.onboarding-slide.active { display: flex; }

#arena-screen { background: #000; padding-bottom: 0; }
#video-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
video, canvas {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  object-fit: cover;
}
.top-hud {
  position: absolute;
  top: 45px; left: 16px; right: 16px;
  z-index: 20;
}
.boss-card {
  background: rgba(19, 21, 27, 0.92);
  border: 1px solid var(--card-border);
  border-radius: 18px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  backdrop-filter: blur(12px);
}
.boss-lvl {
  font-size: 0.72rem;
  color: var(--primary);
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1.2px;
}
.boss-name {
  font-size: 1.15rem;
  font-weight: 900;
  color: #fff;
}
.hp-bar-bg {
  width: 100%;
  height: 20px;
  background: rgba(255,255,255,0.06);
  border-radius: 8px;
  margin-top: 10px;
  overflow: hidden;
  position: relative;
  border: 1px solid var(--card-border);
}
.hp-bar-fill {
  height: 100%;
  width: 100%;
  background: var(--primary);
  transition: width 0.25s ease-out;
}
.hp-text {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 0.78rem;
  color: #0a0b0e;
}
.close-btn {
  position: absolute;
  top: 12px; right: 14px;
  width: 30px; height: 30px;
  background: rgba(255,255,255,0.08);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: #fff;
  cursor: pointer;
  border: 1px solid var(--card-border);
}
.sensor-status-banner {
  position: absolute;
  top: 185px; left: 20px; right: 20px;
  background: rgba(19, 21, 27, 0.92);
  border: 1px solid var(--card-border);
  border-radius: 14px;
  padding: 12px 18px;
  color: #fff;
  font-size: 0.85rem;
  font-weight: 800;
  text-align: center;
  z-index: 25;
  backdrop-filter: blur(10px);
}
.bottom-hud {
  position: absolute;
  bottom: 40px; left: 20px; right: 20px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  z-index: 20;
}
.stat-box {
  background: rgba(19, 21, 27, 0.9);
  border: 1px solid var(--card-border);
  border-radius: 16px;
  padding: 12px 16px;
  text-align: center;
  backdrop-filter: blur(10px);
  min-width: 90px;
}
.stat-val { font-size: 1.4rem; font-weight: 900; color: #fff; }
.stat-lbl { font-size: 0.65rem; color: var(--subtext); text-transform: uppercase; letter-spacing: 0.8px; font-weight: 800; }
.rep-circle {
  width: 90px; height: 90px;
  border-radius: 50%;
  border: 4px solid var(--primary);
  background: rgba(19, 21, 27, 0.92);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.4rem;
  font-weight: 900;
  color: var(--primary);
}""",

    "auth.js": """import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyAT1A-Em7JMMi-v4eZLEHxSZc7afJs9mpg",
  authDomain: "push-up-arena-371b9.firebaseapp.com",
  projectId: "push-up-arena-371b9",
  storageBucket: "push-up-arena-371b9.firebasestorage.app",
  messagingSenderId: "428269289235",
  appId: "1:428269289235:web:3e3706dcfead663442e4e6",
  measurementId: "G-87JFFS2B7M"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

window.firebaseAuth = auth;
window.firebaseProvider = provider;
window.signInWithPopup = signInWithPopup;
window.signOut = signOut;
window.onAuthStateChanged = onAuthStateChanged;

onAuthStateChanged(auth, (user) => {
  if (user) {
    window.state.signedIn = true;
    window.state.userName = user.displayName || "Kayden";
    window.state.photoURL = user.photoURL || "";

    const saved = localStorage.getItem('pushup_realm_state_' + user.uid);
    if (saved) {
      try { window.state = { ...window.state, ...JSON.parse(saved) }; } catch(e){}
      document.getElementById('onboarding-modal').classList.remove('active');
      window.postLoginInit();
    } else {
      document.getElementById('onboarding-modal').classList.add('active');
      document.getElementById('slide-auth').style.display = 'none';
      document.getElementById('onboarding-progress-bar').style.display = 'flex';
      document.getElementById('onboarding-slides-container').style.display = 'flex';
      document.getElementById('onboarding-nav-btns').style.display = 'flex';
      document.getElementById('signup-name').value = window.state.userName;
      window.updateSlideUI();
    }
  } else {
    window.state.signedIn = false;
    document.getElementById('onboarding-modal').classList.add('active');
    document.getElementById('slide-auth').style.display = 'flex';
    document.getElementById('onboarding-progress-bar').style.display = 'none';
    document.getElementById('onboarding-slides-container').style.display = 'none';
    document.getElementById('onboarding-nav-btns').style.display = 'none';
  }
});""",

    "camera.js": """let camera = null;
let pose = null;
let repPhase = "TOP";
let smoothedAngle = 170;

function startArena(mode) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.sub-screen').forEach(s => s.classList.remove('active'));
  document.querySelector('.bottom-nav').style.display = 'none';
  document.getElementById('arena-screen').classList.add('active');

  window.state.currentReps = 0;
  updateArenaHpDisplay();

  const videoElement = document.getElementById('webcam');
  const canvasElement = document.getElementById('output-canvas');
  const canvasCtx = canvasElement.getContext('2d');

  pose = new Pose({ locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}` });
  pose.setOptions({ modelComplexity: 1, smoothLandmarks: true, minDetectionConfidence: 0.7, minTrackingConfidence: 0.7 });

  pose.onResults((results) => {
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;
    canvasCtx.save();
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    canvasCtx.drawImage(results.image, 0, 0, canvasElement.width, canvasElement.height);

    if (results.poseLandmarks) {
      processSensorEngine(results.poseLandmarks);
    }
    canvasCtx.restore();
  });

  camera = new Camera(videoElement, {
    onFrame: async () => { await pose.send({ image: videoElement }); },
    width: 640,
    height: 480
  });
  camera.start();
}

function startCampaignLevel(chapterId, levelId) {
  window.currentChapter = chapterId;
  window.currentLevel = levelId;
  const chapter = window.storyChapters[chapterId - 1];
  const boss = chapter.bosses[levelId - 1];

  window.state.aiTargetReps = boss.reps;
  document.getElementById('arena-boss-title').innerText = `CHAPTER ${chapterId}-${levelId}: ${chapter.name}`;
  document.getElementById('boss-name-txt').innerText = `Boss: ${boss.name} (${boss.reps} Reps)`;

  startArena('story');
}

function processSensorEngine(landmarks) {
  const lShoulder = landmarks[11], lElbow = landmarks[13], lWrist = landmarks[15];
  if (!lShoulder || !lElbow || !lWrist) return;

  const rawAngle = calculateAngle(lShoulder, lElbow, lWrist);
  smoothedAngle = (smoothedAngle * 0.5) + (rawAngle * 0.5);
  document.getElementById('elbow-angle-val').innerText = Math.round(smoothedAngle) + '°';

  let bottomThreshold = window.state.formStrictness === 'master' ? 75 : (window.state.formStrictness === 'lenient' ? 95 : 85);

  if (repPhase === "TOP" && smoothedAngle < 130) {
    repPhase = "DESCENDING";
  } else if (repPhase === "DESCENDING" && smoothedAngle <= bottomThreshold) {
    repPhase = "BOTTOM";
  } else if (repPhase === "BOTTOM" && smoothedAngle > 105) {
    repPhase = "ASCENDING";
  } else if (repPhase === "ASCENDING" && smoothedAngle >= 145) {
    repPhase = "TOP";
    window.state.currentReps++;
    window.state.totalReps++;
    window.state.gold += 10;
    document.getElementById('rep-circle-val').innerText = window.state.currentReps;
    document.getElementById('total-reps-val').innerText = window.state.currentReps;
    document.getElementById('header-gold-val').innerText = window.state.gold;
    updateArenaHpDisplay();

    if (window.state.currentReps >= window.state.aiTargetReps) {
      triggerVictoryCondition();
    }
    saveState();
  }
}

function calculateAngle(A, B, C) {
  const AB = Math.sqrt(Math.pow(B.x - A.x, 2) + Math.pow(B.y - A.y, 2));
  const BC = Math.sqrt(Math.pow(B.x - C.x, 2) + Math.pow(B.y - C.y, 2));
  const AC = Math.sqrt(Math.pow(C.x - A.x, 2) + Math.pow(C.y - A.y, 2));
  return Math.acos((Math.pow(AB, 2) + Math.pow(BC, 2) - Math.pow(AC, 2)) / (2 * AB * BC)) * (180 / Math.PI);
}

function updateArenaHpDisplay() {
  const rem = Math.max(0, window.state.aiTargetReps - window.state.currentReps);
  const pct = Math.min(100, (window.state.currentReps / window.state.aiTargetReps) * 100);
  document.getElementById('hp-bar').style.width = pct + '%';
  document.getElementById('hp-txt').innerText = `${rem} Reps Remaining`;
}

function triggerVictoryCondition() {
  if (camera) camera.stop();
  window.state.enemiesDefeated++;
  window.state.sRanksAchieved++;
  window.state.gems += 5;

  if (window.currentChapter && window.currentLevel) {
    if (!window.state.campaignProgress[window.currentChapter]) {
      window.state.campaignProgress[window.currentChapter] = {};
    }
    window.state.campaignProgress[window.currentChapter][window.currentLevel] = "SSS";
    
    if (window.currentLevel < 5) {
      window.state.unlockedLevel = Math.max(window.state.unlockedLevel, window.currentLevel + 1);
    } else if (window.currentChapter < 5) {
      window.state.unlockedChapter = Math.max(window.state.unlockedChapter, window.currentChapter + 1);
      window.state.unlockedLevel = 1;
    }
  }

  document.getElementById('arena-screen').classList.remove('active');
  document.getElementById('victory-modal').classList.add('active');
  saveState();
}

function closeVictoryModal() {
  document.getElementById('victory-modal').classList.remove('active');
  document.querySelector('.bottom-nav').style.display = 'flex';
  switchTab('story');
  renderStoryCampaignMap();
}

function exitArena() {
  if (camera) camera.stop();
  document.getElementById('arena-screen').classList.remove('active');
  document.querySelector('.bottom-nav').style.display = 'flex';
  switchTab('home');
  saveState();
}

window.startArena = startArena;
window.startCampaignLevel = startCampaignLevel;
window.exitArena = exitArena;
window.closeVictoryModal = closeVictoryModal;""",

    "app.js": """window.state = {
  userName: "Kayden",
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
const totalSlides = 4;

function loginWithGoogle() {
  window.signInWithPopup(window.firebaseAuth, window.firebaseProvider)
    .catch((error) => {
      alert("Google Sign-In Error: " + error.message);
    });
}

function postLoginInit() {
  runAiTargetCalculation();
  document.getElementById('header-gold-val').innerText = window.state.gold;
  document.getElementById('header-gems-val').innerText = window.state.gems;
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
    document.getElementById(`slide-${i}`).classList.toggle('active', i === currentSlide);
    document.getElementById(`p-step-${i}`).classList.toggle('active', i <= currentSlide);
  }
  document.getElementById('back-btn').style.display = currentSlide === 1 ? 'none' : 'block';
  document.getElementById('next-btn').innerText = currentSlide === totalSlides ? 'Enter Realm' : 'Next';
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
  alert(`🛡️ ARMORY & ARTIFACT SHOP\nGold: 🪙 ${window.state.gold} | Gems: 💎 ${window.state.gems}\\n\\nLegendary Gear Unlocked!`);
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
window.openArmory = openArmory;
window.saveState = saveState;"""
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully updated: {filename}")

print("\\nAll project files successfully regenerated and synchronized!")
