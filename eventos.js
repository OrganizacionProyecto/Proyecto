
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form2');
  
    form.addEventListener('submit', function(e) {
      e.preventDefault();
  
      const nombre = document.getElementById('nombre').value;
      const email = document.getElementById('email').value;
  
      //  agregar la lógica para enviar el correo electrónico.
  
      alert("Su solicitud se ha enviado con éxito. En breve nos comunicaremos con usted.");
  
      form.reset();
    });
  });

  
 //eventos del formulario de login

 document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('showRegister').addEventListener('click', function() {
      document.getElementById('registerContainer').style.display = 'block';
      document.getElementById('showLogin').style.display = 'inline';
      document.getElementById('showRegister').style.display = 'none';
      document.getElementById('loginContainer').style.display = 'none';
  });

  document.getElementById('showLogin').addEventListener('click', function() {
      document.getElementById('registerContainer').style.display = 'none';
      document.getElementById('showLogin').style.display = 'none';
      document.getElementById('showRegister').style.display = 'inline';
      document.getElementById('loginContainer').style.display = 'block';
  });

  document.getElementById('loginForm').addEventListener('submit', function(event) {
      event.preventDefault();
      var username = document.getElementById('username').value;
      var password = document.getElementById('password').value;
      // Aquí puedes agregar la lógica de autenticación con JavaScript
  });

  document.getElementById('registerForm').addEventListener('submit', function(event) {
      event.preventDefault();
      var regUsername = document.getElementById('regUsername').value;
      var regPassword = document.getElementById('regPassword').value;
      var regEmail = document.getElementById('regEmail').value;
      // Aquí puedes agregar la lógica de registro con JavaScript
  });
});


