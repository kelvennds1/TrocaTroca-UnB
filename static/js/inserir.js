function checkCategory() {
    var categorySelect = document.getElementById("category");
    var raceLabel = document.getElementById("race-label");
    var raceInput = document.getElementById("race");
    var brandLabel = document.getElementById("brand-label");
    var brandInput = document.getElementById("brand");

    if (categorySelect.value === "28") {
    raceLabel.style.display = "block";
    raceInput.style.display = "block";
    brandLabel.style.display = "none";
    brandInput.style.display = "none";
    } else {
    raceLabel.style.display = "none";
    raceInput.style.display = "none";
    brandLabel.style.display = "block";
    brandInput.style.display = "block";
    }
}