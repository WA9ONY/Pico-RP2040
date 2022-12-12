# Raspberry Pi Pico & RP2040 Microcontroller Projects
[David Haworth](http://www.stargazing.net/david/index.html), [WA9ONY](https://www.qrz.com/db/WA9ONY)

## RP2040 Microcontroller Introduction

Rasperry Pi Pico boards area  new popular low cost, powerful [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) that was created for education, makers, hobbyiest, etc. in January 2021. In less than two years over 2 million have been sold.  The RP2040 is the microcontroller IC used in the Pico boards.  The RP2040 is sold for $1 and is used by many other companies to create boards that include the RP2040.

The RP2040 is a dual core, 32-bit [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family) Cortex M0+ processor that has very low power requirements. Therefore, it is a good choice for battery operation.

The Raspberry Pi [SBC](https://en.wikipedia.org/wiki/Single-board_computer), single board computers, are the third most popular personal computer behind Apple Mac OS, and Window PCs.  A SBC runs an operation system to interface to the user and runs various programs.  In contrast the RP2040 is a [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) design to interface to hardware to do a signal task. 

To use a microcontroller it is connected to additional electrical hardware using digital I/O, analog I/O, buses ([I2C](https://en.wikipedia.org/wiki/I%C2%B2C), [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface), [UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter), etc.). A compuer is used to develop the software to run one the microcontroller. The software is downloaded from the computer to the microcontroller board where is runs.  The software is saved on flash memory on the microcontroller board and runs when the board is power up and not connected to the computer.  When problems occur the computer is connected to the microcontroller board to debug it.

## [Raspberry Pi Foundation](https://en.wikipedia.org/wiki/Raspberry_Pi_Foundation)

Raspberry Pi Foundation helped redefine the personal computer market with the [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi) low cost single board computer running Linux.
In January 2021, Raspberry Pi Foundation entered the microcontroller market with a high performace low cost (1$ single unit) microcontroller RP2040 and its boards.  Raspberry Pi Foundation make the RB2040 available to other companies: Adafruit, Sparkfun, Ardinuo, etc. This has caused a explosion of low cost microcontroller [boards](https://en.wikipedia.org/wiki/RP2040) that include the RP2040.

[Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) boards
+ [Pico $4](https://www.adafruit.com/product/4864) Has Rp2040, clock chip, flash chip and 3.3V regulator chip
+ [Pico H $5](https://www.adafruit.com/product/5525) Adds two 20 pin headers to the Pico.
+ [Pico W $6](https://www.adafruit.com/product/5526) Adds WiFy chip to the Pico
+ [Pico WH $7](https://www.adafruit.com/product/5544) dds two 20 pin headers to the Pico W.
+ [RB2040 $1](https://www.adafruit.com/product/5041) Just the RP2040 chip.

Wikipedia
+ [Raspberry Pi Pico](https://en.wikipedia.org/wiki/Raspberry_Pi#Raspberry_Pi_Pico)
+ [RP2040](https://en.wikipedia.org/wiki/RP2040)

### Videos
+ Exploring the Next Generation of Arduino Microcontrollers (Pico) [video](https://www.youtube.com/watch?v=HOi_AYEgSmo) - Glen Popiel, KW5GP
+ YouTube: Raspberry Pi Pico [list](https://www.youtube.com/results?search_query=raspberry+pi+pico)

### Books
+ Get Started with MicroPython on Raspberry Pi Pico [free PDF](https://hackspace.raspberrypi.com/books/micropython-pico)
+ Raspberry Pi Pico for Radio Amateurs ([print & E-book](https://www.elektor.com/raspberry-pi-pico-for-radio-amateurs-e-book)) color PDF 307 pages. 201 project pages 
+ Amazon Pico book [list](https://www.amazon.com/s?k=raspberry+pi+pico+book&crid=3TYSWPL6AAMTA&sprefix=raspberry+pi+pico+book%2Caps%2C146&ref=nb_sb_noss_1)

### Magazines
+ Hackspace issue [39, 40, 44](https://hackspace.raspberrypi.com/issues?page=2), [52, 57, 61](https://hackspace.raspberrypi.com/issues?page=1)
+ MagPi issue [109](https://magpi.raspberrypi.com/issues?page=2), [119, 121](https://magpi.raspberrypi.com/issues)
+ [Make](https://makezine.com/) magazine volumn 83 contains the 2022 annual Boards Guide (79 boards) on microcontrollers and SBCs. Back issues are availale with a digital subscription.

### Internet Archive Raspberry Pi Pico [list](https://archive.org/search.php?query=Raspberry%20Pi%20Pico)

### GitHub Repo
+ [WA9ONY/Raspberry_Pi_Pico_RP2040](https://github.com/WA9ONY/Raspberry_Pi_Pico_RP2040)
+ Over 3,100 Raspberry Pi Pico [repositories](https://github.com/search?q=Raspberry+Pi+Pico)
  +[raspberrypi/pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples)
+ [SSH key for GitHub](https://garywoodfine.com/setting-up-ssh-keys-for-github-access/) files upload

### Small list from >40 RP2040 boards
+ [Adafruit](https://www.adafruit.com/)
  + [RP2040s](https://www.adafruit.com/?q=RP2040&sort=BestMatch)
  + [Adafruit P4884 Feather RP2040](https://www.adafruit.com/product/4884)
  + [Adafruit P4888 ItsyBitsy RP2040](https://www.adafruit.com/product/4888)
  + [Adafruit P4900 QT Py RP2040](https://www.adafruit.com/product/4900)
  + [Adafruit P5056 Trinkey QT2040 - RP2040 USB Key with Stemma QT](https://www.adafruit.com/product/5056)
  + [Adafruit P5302 KB2040 - RP2040 Kee Boar Driver](https://www.adafruit.com/product/5302)
  + STEMMA QT [video](https://www.youtube.com/watch?v=6GXRRuFuFy0)
  + [Circuitpython library](https://www.adafruit.com/category/956)
  
![Arduino Nanao RP240 Connect](/Images/arduinoNanoM.jpg)
<center>Arduino Nano RP2040 Connect</center>
+ [Arduino](https://www.arduino.cc/)
  + [Arduino Nano RP2040 Connect](https://store-usa.arduino.cc/products/arduino-nano-rp2040-connect-with-headers)
  + [YouTube Short First power on by WA9ONY](https://www.youtube.com/shorts/O2xxTe2i11w)
+ [SparkFun](https://www.sparkfun.com/)
  + [RP2040s](https://www.sparkfun.com/search/results?term=RP2040)
  + [SparkFun Pro Micro - RP2040](https://www.sparkfun.com/products/18288)
  + [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/products/17745)
  + [WizFi360-EVB-Pico](https://www.sparkfun.com/products/19959)
  + [W5500-EVB-Pico](https://www.sparkfun.com/products/19958)
+ [Seeed Studio](https://www.seeedstudio.com/)
  + [RP2040s](https://www.seeedstudio.com/catalogsearch/result/?q=rp2040)
  + [XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html?queryID=9178e9456690e66382d9d6934ff4ae0a&objectID=5026&indexName=bazaar_retailer_products)
+ [Waveshare](https://www.waveshare.com/)
  + [RP2040s](https://www.waveshare.com/catalogsearch/result/?q=RP2040)
  + [RP2040-Zero](https://www.waveshare.com/rp2040-zero.htm)
  + [RP2040-One](https://www.amazon.com/gp/product/B0BLMPDMLD/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
  + [RP2040-Plus Mini Board](https://www.amazon.com/dp/B0B6BM7CVT?psc=1&smid=A2SA28G0M1VPHD&ref_=chk_typ_imgToDp)

### Software
+ [Python](https://www.python.org/), [Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
  - [Micropython](https://micropython.org/)
    * [MicroPython on the Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
    * [Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
    * [Quick reference for the RP2](https://docs.micropython.org/en/latest/rp2/quickref.html)
  - [Circuitpython](https://circuitpython.org/)
    * CircuitPython School 57 [videos](https://www.youtube.com/playlist?list=PL9VJ9OpT-IPSsQUWqQcNrVJqy4LhBjPX2) by John Gallaugher
+ C, [Wikipedia](https://en.wikipedia.org/wiki/C_(programming_language)) and [C++](https://isocpp.org/), [Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
  - [The C/C++ SDK](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)
+ Arduino
  - [Web Editor](https://docs.arduino.cc/arduino-cloud/getting-started/getting-started-web-editor#getting-started-with-the-web-editor) need a Arduino Agent to communicate between the browser and Arduino board.
    * WA9ONY uses Web Editor on Chrome on Ubuntu 22.04.1 LTS, Intel NUC8i7HVK computer
  - [IDE V1.8](https://www.arduino.cc/en/software) Legacy
  - [IDE V2](https://www.arduino.cc/en/software) is 64-bit
    * [Guide](https://www.arduino.cc/en/Guide)
    + Supports Arduino & Raspberry Pi Pico libraries
    - [IDE V2 on Raspberry Pi](https://forum.arduino.cc/t/arduino-ide-2-0-0-on-raspberry-pi/855695)
+ Assembly
  - [RP2040 Assembly Language Programming: ARM Cortex-M0+ on the Raspberry Pi Pico](https://www.amazon.com/RP2040-Assembly-Language-Programming-Cortex-M0/dp/148427752X/ref=sr_1_1?crid=10C0D1RJF1EMB&keywords=raspberry+pi+pico+assembly+language+programming&qid=1670506014&sprefix=Raspberry+Pi+Pico+ass%2Caps%2C158&sr=8-1) 1st ed. Edition
    * Shows how to mix assembly with C in a program
 
 
## Arduino Microcontroller 
### Overview 
[Arduino](https://www.arduino.cc/) is a popular microcontroller that was created for education in ~2003. Over 10 million Uno boards have been sold since 2010.  

Arduino supports the RP2040 with the Arduino [Nano RP2040 Connect](https://store-usa.arduino.cc/products/arduino-nano-rp2040-connect-with-headers). 
+ Wikipedia: [Arduino](https://en.wikipedia.org/wiki/Arduino)

### Videos
+ Exploring the Next Generation of Arduino Microcontrollers (Pico) [video](https://youtu.be/HOi_AYEgSmo) - Glen Popiel, KW5GP
+ YouTube video [list](https://www.youtube.com/results?search_query=Arduino): Arduino
  - New Arduino Tutorials [List](https://www.youtube.com/playlist?list=PLGs0VKk2DiYw-L-RibttcvK-WBZm8WLEP) 68 videos

### Books
+ [Get Started With Arduino](https://hackspace.raspberrypi.com/articles/get-started-with-arduino-book) free PDF
+ ARRL
  - [Arduino](https://www.arrl.org/arduino) 352 pages by KW5GP
  - [Arduino 2](https://www.arrl.org/arduino2) 500 pages by KW5GP
Amazon Arduino Ham Radio Projects book [list](https://www.amazon.com/s?k=arduino+ham+radio&crid=YSCCY2436JXJ&sprefix=arduino+ham%2Caps%2C157&ref=nb_sb_ss_ts-doa-p_1_11)

### Magazines
+ Hackspace issue [30](https://hackspace.raspberrypi.com/issues?page=3), [44](https://hackspace.raspberrypi.com/issues?page=2)
+ Internet Archive Arduino [list](https://archive.org/search.php?query=Arduino&sin=)


## WA9ONY Projects

### Project 1: TBD
#### Objective

### Project 2: TBD
#### Objective


73 David Haworth WA9ONY
