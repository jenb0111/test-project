import firebase from 'firebase/app'
import 'firebase/firestore'

// Initialize Firebase
var config = {
    apiKey: "AIzaSyAsEMlAAvqvl1Q5Hc5Xm9Djj0cSKyuqyIY",
    authDomain: "test-project-98a1b.firebaseapp.com",
    databaseURL: "https://test-project-98a1b.firebaseio.com",
    projectId: "test-project-98a1b",
    storageBucket: "test-project-98a1b.appspot.com",
    messagingSenderId: "217146269575"
  };
  firebase.initializeApp(config);
  const db = firebase.firestore();

  db.settings({ timestampsInSnapshots: true })

  export default db;