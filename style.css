:root {
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
}
