// Obtén el elemento <ul> donde se mostrará el historial
var listaHistorial = document.getElementById('lista-historial');

// Función para agregar un nuevo elemento de seguimiento
function agregarSeguimiento(fecha, estado) {
  // Crea un nuevo elemento de lista <li>
  var nuevoElemento = document.createElement('li');
  
  // Crea los elementos de <span> para la fecha y el estado
  var spanFecha = document.createElement('span');
  spanFecha.className = 'fecha';
  spanFecha.textContent = fecha;
  
  var spanEstado = document.createElement('span');
  spanEstado.className = 'estado';
  spanEstado.textContent = estado;
  
  // Agrega los elementos <span> al elemento <li>
  nuevoElemento.appendChild(spanFecha);
  nuevoElemento.appendChild(spanEstado);
  
  // Agrega el elemento <li> al historial
  listaHistorial.appendChild(nuevoElemento);
}

// Ejemplo de uso: agregar un nuevo elemento al historial
agregarSeguimiento('2023-06-01 10:00', 'En proceso');
