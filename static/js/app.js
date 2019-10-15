'use strict';

let button = document.getElementById('ver');

button.onclick = function() {

  let passwordInput = document.getElementById('password');

  if (passwordInput.type == 'text') {
    passwordInput.type = 'password';
  } else {
    passwordInput.type = 'text';
  }

}

