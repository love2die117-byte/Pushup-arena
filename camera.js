let camera = null;
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
window.closeVictoryModal = closeVictoryModal;
