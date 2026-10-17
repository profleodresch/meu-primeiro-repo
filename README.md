# meu-primeiro-repo
Meu primeiro repositório - aprendendo Git, GitHub, Python e Web 🚀

## 📊 Calculadora de IMC

Aplicativo que calcula o Índice de Massa Corporal — em **Python (terminal)** e **Web (navegador)**.

### Opção A — Python (terminal)

```bash
python imc.py
```

Digite seu peso (kg) e altura (m) quando solicitado.

Exemplo:
```
Digite seu peso em kg (ex: 70.5): 70.5
Digite sua altura em metros (ex: 1.75): 1.75

Seu IMC: 23.02
Classificação: Peso normal
```

### Opção B — Web (navegador)

Abra o arquivo `index.html` no navegador, ou use um servidor local:

```bash
python -m http.server 8000
# acesse http://localhost:8000
```

Digite peso e altura e clique em **Calcular IMC**.

Arquivos:
- `index.html` → estrutura
- `style.css` → visual
- `script.js` → cálculo

### Fórmula
IMC = peso / (altura × altura)

### Tabela OMS
| IMC | Classificação |
|-----|---------------|
| < 18.5 | Abaixo do peso |
| 18.5 - 24.9 | Peso normal |
| 25 - 29.9 | Sobrepeso |
| 30 - 34.9 | Obesidade grau 1 |
| 35 - 39.9 | Obesidade grau 2 |
| >= 40 | Obesidade grau 3 |


