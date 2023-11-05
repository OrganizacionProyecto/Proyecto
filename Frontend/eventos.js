//evento mensaje envio formulario contacto



const imagenes = ["imag_productos/aceite_coco.jpeg", "imag_productos/cafe_verde.jpeg", "imag_productos/garcimax.jpeg"];
let index = 0;

function cambiarImagen() {
    document.getElementById("carruselImagen").src = imagenes[index];
    index = (index + 1) % imagenes.length;
}

cambiarImagen(); // Muestra la primera imagen de inmediato

setInterval(cambiarImagen, 2000); // Cambia de imagen cada 2 segundos

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('.form2');

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;

    if (nombre.trim() === '' || email.trim() === '') {
      alert("Por favor, complete todos los campos.");
      return;
    }

    if (!isValidEmail(email)) {
      alert("Por favor, ingrese una dirección de correo electrónico válida.");
      return;
    }

    alert("Su solicitud se ha enviado con éxito. En breve nos comunicaremos con usted.");

    form.reset();
  });

  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
    return email.includes('@');
  }
});


//eventos del formulario de login
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('formLogin');

  if (form) {
    form.addEventListener('submit', function(event) {
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
        alert("El nombre de usuario y/o la contraseña no son correctos.");
      }
    });
  }
});


   //eventos del formulario de Registro

   document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
  
    var regNombreUsuario = document.getElementById('regNombreUsuario').value;
    var contraseña = document.getElementById('regPassword').value;
    var mail= document.getElementById('regEmail').value;
    
      
      alert('Excelente!!! en breve recibiras un mail con indicaciones.');
    });

   
    