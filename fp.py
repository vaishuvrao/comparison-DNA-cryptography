from firebase import firebase
firebase = firebase.FirebaseApplication('https://simple-and-f6cb1.firebaseio.com/', None)
result = firebase.get('/Crypto/key/', '')
print(result)