//evento mensaje envio formulario contacto

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('.form2');

  form.addEventListener('submit', function(e) {
      e.preventDefault();

      alert('Los datos se han enviado correctamente.'); // Muestra una alerta

      form.reset(); // Resetea el formulario después de enviar

    });
});


  
 //eventos del formulario de login

 document.getElementById('formLogin').addEventListener('submit', function(event1) {
  event1.preventDefault(); // Evita que el formulario se envíe automáticamente
  
    var nomUsuario = document.getElementById('nombreUsuario').value;
    var contraseña = document.getElementById('password').value;
  
    //variables ficticias para prueba
    var usuarios = [
      {nomUsuario: 'usuario1', contraseña: 'contraseña1'},
      {nomUsuario: 'usuario2', contraseña: 'contraseña2'},
    ];
  
    var usuarioCorrecto = false;
  
    for (var i = 0; i < usuarios.length; i++) {
      if (usuarios[i].nomUsuario === nomUsuario && usuarios[i].contraseña === contraseña) {
        usuarioCorrecto = true;
        break;
      }
    }
  
    if (usuarioCorrecto) {
      alert('Inicio de sesión exitoso');
    } else {
      alert('El nombre de usuario y/o la contraseña no son correctos.');
    }
  });
  
   //eventos del formulario de Registro

 document.getElementById('registroForm').addEventListener('submit', function(event1) {
    event1.preventDefault(); // Evita que el formulario se envíe automáticamente
  
    var regNombreUsuario = document.getElementById('regNombreUsuario').value;
    var contraseña = document.getElementById('regPassword').value;
    var mail= document.getElementById('regEmail').value;
  
    //variables ficticias para prueba
    var usuarios = [
      {regNombreUsuario: 'usuario1', contraseña: 'contraseña1', mail: 'usuario1@gmail.com'},
      {regNombreUsuario: 'usuario2', contraseña: 'contraseña2', mail: 'usuario2@gmail.com'},
    ];
  
    var usuarioCorrecto = false;
  
    for (var i = 0; i < usuarios.length; i++) {
      if (usuarios[i].regNombreUsuario === regNombreUsuario && usuarios[i].contraseña === contraseña && 
        usuarios[i].mail=== mail) {
        usuarioCorrecto = true;
        break;
      }
    }
  
    if (usuarioCorrecto) {
      alert('Registro exitoso');
    } else {
      alert('Los datos ingresados son incorrectos.');
    }
  });
  