# Raspberry PI examples

- [Raspberry PI examples](#raspberry-pi-examples)
  - [Setup](#setup)
    - [Install micropython](#install-micropython)
    - [VSCode](#vscode)
    - [Pipkin](#pipkin)
  - [Base Components](#base-components)
  - [Examples](#examples)
    - [2x16 LCD I2C](#2x16-lcd-i2c)
      - [Components](#components)
    - [motion sensor](#motion-sensor)
      - [Components](#components-1)
    - [onboard led](#onboard-led)
      - [Components](#components-2)
    - [SSD1306 OLED I2C](#ssd1306-oled-i2c)
      - [Components](#components-3)

## Setup

Most examples in this repo are built for boards with `RP2040` chipset, does not really matter if it's a Raspberry or something else, as long as chipset on that board is `RP2040`.

### Install micropython

Depending on the board installation may slightly differ, but it will usually boil down to running board in boot mode so it can be recognised as USB storage device, to which micropython `*.uf2` file will have to be copied.  

For detailed instructions see either board vendor instructions, micropython docs or [raspberry pi](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) docs.

### VSCode

I highly recommend using [VSCode](https://code.visualstudio.com/) over [Thonny](https://thonny.org/) (despite that second one is usually recommended as the default IDE for working with micropython).

In order to be able to push code to board you can use [MicroPico](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go) extension.

### Pipkin

In order to use specific libraries on board you might need to install them on the board.
[Pipkin](https://pypi.org/project/pipkin/) makes this task as easy as:

```shell
pip install pipkin
```

and from there all you need is for example:

```shell
pipkin install picozero
```

## Base Components

> Affiliate link disclaimer!  
> Links to components in examples are affiliate links. If you buy component using any of those, you won't pay more, but I'll get a cut, which will allow me to add more examples.

Vast majority of examples are built using breadboard, some jumper wires and wither RaspberryPi Pico W or RP2040-Zero.

- [RP Pico W - Amazon](https://amzn.to/47xPdUn)
- [RP Pico W - AliExpress](https://s.click.aliexpress.com/e/_DdLnsb9)
- [RP2040-Zero - Amazon](https://amzn.to/3T4GuEL)
- [RP2040-Zero - AliExpress](https://s.click.aliexpress.com/e/_DFgT0A3)
- [Breadboard - Amazon](https://amzn.to/3T40MOB)
- [Breadboard - Aliexpress](https://s.click.aliexpress.com/e/_DdgjI0R)
- [Jumper Wires - Amazon](https://amzn.to/3uEfdPm)
- [Jumper Wires - AliExpress](https://s.click.aliexpress.com/e/_DmMPHxt)

## Examples

### [2x16 LCD I2C](./2x16_lcd_i2c/)

[This](./2x16_lcd_i2c/main.py) example uses `2x16 LCD` with `I2C` module already soldered in.

> This example uses external libraries to communicate with display using I2C:
>
> - [python_lcd](https://github.com/dhylands/python_lcd)
> - [RPI-PICO-I2C-LC](https://github.com/T-622/RPI-PICO-I2C-LCD)
>
> You will need two files from those repos:
>
> - [lcd_api](https://github.com/dhylands/python_lcd/blob/master/lcd/lcd_api.py)
> - [pico_i2c_lcd](https://github.com/T-622/RPI-PICO-I2C-LCD/blob/main/pico_i2c_lcd.py)
>
> copy them over to your project, and make sure to also send it to board

#### Components

- [2x16 LCD - Amazon](https://amzn.to/3Rw1CTn)
- [2x16 LCD - AliExpress](https://s.click.aliexpress.com/e/_DFjEm4n)

---

### [motion sensor](./motion_sensor/)

[This](./motion_sensor/machine.py) example uses `HC-SR501` motion sensor.  
[Second example](./motion_sensor/picozero.py) uses same sensor, but instead of relying only on micropython built in code, this one uses [picozero](https://picozero.readthedocs.io/en/latest/api.html) library.

#### Components

- [HC-SR501 - Amazon](https://amzn.to/49VN6LF)
- [HC-SR501 - AliExpress](https://s.click.aliexpress.com/e/_DdMvH6X)

---

### [onboard led](./onboard_led/)

[This](./onboard_led/main.py) example uses `RP2040-Zero` onboard led (type `ws2812`).  
[Second example](./onboard_led/with_button.py) additionally uses tactile switch (both `6x6 mm` and `12x12 mm` will to just fine).

#### Components

- [6x6mm - Amazon](https://amzn.to/40ZcyM2)
- [6x6mm - AliExpress](https://s.click.aliexpress.com/e/_DDdD25t)
- [12x12mm - Amazon](https://amzn.to/3uBck1R)
- [12x12mm - AliExpress](https://s.click.aliexpress.com/e/_DBB46B5)

### [SSD1306 OLED I2C](./ssd1306_oled/)

[This](./ssd1306_oled/main.py) example uses `SSD1306` 128x32 OLED I2C display.

> This example uses external library to communicate with display using I2C:
>
> - [ssd1306.py](https://www.hackster.io/diyprojectslab/how-to-use-an-oled-display-with-raspberry-pi-pico-d9d9cb)

#### Components

- [SSD1306 128x32 - Amazon](https://amzn.to/47aSBmV)
- [SSD1306 128x32 - AliExpress](https://s.click.aliexpress.com/e/_DdGpOTj)