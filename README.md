# Raspberry Pi Pico & RP2040 Microcontroller Projects

<p align="center">
  <img width="739" height="337" src="/Images/picoS.jpg">  
</p>

[David Haworth](http://www.stargazing.net/david/index.html), [WA9ONY](https://www.qrz.com/db/WA9ONY)

## RP2040 Microcontroller Introduction

Rasperry Pi Pico boards area  new popular low cost, powerful [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) that was created for education, makers, hobbyiest, etc. in January 2021. In less than two years over 2 million have been sold.  The RP2040 is the microcontroller IC used in the Pico boards.  The RP2040 is sold for $1 and is used by many other companies to create boards that include the RP2040.

The RP2040 is a dual core, 32-bit [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family) Cortex M0+ processor that has very low power requirements. Therefore, it is a good choice for battery operation.

The Raspberry Pi [SBC](https://en.wikipedia.org/wiki/Single-board_computer), single board computers, are the third most popular personal computer behind Apple Mac OS, and Window PCs.  A SBC runs an operation system to interface to the user and runs various programs.  In contrast the RP2040 is a [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) design to interface to hardware to do a signal task. 

To use a microcontroller it is connected to additional electrical hardware using digital I/O, analog I/O, buses ([I2C](https://en.wikipedia.org/wiki/I%C2%B2C), [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface), [UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter), etc.). A compuer is used to develop the software to run one the microcontroller. The software is downloaded from the computer to the microcontroller board where is runs.  The software is saved on flash memory on the microcontroller board and runs when the board is power up and not connected to the computer.  When problems occur the computer is connected to the microcontroller board to debug it.

<p align="center">
  <img align="right" width="215" height="53" src="/Images/rpiLogo.png"> 
</p>

## [Raspberry Pi Foundation](https://en.wikipedia.org/wiki/Raspberry_Pi_Foundation)

Raspberry Pi Foundation helped redefine the personal computer market with the [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi) low cost single board computer running Linux.
In January 2021, Raspberry Pi Foundation entered the microcontroller market with a high performace low cost (1$ single unit) microcontroller RP2040 and its boards.  Raspberry Pi Foundation make the RP2040 available to other companies: Adafruit, Sparkfun, Ardinuo, etc. This has caused a explosion of low cost microcontroller [boards](https://en.wikipedia.org/wiki/RP2040) that include the RP2040.

<p align="center">
  <img width="640" height="161" src="/Images/picoPicoW.jpg">  
</p>
The board on the left is a Pico and the board on the right is a Pico W.  Both boards have pins soldered on them.

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
+ YouTube
  + Raspberry Pi Pico [list](https://www.youtube.com/results?search_query=raspberry+pi+pico)
  + ExplainingComputers Pico [list](https://www.youtube.com/@ExplainingComputers/search?query=Pico)

### Books
+ Get Started with MicroPython on Raspberry Pi Pico [free PDF](https://hackspace.raspberrypi.com/books/micropython-pico)
+ Amazon Pico book [list](https://www.amazon.com/s?k=raspberry+pi+pico+book&crid=3TYSWPL6AAMTA&sprefix=raspberry+pi+pico+book%2Caps%2C146&ref=nb_sb_noss_1)
+ Raspberry Pi Pico for Radio Amateurs ([print & E-book](https://www.elektor.com/raspberry-pi-pico-for-radio-amateurs-e-book)) color PDF 307 pages. 201 project pages
  + Station mains power on/off control
  + Radio station clock
  + GPS based station geographical coordinates
  + Radio station temperature and humidity
  + Various waveform generation methods using software and hardware (DDS)
  + Frequency counter
  + Voltmeter / ammeter / ohmmeter / capacitance meter
  + RF meter and RF attenuators
  + Morse code exercisers
  + RadioStation Click board
  + Raspberry Pi Pico based FM radio
  + Using Bluetooth and Wi-Fi with Raspberry Pi Pico
  + Radio station security with RFID
  + Audio amplifier module with rotary encoder volume control
  + Morse decoder
  + Using the FS1000A TX-RX modules to communicate with Arduino   

### Magazines
+ Hackspace issue [39, 40, 44](https://hackspace.raspberrypi.com/issues?page=2), [52, 57, 61](https://hackspace.raspberrypi.com/issues?page=1)
+ MagPi issue [109](https://magpi.raspberrypi.com/issues?page=2), [119, 121](https://magpi.raspberrypi.com/issues)
+ [Make](https://makezine.com/) magazine volumn 83 contains the 2022 annual Boards Guide (79 boards) on microcontrollers and SBCs. Back issues are availale with a digital subscription.

### Internet Archive Raspberry Pi Pico [list](https://archive.org/search.php?query=Raspberry%20Pi%20Pico)

### Pico & RP2040 boards (>40) lists

+ Wikipedia list on [RP2040]([https://en.wikipedia.org/wiki/Adafruit_Industries](https://en.wikipedia.org/wiki/RP2040))
+ Earle F. Philhower, III GitHub [supported RP2040 boards](https://github.com/earlephilhower/arduino-pico)
+ Tom's Hardware [Best RP2040 Boards 2022](https://www.tomshardware.com/best-picks/best-rp2040-boards)
+ Electromaker [RP2040 Board Comparison - Which RP2040 Board Should You Buy](https://www.electromaker.io/blog/article/rp2040-board-comparison-which-rp2040-board-should-you-buy)
+ Electromaker [Electromakers guide to boards 2022](https://www.electromaker.io/board-guide?type=microcontroller&processor=RP2040)
+ Electromaker [Top 5 Alternatives to Raspberry Pi Pico](https://www.electromaker.io/blog/article/top-5-alternatives-to-raspberry-pi-pico)
+ Renzo Mischianti [Raspberry Pi Pico, W, and other rp2040 boards: pinout, specs, and Arduino IDE configuration – 1](https://www.mischianti.org/2022/09/26/raspberry-pi-pico-w-and-other-rp2040-boards-pinout-specs-and-arduino-ide-configuration-1/)
+ MUO [11 Alternatives to the Raspberry Pi Pico](https://www.makeuseof.com/alternatives-to-the-raspberry-pi-pico/)
+ All3DP [The Best RP2040 Boards of 2022 – Buyer’s Guide](https://all3dp.com/2/rp2040-board-buyers-guide/)

<p align="center">
  <img align="right" width="220" height="75" src="/Images/Adafruit_logo.svg.png"> 
</p>

#### [Adafruit Industries](https://www.adafruit.com/) [RP2040s](https://www.adafruit.com/?q=RP2040&sort=BestMatch)

<p align="center">
  <img width="479" height="229" src="/Images/AdafruitRP2040.jpg"> 
</p>

Adafruit [(Wikipedia)](https://en.wikipedia.org/wiki/Adafruit_Industries) is develops and sells open source hardware and is localed in New Your city. Adafruit is an offical distributer of Raspberry Pi products.  Therefore, they sell the Raspberry Pi Pico family of products and the Raspberry Pi SBC produccts. Also, Adafruit develops there own RP2040

Above photo left to right:
+ [Adafruit P4884 Feather RP2040](https://www.adafruit.com/product/4884) with STEMMA QT
+ [Adafruit P4888 ItsyBitsy RP2040](https://www.adafruit.com/product/4888)
+ [Adafruit P4900 QT Py RP2040](https://www.adafruit.com/product/4900) with STEMMA QT
+ [Adafruit P5056 Trinkey QT2040 - RP2040 USB Key with Stemma QT](https://www.adafruit.com/product/5056) with STEMMA QT
+ [Adafruit P5302 KB2040 - RP2040 Kee Boar Driver](https://www.adafruit.com/product/5302) with STEMMA QT

Some Adafriut product are available on Amazon.

Adafruit STEMMA QT is a easy to use (no soldering) I2C interface with small connectors on sensor boards and some RP2040 boards.
+ STEMMA QT [video](https://www.youtube.com/watch?v=6GXRRuFuFy0)

<p align="center">
  <img width="300" height="132" src="/Images/circuitpython.jpg"><img width="108" height="111" src="/Images/micropython.png">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img width="300" height="90" src="/Images/python.png">  
</p>

Adafruit CircuitPython is based on [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) and is a fork of [MicroPython](https://micropython.org/) that support the Adafruit RP2040 boards, Raspberry Pi Pico boards (Adafruit sells them) and the large selection of Adafriut sensors boards.  CircuitPython works great with the Mu IDE.  CircuitPython has RP2040 functions like deep sleep that are not in CircuitPython.
+ [CircuitPython](https://circuitpython.org/)
  + [Getting Started with Raspberry Pi Pico and CircuitPython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython)
  + [CircuitPython library](https://www.adafruit.com/category/956) >280 Python libraries.

<p align="center">
  <img align="right" width="74" height="57" src="/Images/arduinoLogo.png"> 
</p>

#### [Arduino](https://www.arduino.cc/) Nano RP2040 Connect

<p align="center">
  <img width="640" height="278" src="/Images/arduinoNanoM.jpg">  
</p>

+ Above photo is an [Arduino Nano RP2040 Connect](https://store-usa.arduino.cc/products/arduino-nano-rp2040-connect-with-headers)
+ [YouTube Short First power on by WA9ONY](https://www.youtube.com/shorts/O2xxTe2i11w)
+ Arduino RP2040 librar [list](https://www.arduinolibraries.info/architectures/rp2040)

<p align="center">
  <img align="right" width="169" height="83" src="/Images/sparkfunLogo.png"> 
</p>

#### [SparkFun](https://www.sparkfun.com/)
Some SparkFun products are available from [Amazon](https://www.amazon.com/s?k=SparkFun&crid=6GWYUPXP9EMB&sprefix=sparkfun%2Caps%2C310&ref=nb_sb_noss_1)
  + [RP2040s](https://www.sparkfun.com/search/results?term=RP2040)
  + [SparkFun Pro Micro - RP2040](https://www.sparkfun.com/products/18288)
  + [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/products/17745)
  + [WizFi360-EVB-Pico](https://www.sparkfun.com/products/19959)
  + [W5500-EVB-Pico](https://www.sparkfun.com/products/19958)

<p align="center">
  <img align="right" width="225" height="54" src="/Images/seedstudioLogo.png"> 
</p>

#### [Seeed Studio](https://www.seeedstudio.com/)
Some Seeed Studio products are available from [Amazon](https://www.amazon.com/s?k=Seeed+Studio&crid=PQF86EWIGSXL&sprefix=seeed+studio%2Caps%2C197&ref=nb_sb_noss_1)
+ [RP2040s](https://www.seeedstudio.com/catalogsearch/result/?q=rp2040)
+ [XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html?queryID=9178e9456690e66382d9d6934ff4ae0a&objectID=5026&indexName=bazaar_retailer_products)

<p align="center">
  <img align="right" width="299" height="61" src="/Images/waveshareLogo.png"> 
</p>

#### [Waveshare](https://www.waveshare.com/)
Some Waveshare products are available from [Amazon](https://www.amazon.com/s?k=Waveshare&crid=AJL406YJVRKX&sprefix=waveshare%2Caps%2C136&ref=nb_sb_noss_1)
+ [RP2040s](https://www.waveshare.com/catalogsearch/result/?q=RP2040)
+ [RP2040-Zero](https://www.waveshare.com/rp2040-zero.htm)
+ [RP2040-One](https://www.amazon.com/gp/product/B0BLMPDMLD/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
+ [RP2040-Plus Mini Board](https://www.amazon.com/dp/B0B6BM7CVT?psc=1&smid=A2SA28G0M1VPHD&ref_=chk_typ_imgToDp)

### Software
+ [Python](https://www.python.org/), [Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
  - [MicroPython](https://micropython.org/)
    * [MicroPython on the Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
    * [Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
    * [Quick reference for the RP2](https://docs.micropython.org/en/latest/rp2/quickref.html)
    * [Raspberry Pi Pico RP2040 Programming in MicroPython with Examples](https://www.electroniclinic.com/raspberry-pi-pico-rp2040-programming-in-micropython-with-examples/)
    * Digi-Key Tutorials
    *   Raspberry Pi Pico and RP2040 - MicroPython Part 1: Blink [tutorial](https://www.digikey.com/en/maker/projects/raspberry-pi-pico-and-rp2040-micropython-part-1-blink/58b3c31ac93649849b58824caa00529c)
    *   Raspberry Pi Pico and RP2040 - MicroPython Part 2: I2C Sensor and Module [tutorial](https://www.digikey.com/en/maker/projects/raspberry-pi-pico-and-rp2040-micropython-part-2-i2c-sensor-and-module/b43e7958153f41fc9e7403df4d626ba5)
  - [CircuitPython](https://circuitpython.org/)
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
 
 ### GitHub Repo
+ [WA9ONY/Raspberry_Pi_Pico_RP2040](https://github.com/WA9ONY/Raspberry_Pi_Pico_RP2040)
+ Over 3,100 Raspberry Pi Pico [repositories](https://github.com/search?q=Raspberry+Pi+Pico)
  + [raspberrypi/pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples)
+ YouTube git & GitHub [list](https://www.youtube.com/results?search_query=GitHub)
 
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

# WA9ONY Projects

## Project 1: Build a Computer for Micorocontroller Development

<p align="center">
  <img width="640" height="480" src="/Images/P400.jpg">  
</p>

To use the Pico a computer with a Pico [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) is needed.
To use the Pico.
1. Create a Pico program in the IDE.
2. Download the program into the Pico.
3. Run the program.
4. Debug the program in the IDE.

### Goals
The computer needs to run these ADE
+ MicroPython - Thonny IDE
+ Circuitpython - Mu IDE

Use Raspberry Pi P400 computer.
Create a new microSD card with latest OS with full install.
The full install includes Thonny and Mu.

## Project 2: Setup Git and GitHub

<p align="center">
  <img width="640" height="480" src="/Images/GitHub.jpg">  
</p>

GitHub is a great way to document and share Pico projects.
The GitHub home READ.md file provides a place to documenting the Pico projects.
The GitHub provides free file storage ([repository](https://en.wikipedia.org/wiki/Repository_(version_control))) and version change control.
GitHub is used by a web interface or a Linux CLI.
The Raspberry Pi P400 full install includes git.

### Goals
+ Use git CLI on the computer.
+ Use GitHub web interface.
+ Create Raspberry Pi Pico and RP2040 repo.
+ Create a README.md file describing Pico/RP2030 projects and resources.

### Resources
+ Articles
  + TBD
  + Wikipedia
    + [RGitHub]([https://en.wikipedia.org/wiki/Raspberry_Pi#Raspberry_Pi_Pico](https://en.wikipedia.org/wiki/GitHub))
  + [SSH key for GitHub](https://garywoodfine.com/setting-up-ssh-keys-for-github-access/) files upload
+ Videos
  + YouTube [list](https://www.youtube.com/results?search_query=GitHub)
+ Books
  +Amazon [list](https://www.amazon.com/s?k=Github+in+books&crid=2SACFZLPDLFD9&sprefix=github+in+books%2Caps%2C148&ref=nb_sb_noss_1)   

## Project 3 : Learn Micropython on the Pico

<p align="center">
  <img width="333" height="499" src="/Images/GetStartedWithMicroPythonOnRaspberryPiPico.png">  
</p>

### Goals
+ Learn how to program the Pico in [MicropPython](https://micropython.org/).
+ Learn how to use the [Thonny](https://thonny.org/) IDE.
+ Learn about the [Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/).

### Resources
+ Articles
  + [MicroPython on the Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
  + [Quick reference for the RP2](https://docs.micropython.org/en/latest/rp2/quickref.html)
  + Wikipedia
    + [Raspberry Pi Pico](https://en.wikipedia.org/wiki/Raspberry_Pi#Raspberry_Pi_Pico)
    + [RP2040](https://en.wikipedia.org/wiki/RP2040)
    + [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
    + [Thonny IDE](https://en.wikipedia.org/wiki/Thonny)
+ Books
  + Get Started with MicroPython on Raspberry Pi Pico 138 pages [PDF](https://hackspace.raspberrypi.com/books/micropython-pico)
  + Raspberry Pi Pico Python SDK 46 pages [PDF](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
  + Python in easy steps 2nd Edition 192 pages [Amazon](https://www.amazon.com/Python-easy-steps-2nd-Covers-ebook/dp/B07FPPVWRX?ref_=ast_sto_dp)
+ Videos
  + YouTube: Raspberry Pi Pico [list](https://www.youtube.com/results?search_query=raspberry+pi+pico)
+ Courses
  + The Great Courses: How to Program: Computer Science Concepts and Python Exercises [video](https://www.thegreatcourses.com/courses/how-to-program-computer-science-concepts-and-python-exercises) 
+ Code
  + GitHub: [raspberrypi/pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio)


## Project4 : Setup Pico with Micropython

<p align="center">
  <img width="640" height="480" src="/Images/dataLogVTemp2.jpg">  
</p>

### Goal
+ Setup the Pico to run micopython with the Raspberry Pi P400 computer.
+ Configure the Pico for micropython.
+ Use Thonny to create, edit and debug micropython programs to run on the Pico.

## Project : Run Pico on Batteries

<p align="center">
  <img width="640" height="480" src="/Images/voltsTemp.jpg">  
</p>

### Goal
+ Design a circuit so that the Pico automatically runs on the USB micro connector or a battery input.
+ The Pico automatically switch to the highest voltage.
+ Protect both sources from loading down the other souce.

## Project : Run Pico on Solar Cells

<p align="center">
  <img width="640" height="480" src="/Images/solar1.jpg"> 
  <img width="640" height="480" src="/Images/solar2.jpg">  

</p>

### Goal
+ Use a low cost solar cells that are design for remove cameras that provide 5V.
+ Find a solar cell with a micro USB connector that will plug directly into the Pico.
+ Test the solar cell/battery power configuration.
+ Find a water proof box for the Pico and battery.

## Project : Use Pico A/Ds to Measure Vbus, Vsys and Vbattery

<p align="center">
  <img width="640" height="480" src="/Images/adVoltsDivider.jpg">  
</p>

### Goal
+ Use the three A/D converters to measure Vbus, Vsys and Vbattery voltage.
+ Design a 50% voltage divider to prevent damage to the A/D inputs that have a maximum of 3.3V.
+ Test how low Vbattery can go before the Pico stops operating.

## Project : Use Pico A/D to Measure CPU Temperature

<p align="center">
  <img width="640" height="480" src="/Images/dataLogVTemp.jpg">  
</p>

### Goal
+ Use the forth A/D converter to measure CPU temperature.
+ Measure the Vbus, Vsys and Vbattery voltage.
+ Use the internal real-time clock to time mark the data readings.
+ Save time, Vbus, Vsys, Vbattery and temperature to data log on the Pico flash memory.

Data log saved to Pico flash memory.
Below is the first few lines of the data file that was stored on the Pico flash memory.

<pre>
Day Time    VBUS  VSYS  VBat  Temp 2022/11/28
28 17:28:11 5.29V 5.16V 1.87V 72.25F
28 17:28:21 5.30V 5.16V 3.55V 72.25F
28 17:28:31 1.04V 3.05V 3.41V 72.25F
28 17:28:41 1.03V 3.06V 3.44V 70.56F
28 17:28:51 1.03V 3.06V 3.44V 70.56F
28 17:29:1  1.02V 3.05V 3.44V 71.41F
28 17:29:11 1.02V 3.06V 3.42V 72.25F
28 17:29:21 1.02V 3.06V 3.42V 72.25F
28 17:29:31 1.02V 3.05V 3.42V 70.56F
28 17:29:41 1.02V 3.07V 3.42V 70.56F
28 17:29:51 1.01V 3.05V 3.42V 70.56F
28 17:30:1  1.00V 3.06V 3.44V 70.56F
28 17:30:11 0.99V 3.07V 3.41V 69.72F
28 17:30:21 0.98V 3.05V 3.41V 69.72F
28 17:30:31 0.98V 3.06V 3.41V 68.88F
28 17:30:41 0.98V 3.04V 3.41V 69.72F
28 17:30:51 0.97V 3.04V 3.41V 68.88F
28 17:31:1  0.96V 3.06V 3.41V 68.88F
28 17:31:11 0.96V 3.04V 3.41V 68.04F
28 17:31:21 0.95V 3.05V 3.41V 68.04F
</pre>

# Future Project Ideas

+ A/D test, speed, accuracy, 2 point cal, etc.
+ Battery operation tests.
+ Low power modes, sleep, deep sleep.
+ Two core programming.
+ File functions and largest file size.
+ Use circuitpython.
+ Implement a RTC with I2C bus.
+ Use the different python libraries.
+ Use the Arduino IDE and libraries.

73 David Haworth WA9ONY
