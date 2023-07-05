
document.addEventListener("DOMContentLoaded", function() {
  // Selecionar o botão de troca
  var trocaButton = document.getElementById("filter-troca");
  var doacaoButton = document.getElementById("filter-doacao");
  // Adicionar o manipulador de evento para o botão de troca
  trocaButton.addEventListener("click", function() {
    // Redirecionar para a página de troca
    window.location.href = "/explorar/Troca";
  });
  doacaoButton.addEventListener("click", function() {
    // Redirecionar para a página de troca
    window.location.href = "/explorar/Doação";
  });
});

// Selecione todos os elementos com a classe '.item'
var items = document.querySelectorAll('.item');

items.forEach(function(item) {
  item.addEventListener('click', function() {
    // Obtenha o ID do item clicado
    var itemId = item.getAttribute('data-id');
    
    // Redirecione para a página de compra do produto usando o ID
    window.location.href = '/anuncio/' + itemId;
  });
});



