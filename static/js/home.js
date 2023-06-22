const carousel = document.querySelector('.carousel');

let isDragging = false;
let startPos = 0;
let currentTranslate = 0;
let prevTranslate = 0;

carousel.addEventListener('mousedown', dragStart);
carousel.addEventListener('touchstart', dragStart);
carousel.addEventListener('mouseup', dragEnd);
carousel.addEventListener('mouseleave', dragEnd);
carousel.addEventListener('touchend', dragEnd);
carousel.addEventListener('mousemove', drag);
carousel.addEventListener('touchmove', drag);

function dragStart(event) {
  if (event.type === 'touchstart') {
    startPos = event.touches[0].clientX;
  } else {
    startPos = event.clientX;
    event.preventDefault();
  }

  isDragging = true;
  // Captura a posição inicial do mouse ou toque
  prevTranslate = currentTranslate;
}

function drag(event) {
  if (isDragging) {
    let currentPosition = 0;
    if (event.type === 'touchmove') {
      currentPosition = event.touches[0].clientX;
    } else {
      currentPosition = event.clientX;
    }

    // Calcula o quanto o mouse ou toque se moveu em relação à posição inicial
    const diff = currentPosition - startPos;
    // Atualiza a posição de rolagem do carrossel
    currentTranslate = prevTranslate + diff;

    // Aplica a tradução para mover o carrossel
    carousel.style.transform = `translateX(${currentTranslate}px)`;
  }
}

function dragEnd() {
  isDragging = false;
}
