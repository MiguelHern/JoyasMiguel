let button_agregar = document.querySelector(".button__more");
let display_alert = document.querySelector('.container__alerta-inventario')

button_agregar.addEventListener('click', () => {
    if (display_alert.style.display !== 'flex') {
        display_alert.style.display = 'flex';
    } else {
        display_alert.style.display = 'none';
    }
})

display_alert.addEventListener('click', (event) => {
    if (event.target === display_alert) {
        display_alert.style.display = 'none';
    }
});

/* ****************************** Input Files img ****************************** */
let inputFile = document.getElementById('archivo')
let imgFile = document.querySelector('.img_inputFile')
let buttonFile = document.getElementById('button__file')
let buttonText = document.querySelector('.buttonText')

inputFile.addEventListener('change', (event) => {
    var input = event.target;

    // Verificar si se seleccionó una imagen
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            buttonText.textContent = '';
            buttonFile.style.paddingTop = '8px'
            imgFile.src = e.target.result;
            imgFile.style.height = '200px';
        };

        // Leer el contenido de la imagen como una URL de datos
        reader.readAsDataURL(input.files[0]);
    }
})