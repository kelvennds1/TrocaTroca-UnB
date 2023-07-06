// Obtém o elemento do carrossel
const carousel = document.querySelector('.carousel');

let isDragging = false; // Indica se o usuário está arrastando o carrossel
let startPos = 0; // Posição inicial do toque
let currentTranslate = 0; // Valor atual do deslocamento

// Evento de toque inicial
carousel.addEventListener('touchstart', touchStart);

function touchStart(e) {
  isDragging = true;
  startPos = e.touches[0].clientX; // Obtém a posição inicial do toque
  currentTranslate = getTranslateX(); // Obtém o valor atual do deslocamento
}

// Evento de movimento do toque
carousel.addEventListener('touchmove', touchMove);

function touchMove(e) {
  if (!isDragging) return;

  const currentPosition = e.touches[0].clientX; // Obtém a posição atual do toque
  const diff = currentPosition - startPos; // Calcula a diferença de posição

  // Atualiza o deslocamento do carrossel de acordo com a diferença de posição
  const newTranslate = currentTranslate + diff;
  setTranslateX(newTranslate);

  // Restringe o deslocamento para evitar que os itens desapareçam
  const maxTranslate = getMaxTranslate();
  const minTranslate = 0;

  if (newTranslate > maxTranslate) {
    setTranslateX(maxTranslate);
  } else if (newTranslate < minTranslate) {
    setTranslateX(minTranslate);
  }
}

// Evento de finalização do toque
carousel.addEventListener('touchend', touchEnd);

function touchEnd() {
  isDragging = false;
}

// Função auxiliar para obter o valor atual de deslocamento do carrossel
function getTranslateX() {
  const transformMatrix = window.getComputedStyle(carousel).getPropertyValue('transform');
  const matrix = new DOMMatrixReadOnly(transformMatrix);
  return matrix.m41;
}

// Função auxiliar para definir o valor de deslocamento do carrossel
function setTranslateX(value) {
  carousel.style.transform = `translateX(${value}px)`;
}

// Função auxiliar para obter o valor máximo de deslocamento
function getMaxTranslate() {
  const containerWidth = carousel.offsetWidth;
  const contentWidth = carousel.scrollWidth;
  return containerWidth - contentWidth;
}

// Selecione todos os elementos com a classe '.item'
var items = document.querySelectorAll('.item');

// Adicione o evento de clique a cada item
items.forEach(function(item) {
  item.addEventListener('click', function() {
    // Obtenha o ID do item clicado
    var itemId = item.getAttribute('data-id');
    
    // Redirecione para a página de compra do produto usando o ID
    window.location.href = '/anuncio/' + itemId;
  });
});


const hamburgerIcon = document.getElementById("hamburgerIcon");
const sidebar = document.querySelector(".sidebar");

hamburgerIcon.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});

