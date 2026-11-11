import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
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

    const saved = localStorage.getItem('pushup_arena_state_' + user.uid);
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
});
