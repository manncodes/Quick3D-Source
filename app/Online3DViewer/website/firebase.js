// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
    apiKey: "AIzaSyBHUU0WTY8j9QDX-rEx-rNvMrRIzwI9l5E",
    authDomain: "quick3d-a9d3d.firebaseapp.com",
    projectId: "quick3d-a9d3d",
    storageBucket: "quick3d-a9d3d.appspot.com",
    messagingSenderId: "751533499745",
    appId: "1:751533499745:web:56b8968d9258a20b569120",
    measurementId: "G-XGRYMWCTYW"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

var starsRef = storageRef.child('img/1.jpg');
// Get the download URL
starsRef.getDownloadURL()
.then((url) => {
    console.log(url)
    var test = 'firebase_url';
    document.querySelector('#preview-img').src = test;
// Insert url into an <img> tag to "download"
})
.catch((error) => {
// A full list of error codes is available at
// https://firebase.google.com/docs/storage/web/handle-errors
switch (error.code) {
    case 'storage/object-not-found':
    // File doesn't exist
    break;
    case 'storage/unauthorized':
    // User doesn't have permission to access the object
    break;
    case 'storage/canceled':
    // User canceled the upload
    break;

    // ...

    case 'storage/unknown':
    // Unknown error occurred, inspect the server response
    break;
}
});


// Create a reference to the file we want to download
var starsRef = storageRef.child('images/1.jpg');

// Get the download URL
starsRef.getDownloadURL()
.then((url) => {
  // Insert url into an <img> tag to "download"
})
.catch((error) => {
  // A full list of error codes is available at
  // https://firebase.google.com/docs/storage/web/handle-errors
  switch (error.code) {
    case 'storage/object-not-found':
      // File doesn't exist
      break;
    case 'storage/unauthorized':
      // User doesn't have permission to access the object
      break;
    case 'storage/canceled':
      // User canceled the upload
      break;

    // ...

    case 'storage/unknown':
      // Unknown error occurred, inspect the server response
      break;
  }
});