# Teste de Calculadora com Appium
Teste automatizado para somar 2 + 2 no aplicativo de calculadora do Android usando Appium.

# Autor
Kennedy Gustavo de Oliveira

## Pré-requisitos
- Linux
- Node.js
- Java JDK
- Android SDK
- Appium
- Python com ambiente virtual

## Como executar
1. Ative o ambiente virtual: `source venv/bin/activate`
2. Inicie o Appium: `appium`
3. Inicie o emulador: `/home/<seu_usuario>/Android/Sdk/emulator/emulator -avd Pixel_4`
4. Execute: `pytest tests/test_calculator.py -v --html=report.html`

## Resultados
- Tempo de execução: ~4.58 segundos
- Relatório: `report.html`

## CI/CD
Configurado com GitHub Actions (`.github/workflows/test.yml`).
