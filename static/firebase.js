
// Fire base scrip

  // Initialize Firebase (ADD YOUR OWN DATA)
  var config = {
    apiKey: "AIzaSyAZ8ophdxLM8GYjpSjhhY8wC0k6GQ2Jccg",
    authDomain: "mental-health-16acb.firebaseapp.com",
    projectId: "mental-health-16acb",
    databaseURL:"https://mental-health-16acb-default-rtdb.firebaseio.com/",
    storageBucket: "mental-health-16acb.appspot.com",
    messagingSenderId: "492537790330",
    appId: "1:492537790330:web:295ed6b580c660b7f8a0c3",
    measurementId: "G-YSGNX1NWX7",
  };
  firebase.initializeApp(config);

  // Reference messages collection
  var messagesRef = firebase.database().ref("UserData");

  // Listen for form submit
  document
    .getElementById("contactForm")
    .addEventListener("submit", submitForm);

  // Submit form
  function submitForm(e) {
    e.preventDefault();

    // Get values
    var name = getInputVal("name");
    var age = getInputVal("age");
    var email = getInputVal("email");
    var country = getInputVal("country");

    // Save message
    saveMessage(name, email, age, country);

    // Show alert


    // Hide alert after 3 seconds
    /*setTimeout(function () {
      document.querySelector(".alert").style.display = "none";
    }, Infinity);*/

    // Clear form
    document.getElementById("contactForm").reset();
  }

  // Function to get get form values
  function getInputVal(id) {
    return document.getElementById(id).value;
  }

  // Save message to firebase
  function saveMessage(name, email, age, country) {
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
      name: name,
      email: email,
      age: age,
      country: country,
    });
  }

  