//evento mensaje envio formulario contacto

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form2');
  
    form.addEventListener('submit', function(e) {
      e.preventDefault();
  
      const nombre = document.getElementById('nombre').value;
      const email = document.getElementById('email').value;
  
    alert("Su solicitud se ha enviado con éxito. En breve nos comunicaremos con usted.");
  
      form.reset();
    });
  });

  
 //eventos del formulario de login

 document.getElementById('formLogin').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
  
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
  