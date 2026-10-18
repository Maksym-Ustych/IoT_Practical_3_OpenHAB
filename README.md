# Практична робота 3.1 — Протоколи зв'язку в IoT

## Мультипротокольна погодна станція

Мета роботи — розробити в OpenHAB емулятор IoT-системи, яка демонструє роботу трьох протоколів зв'язку: MQTT, HTTP REST API та BLE.

У проєкті передбачено:
- MQTT-телеметрію погодних даних;
- HTTP REST API емуляцію;
- BLE емуляцію датчиків і beacon;
- інтеграцію даних у OpenHAB;
- тестування та аналіз роботи протоколів.

## MQTT

Для обміну даними використовується локальний MQTT-брокер Mosquitto та MQTT Binding в OpenHAB.

Створені MQTT-канали:
- температура — `weather_station/sensors/temperature`;
- вологість — `weather_station/sensors/humidity`;
- атмосферний тиск — `weather_station/sensors/pressure`;
- RSSI — `weather_station/status/rssi`;
- стан лампи — `weather_station/devices/lamp/state`;
- яскравість лампи — `weather_station/devices/lamp/brightness/state`;
- стан вентилятора — `weather_station/devices/fan/state`.

Для перевірки передавання повідомлень використано QoS 1 та параметр retain.

Тестові значення:
- температура — 23.7;
- вологість — 56;
- тиск — 1013.2;
- RSSI — -48 dBm;
- лампа — ON;
- яскравість — 75%;
- вентилятор — ON.

### Тестування MQTT

![MQTT testing](docs/mqtt_testing.jpg)

## HTTP REST API

Для емуляції HTTP REST API створено локальний Python-сервер на порту `8090`.

Використані endpoints:
- `/current` — температура, вологість і атмосферний тиск;
- `/status` — стан системи;
- `/devices` — стан лампи, яскравість і вентилятор.

У OpenHAB створено HTTP URL Thing з базовою адресою:

`http://localhost:8090`

Для обробки JSON-відповідей використано JSONPath Transformation.

Створені HTTP-канали:
- HTTP Температура;
- HTTP Вологість;
- HTTP Тиск;
- HTTP Статус;
- HTTP Лампа;
- HTTP Яскравість;
- HTTP Вентилятор.

### HTTP Channels

![HTTP channels](docs/http_channels.jpg)
