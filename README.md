# tensor_test_task

Тестовый проект на Python с использованием pytest и Selenium
Проект представляет собой набор тестовых сценариев для веб-приложений Tensor.ru и Sbis.ru с использованием библиотек pytest и Selenium.

## Используемые модули

- `selenium`
- `pytest`
- `requests`

## Установка

1. Склонируйте проект с помощью Git:

   ```bash
   git clone https://github.com/sachaek/tensor_test_task.git
   cd tensor_test_task
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Установите Chromedriver для вашей операционной системы 
   Описано здесь: https://habr.com/ru/articles/248559/
4. Запустите тесты
   ```bash
   pytest test_sbis_and_tensor_3_scenarios.py
