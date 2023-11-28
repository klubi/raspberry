# Raspberry PI examples

- [Raspberry PI examples](#raspberry-pi-examples)
  - [Setup](#setup)
    - [Install micropython](#install-micropython)
    - [VS Code](#vs-code)
    - [Pipkin](#pipkin)
  - [Base Components](#base-components)
  - [Examples](#examples)
    - [PIR motion sensor](#pir-motion-sensor)
      - [Components](#components)
    - [Onboard led](#onboard-led)
      - [Components](#components-1)

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

### [PIR motion sensor](./motion_sensor/)

[This](./motion_sensor/machine.py) example uses `HC-SR501` motion sensor.  
[Second example](./motion_sensor/picozero.py) uses same sensor, but instead of relying only on micropython built in code, this one uses [picozero](https://picozero.readthedocs.io/en/latest/api.html) library.

#### Components

- [HC-SR501 - Amazon](https://amzn.to/49VN6LF)
- [HC-SR501 - AliExpress](https://s.click.aliexpress.com/e/_DdMvH6X)

### [Onboard led](./onboard_led/)

[This](./onboard_led/main.py) example uses `RP2040-Zero` onboard led (type `ws2812`).  
[Second example](./onboard_led/with_button.py) additionally uses tactile switch (both `6x6 mm` and `12x12 mm` will to just fine).

#### Components

- [6x6mm - Amazon](https://amzn.to/40ZcyM2)
- [6x6mm - AliExpress](https://s.click.aliexpress.com/e/_DDdD25t)
- [12x12mm - Amazon](https://amzn.to/3uBck1R)
- [12x12mm - AliExpress](https://s.click.aliexpress.com/e/_DBB46B5)