# // Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
# // TODO: Add SDKs for Firebase products that you want to use
# // https://firebase.google.com/docs/web/setup#available-libraries

# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDX8GJT90eu6MplhEOAlXseybv9OteoSSU",
  authDomain: "amigos-52944.firebaseapp.com",
  projectId: "amigos-52944",
  storageBucket: "amigos-52944.appspot.com",
  messagingSenderId: "636326216246",
  appId: "1:636326216246:web:dfbd03ffc4373b366f4e97",
  measurementId: "G-FTTE8XKENY"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);