
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



