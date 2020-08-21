# IoT_bulglar_alarm
A system managing PIR sensor, LEDs, a buzzer with MQTT to send information about movements.

## Detailed description
The idea of the IoT system was to prevent a precious thing from a thief. There are two ESP32 boards - one is connected to a PIR sensor, 10 red LEDs and a buzzer (_IoT_infrared.py_ file), the other one to some buttons, two red LEDs and a green one (_IoT_buttons.py_ file). The first board is placed near to the precious thing, the second is a control panel for the owner. With the panel the owner can turn on, turn off or desactivate the alarm system. When the PIR sensor senses some movement while the system is activated, then 10 LEDs begin to blink, the buzzer starts making the alert sound and the red LED on the owner's control panel turns on to inform about the system's state. The ESPs communicate with each other via MQTT communication protocol (with publisher-subsriber architecture). All functions are implemented using Python language (microPython).

## Authors
* **Emilia Szymańska** & **Nicolas Whittaker** - main _software_ and _hardware_ implementation 
* **Sarah Mazzone** & **Claire Penot** - _designing the system_
