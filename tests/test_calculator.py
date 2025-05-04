from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Configurar logging para depuração
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações do Appium (Desired Capabilities usando AppiumOptions)
def get_capabilities():
    options = UiAutomator2Options()
    options.platform_name = "Android"  # Garantir que está corretamente configurado
    options.platform_version = "13"  # Android 13 (API 33)
    options.device_name = "emulator-5554"  # Confirmar com `adb devices`
    options.app_package = "com.google.android.calculator"  # Pacote do app
    options.app_activity = "com.google.android.calculator/.Calculator"  # Atividade do app
    options.automation_name = "UiAutomator2"  # Nome da automação
    options.no_reset = True  # Não resetar o app entre os testes
    options.new_command_timeout = 300  # Timeout para comandos
    logger.info("Capabilities configuradas: %s", options.to_capabilities())
    return options

def test_calculator_sum():
    # Iniciar contagem de tempo
    start_time = time.time()

    # Conectar ao Appium
    try:
        driver = webdriver.Remote("http://localhost:4723", options=get_capabilities())
        logger.info("Conexão com Appium estabelecida com sucesso")
    except Exception as e:
        logger.error("Erro ao conectar ao Appium: %s", str(e))
        raise

    try:
        # Esperar o aplicativo carregar
        wait = WebDriverWait(driver, 10)

        # Clicar no botão "2"
        button_2 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/digit_2")))
        button_2.click()
        logger.info("Clicou no botão '2'")

        # Clicar no botão "+"
        button_plus = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/op_add")))
        button_plus.click()
        logger.info("Clicou no botão '+'")

        # Clicar no botão "2" novamente
        button_2 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/digit_2")))
        button_2.click()
        logger.info("Clicou no botão '2' novamente")

        # Clicar no botão "="
        button_equals = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/eq")))
        button_equals.click()
        logger.info("Clicou no botão '='")

        # Obter o resultado
        result = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/result_final")))
        result_text = result.text
        logger.info("Resultado obtido: %s", result_text)

        # Verificar se o resultado é "4"
        assert result_text == "4", f"Esperado '4', mas obteve '{result_text}'"

        # Calcular tempo de execução
        execution_time = time.time() - start_time
        print(f"Teste concluído: 2 + 2 = 4 (Tempo: {execution_time:.2f} segundos)")

    finally:
        # Fechar o driver
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
