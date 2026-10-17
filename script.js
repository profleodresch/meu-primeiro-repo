function calcularIMC(peso, altura) {
  return peso / (altura * altura);
}

function classificarIMC(imc) {
  if (imc < 18.5) return "Abaixo do peso";
  if (imc < 25) return "Peso normal";
  if (imc < 30) return "Sobrepeso";
  if (imc < 35) return "Obesidade grau 1";
  if (imc < 40) return "Obesidade grau 2";
  return "Obesidade grau 3 (mórbida)";
}

function parseNumero(valor) {
  if (typeof valor !== "string") return NaN;
  return parseFloat(valor.trim().replace(",", "."));
}

document.getElementById("btn-calcular").addEventListener("click", () => {
  const peso = parseNumero(document.getElementById("peso").value);
  const altura = parseNumero(document.getElementById("altura").value);
  const div = document.getElementById("resultado");

  if (!peso || peso <= 0 || !altura || altura <= 0) {
    alert("Digite peso e altura válidos maiores que zero. Ex: 70.5 e 1.75");
    return;
  }

  const imc = calcularIMC(peso, altura);
  document.getElementById("valor-imc").textContent = imc.toFixed(2);
  document.getElementById("class-imc").textContent = classificarIMC(imc);
  div.classList.remove("escondido");
});

document.getElementById("btn-limpar").addEventListener("click", () => {
  document.getElementById("peso").value = "";
  document.getElementById("altura").value = "";
  document.getElementById("resultado").classList.add("escondido");
});
