<A NAME="HOME"></A>
<HR>
<P align="center"><A HREF="README101.md#FUTURE">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="https://groups.io/g/Microcontrollers">Groups.IO</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#INDEX">--&gt;</A></P>  

# RP2040 & Arduino Microcontroller Projects Notes

<p align="center">
<img width="308" height="308" src="/Images/RP2040.png">  
</p>

<p align="center">
The Raspberry Pi RP2040 microcontroller IC is a small computer, 0.267 square inches chip,<BR>with 56 pins of which most of the pins are used to interface to other electronic devices.
</p>
 
<p align="center">
<A HREF="http://www.stargazing.net/david/index.html">David Haworth</A>, <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A>
</p> 

## Introduction  
  
This repo focuses on microcontroller-based projects. It documents WA9ONY microcontroller learning experinces, resources used and projects.  This includes the new (2021) RP2040 microcontroller ecosystem that has shook the microcontroller industry with it's high performace, low cost ($1), small size (0.267 square inches) and availablity to other companies so that they can products that include the RP2040 products (Arduino NANO RP2040 Connect).  Microcontrollers would not be complete without understanding how to use the defacto microcontroller standard since 2005, the Arduino microcontroller ecosystem.

The ham radio projects range from a microcontroller board showing its temperature by using its on board LED to indicate the board's temperature in Morse code to a transceivers built with a microcontroller with other hardware.  In the below project 1: ham radio microcontroller books browse through the book contente in the table to see the various ham radio microcontroller projects (&gt;150) that have been written about.  Also, YouTube and the Internet is filled with ham radio microcontroller projects.
  
Microcontroller projects range from using only the microcontroller developement board to attaching various components and various subsystem boards with  standardized serial interfaces (SPI, I2C, STEMMA QT, etc.).
  
Software is needed to program the microcontroller.  The long time defacto standard is Arduino IDE (since 2005) which is based on C++. Also, MicroPython and CircuitPython have large strong microcontroller ecosystems.  This results in different ways to program the microcontroller.   

<img align="right" width="320" height="240" src="/Images/voltsTemp320.png">

## Summary of What is Needed for Microcontroller Project.
- Microcontroller developement board.
- Additional electronics and subsystem boards needed for the project.
- Computer
  - To develope software with the IDE.
  - To upload the software to the microcontroller board usually with USB interface.
  - To power the microcontroller board with the USB interface. 
- Software IDE to develope the microcontroller software.
- Power the project after software is completed and the computer is not needed.
  - USB power souce
  - Batteries
  - Solar cells


<A NAME="INDEX"></A>
<HR>
<P align="center"><A HREF="#HOME">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - Index - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P1">--&gt;</A></P>  
 
# Microcontroller Projects Notes Index
+ <A HREF="#HOME">Home</A> 
+ Project 1: <A HREF="#P1">Ham Radio Micorocontroller Books</A>
+ Project 2: <A HREF="#P2">Micorocontrollers Books</A>
+ Project 3: <A HREF="#P3">Micorocontrollers in Magazines</A>
+ Project 4: <A HREF="#P4">Micorocontrollers Videos</A>
+ Project 5: <A HREF="#P5">Forums</A>
+ Project 6: <A HREF="#P6">Micorocontrollers Applications</A>
+ Project 7: <A HREF="#P7"><A HREF="#P7">RP2040 Microcontroller Introduction</A>
+ Project 8: <A HREF="#P8">Arduino Microcontroller Introduction</A>
+ Project 9: <A HREF="#P9">RP2040 Development Boards Lists</A>
+ Project 10: <A HREF="#P10">Raspberry Pi RP2040 Boards</A>
+ Project 11: <A HREF="#P11">Adafruit Industries RP2040 Boards</A>
+ Project 12: <A HREF="#P12">Arduino Nano RP2040 Connect Board</A>
+ Project 13: <A HREF="#P13">Seeed Studio RP2040 Boards</A>
+ Project 14: <A HREF="#P14">SparkFun RP2040 Boards</A>
+ Project 15: <A HREF="#P15">Waveshare RP2040 Boards</A>
+ Project 16: <A HREF="#P16">Micorocontrollers Programming</A>
+ Project 17: <A HREF="#P17">Arduino IDEs on Linux Computer</A>
+ Project 18: <A HREF="#P18">Build a Computer for Microcontroller Development</A>
+ Project 19: <A HREF="#P19">Setup GitHub</A>
+ Project 20: <A HREF="#P20">Learn Micropython on the Pico</A>
+ Project 21: <A HREF="#P21">Setup Pico with Micropython</A>
+ Project 22: <A HREF="#P22">Run Pico on Batteries</A>
+ Project 23: <A HREF="#P23">Power the  Pico on Solar Cells</A>
+ Project 24: <A HREF="#P24">Use Pico A/Ds to Measure Vbus, Vsys and Vbattery Voltage
+ Project 25: <A HREF="#P25">Use Pico A/D to Measure CPU Temperature</A>
+ Project 26: <A HREF="#P26">Run the Arduino IDE & Arduno Uno R3</A>
+ Project 27: <A HREF="#P27">Using the GiHub Web Interface</A>
+ Project 28: <A HREF="#P28">Arduino Cloud</A>
+ Project 29: <A HREF="#P29">Arduino Microcontroller Boards</A>
+ Project 30: <A HREF="#P30">Arduino Clone Microcontroller Boards</A> 
+ Project 31: <A HREF="README2.md#P31">Arduino OPLA IoT Kit</A>
+ Project 32: <A HREF="README2.md#P32">Arduino IoTerrific Bundle</A>
+ Project 33: <A HREF="README2.md#P33">Electronic Component Kits</A>
+ Project 34: <A HREF="README2.md#P34">Steps in Building a Microcontroller Project</A>
+ Project 35: <A HREF="README2.md#P35">Electronic Breadboards</A>
+ Project 36: <A HREF="README2.md#P36">PCBs</A>
+ Project 37: <A HREF="README2.md#P37">Soldering</A>
+ Project 38: <A HREF="README2.md#P38">Resistor Power Rating</A>
+ Project 39: <A HREF="README2.md#P39">Resistor Tolerance</A>
+ Project 40: <A HREF="README2.md#P40">Measuring Resistors</A> 
+ Project 41: <A HREF="README2.md#P41">Resistor Composition</A> 
+ Project 42: <A HREF="README2.md#P42">USB</A> 
+ Project 43: <A HREF="README2.md#P43">Arduino Registration and Cloud Plan</A> 
+ Project 44: <A HREF="README2.md#P44">Arduino Simple OPLA Read & Display Sensor Data Sketch</A> 
+ Project 45: <A HREF="README2.md#P45">DIY Soldering Iron Holder</A> 
+ Project 46: <A HREF="README2.md#P46">Arduino MEGA 2560 Microcontroller Board</A>
+ Project 47: <A HREF="README2.md#P47">AC Power Suppies for Microcontroller Boards</A>
+ Project 48: <A HREF="README2.md#P48">Arduino IDEs on Windows 10 Computer</A>
+ Project 49: <A HREF="README2.md#P49">Arduino IDE V1.8 on Raspberry Pi Computer</A>
+ Project 50: <A HREF="README2.md#P50">WA7ABU Repeater Project Net</A>
+ Project 51: <A HREF="README2.md#P51">Learn C++ with Arduino Web Editor & Board</A>
+ Project 52: <A HREF="README2.md#P52">Microcontroller Development Boards Price Table</A>
+ Project 53: <A HREF="README2.md#P53">Starting with Microcontroller</A>
+ Project 54: <A HREF="README2.md#P54">Arduino MEGA 2560 Rev3 Case</A>
+ Project 55: <A HREF="README2.md#P55">Arduino IoT Cloud</A>
+ Project 56: <A HREF="README2.md#P56">Arduino OPLA RGB LED Test</A>
+ Project 57: <A HREF="README2.md#P57">Arduino OPLA Personal Weather Station IoT Cloud</A>
+ Project 58: <A HREF="README2.md#P58">Arduino IoT Cloud Over-the-Air</A>
+ Project 59: <A HREF="README2.md#P59">Arduino IoT Cloud iOS Mobile Dashboard Pane</A>
+ Project 60: <A HREF="README2.md#P60">Fritzing</A>
+ Project 61: <A HREF="README2.md#P61">Tinkercad Arduino Simulator</A>
+ Project 62: <A HREF="README2.md#P62">LED: Light-emitting Diode</A>
+ Project 63: <A HREF="README2.md#P63">I²C-bus: Inter-Integrated Circuit Bus</A>
+ Project 64: <A HREF="README2.md#P64">SPI: Serial Peripheral Interface</A>
+ Project 65: <A HREF="README2.md#P65">OLED: Organic Light-Emitting Diode</A>
+ Project 66: <A HREF="README2.md#P66">I²C-bus: Sparkfun Qwiic</A>
+ Project 67: <A HREF="README2.md#P67">SparkFun 16x2 SerLCD - RGB Text (QWIIC)</A>
+ Project 68: <A HREF="README2.md#P68">Raspberry Pi Pico I²C Scan</A>
+ Project 69: <A HREF="README2.md#P69">Raspberry Pi Pic to SparkFun 16x2 SerLCD Qwiic "hello"</A>
+ Project 70: <A HREF="README2.md#P70">Raspberry Pi Pic to SparkFun 16x2 SerLCD Qwiic "temp"</A>
+ Project 71: <A HREF="README2.md#P71">Raspberry Pi Pic to SparkFun 16x2 SerLCD 96 Char Test</A>
+ Project 72: <A HREF="README2.md#P72">Raspberry Pi Pic I²C MicroPython</A>
+ Project 73: <A HREF="README2.md#P73">I²C-bus: Adafruit STEMMA & STEMMA QT</A>
+ Project 74: <A HREF="README2.md#P74">I²C Waveforms</A>
+ Project 75: <A HREF="README2.md#P75">Tennsy 4.1 Microcontroller Board</A>
+ Project 76: <A HREF="README2.md#P76">I²C-bus: 7-bit Address Table</A>
+ Project 77: <A HREF="README2.md#P77">Microcontroller Boards Table</A>
+ Project 78: <A HREF="README2.md#P78">KiCad Circuit Simulation</A>
+ Project 79: <A HREF="README2.md#P79">Adafruit 2FA: Two-Factor Authentication</A>
+ Project 80: <A HREF="README2.md#P80">Qucs: Quite Universal Circuit Simulator</A>
+ Project 81: <A HREF="README2.md#P81">I²C-bus: Seeed Studio Grove System</A>
+ Project 82: <A HREF="README2.md#P82">MicroPython Pico Function</A>
+ Project 83: <A HREF="README2.md#P83">Book: Programming the Pico, Dr.Simon Monk</A>
+ Project 84: <A HREF="README2.md#P84">I²C-bus: SparkFun Qwiic MultiPort</A>
+ Project 85: <A HREF="README2.md#P85">Tinkercad Circuits</A>
+ Project 86: <A HREF="README2.md#P86">Tinkercad Codeblocks</A>
+ Project 87: <A HREF="README2.md#P87">Tinkercad 3D Design</A>
+ Project 88: <A HREF="README2.md#P88">Diode I-V Characteristics Curve</A>
+ Project 89: <A HREF="README2.md#P89">I-V Characteristics Curve Tester in Tinkercad</A>
+ Project 90: <A HREF="README2.md#P90">I-V Characteristics Curve Tester in Qucs</A>
+ Project 91: <A HREF="README2.md#P91">I-V Characteristics Curve Tester Theory of Operation</A>
+ Project 92: <A HREF="README2.md#P92">Color LEDs I-V Characteristics Curve</A>
+ Project 93: <A HREF="README2.md#P93">Red LED Turn On  I-V Characteristics Curve</A>
+ Project 94: <A HREF="README2.md#P94">Zener Diode I-V Characteristics Curve</A> 
+ Project 95: <A HREF="README2.md#P95">Two Series Zener Diodes I-V Characteristics Curve</A>
+ Project 96: <A HREF="README2.md#P96">Series Circuit (2 Zener Diodes & 100 Ohms Resistor) I-V Characteristics Curve</A>
+ Project 97: <A HREF="README2.md#P97">Resistors I-V Characteristics Curve</A>
+ Project 98: <A HREF="README2.md#P98">Capacitor I-V Characteristics Curve</A>
+ Project 99: <A HREF="README2.md#P99">Transformer I-V Characteristics Curve</A>
+ Project 100: <A HREF="README2.md#P100">2N3055 NPN Transistor BE I-V Characteristics Curve</A>
+ Project 101: <A HREF="README101.md#P101">YouTube Channel Gems</A>
+ Project 102: <A HREF="README101.md#P102">List of YouTube Playlists</A>
+ Project 103: <A HREF="README101.md#P103">2N3055 Testing with the Peak Atlas DCA75 Pro</A>
+ Project 104: <A HREF="README101.md#P104">I-V Characteristics Curve Tester Version 2</A>
+ Project 105: <A HREF="README101.md#P105">2N3055 Ic-Vc, Ib I-V Characteristics Curve Tester Version 2</A>
+ Project 106: <A HREF="README101.md#P106">2N3055 Ic-Vc, Ib LED Test</A>
+ Project 107: <A HREF="README101.md#P107">Elektor TV Webinars</A>
+ Project 108: <A HREF="README101.md#P108">Arduino IDE MicroPython</A>
+ Project 109: <A HREF="README101.md#P109">Embedded World Exhibition & Conference</A>
+ Project 110: <A HREF="README101.md#P110">Elektor Digital Green Magazine</A>
+ Project 111: <A HREF="README101.md#P111">Search PDFs for Text</A>
+ Project 112: <A HREF="README101.md#P112">Newsletters</A>
+ Project 113: <A HREF="README101.md#P113">Internet Archive</A>
+ Project 114: <A HREF="README101.md#P114">Digi-Key Electronics</A>
+ Project 115: <A HREF="README101.md#P115">tinyML Foundation</A>
+ Project 116: <A HREF="README101.md#P116">AI: Artificial Intelligence/A>
+ Project 117: <A HREF="README101.md#P117">ML (Machine Learning) & tinyML</A>
+ Project 118: <A HREF="README101.md#P118">Khan Academy</A>
+ Project 119: <A HREF="README101.md#P119">OCW: MIT Open Course Ware</A>
+ Project 120: <A HREF="README101.md#P120">TensorFlow</A>
+ Project 121: <A HREF="README101.md#P121">Microcontrollers Machine Learning</A>
+ Project 122: <A HREF="README101.md#P122">SBC (Single Board Computer) Machine Learning</A>
+ <A HREF="README2.md#Future">Future Project Ideas</A>

<A NAME="P1"></A>
<HR>
<P align="center"><A HREF="#INDEX">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P2">--&gt;</A></P>  
 
# Project 1: Ham Radio Micorocontroller Books

<p align="center">
  <img width="567" height="740" src="/Images/Books5.png">  
</p>

The below table identifies books on microcontrollers in ham radio.  
  
Look at the contents column to see the various ham radio microcontroller projects that have been written about in these books. The books are sorted with the newest books at the top of the table.

Summary of the eight books:
+ 130 chapters
+ 2,937 pages
+ 135 projects
  + Here is one project taken from each book.
     + FM radio
     + Simple DDS based CW TX
     + DSP post processor
     + 40 meter QRP JT65 transceiver
     + DDS VFO
     + Talking SWR meter
     + APRS data logger
     + RTTY reader

Review
+ [Arduino Projects for Amateur Radio](https://www.n4nrv.org/microcontroller-projects-for-amateur-radio/)

<p align="center"><B>
Ham radio microcontroller books table 1.1.
</B></p>

<TABLE>
  <TR>
    <TD><P><B>
      Book Title
      </B></P></TD>
    <TD><P><B>
      Author
    </B></P></TD>
    <TD><P><B>
      Publisher
    </B></P></TD>
    <TD><P><B>
      Date
    </B></P></TD>
    <TD><P><B>
      Contents
    </B></P></TD>
    <TD><P><B>
    Projects
    </B></P></TD>
    <TD><P><B>
      Pages
    </B></P></TD>
    <TD><P><B>
      uC
    </B></P></TD>
    <TD><P><B>
      Software
    </B></P></TD>
    <TD><P><B>
      Price
    </B></P></TD>
  </TR>
    
  <TR>
    <TD> 
      <A HREF="https://www.elektor.com/raspberry-pi-pico-for-radio-amateurs-e-book">Raspberry Pi Pico for Radio Amateurs</A>
    </TD>
    <TD>
      G7SCU
    </TD>
    <TD>
      <A HREF="https://www.elektor.com/books">Elektor</A>
    </TD>    
     <TD>
      2021
    </TD>
     <TD>
      <A HREF="./BookContents/RaspberryPiPicoforRadioAmateurs.pdf">PDF</A>
    </TD>
    <TD>    
    43
    </TD>    
    <TD>
      310 Color PDF
    </TD>
     <TD>
      <A HREF="https://en.wikipedia.org/wiki/RP2040">RP2040</A>
     </TD>
     <TD>
       <A HREF="https://www.elektor.com/raspberry-pi-pico-for-radio-amateurs-e-book">Files</A>
    </TD>
      <TD>
        <P>€29.95<BR> PDF</P>
    </TD>
  </TR>
  
   <TR>
   <TD>
     <P>
     <A HREF="https://rsgb.org/main/blog/publications/books-extra/2021/04/24/microcontroller-know-how/">Microcontroller Know How Amateur Radio<BR> projects and much more</A>
     </P>  
    </TD>
    <TD>
      G0MGX
    </TD>
     <TD>
      <A HREF="https://www.rsgbshop.org/acatalog/Online_Catalogue_Radio_Books___CDs_29.html">RSGB</A>
    </TD>     
     <TD>
      2021
    </TD>
    <TD>
      <A HREF="./BookContents/MicrocontrollerKnowHowAmateurRadioprojects.png">PNG</A>
    </TD>
    <TD>    
    9
    </TD>    
    <TD>
      175 Color Kindle
    </TD>
    <TD>
      <P><A HREF="https://en.wikipedia.org/wiki/Arduino">Arduino</A><BR>
        <A HREF="https://stm32-base.org/boards/STM32F103C8T6-Blue-Pill.html">Blue Pill</A></P>  
    </TD>
    <TD>
      <A HREF="https://drive.google.com/drive/folders/1Q0chpbWhwx7m6oytslTZod9CoWsARgBl">Files</A>
    </TD>  
    <TD>
      $21.99 <A HREF="https://www.amazon.com/kindle-dbs/storefront?storeType=browse&node=154606011">Kindle</A>
    </TD>
  </TR>

   <TR>
   <TD>
      <A HREF="https://home.arrl.org/action/Store/Product-Details/productId/133985">More Arduino for Ham Radio</A>
    </TD>
    <TD>
      <A HREF="https://www.qrz.com/db/KW5GP">KW5GP</A>
    </TD>
    <TD>
      <A HREF="https://home.arrl.org/action/Shop/Products#filter=%7B%22Facet%22%3A%7B%22Name%22%3A%22Publications%22,%22Value%22%3A%22WEB_FACET_1%22%7D,%22SubFacet%22%3A%7B%22Name%22%3A%22Books%22,%22Value%22%3A%22BOOKS%22%7D,%22Category%22%3Anull,%22SubCategory%22%3Anull%7D&searchTerm=&searchItemNameTerm=&searchDescriptionTerm=&productClass=">ARRL</A>
    </TD>
    <TD>
      2021
    </TD>
    <TD>
      <A HREF="./BookContents/MoreArduinoFHR.png">PNG</A>
    </TD>
    <TD>    
     10
    </TD>    
    <TD>
     384
    </TD>
    <TD>
     <P><A HREF="https://en.wikipedia.org/wiki/Arduino">Arduino</A></P>  
    </TD>    
    <TD>
      <A HREF="http://www.kw5gp.com/Arduino3/">Files</A>
    </TD>
    <TD>
      $39.95
    </TD>
  </TR>    
     
   <TR>
   <TD>
     <A HREF="https://home.arrl.org/action/Store/Product-Details/productId/132600">Microcontroller Projects for Amateur Radio</A>
    </TD>
    <TD>
      <A HREF="https://www.qrz.com/db/W8TEE">W8TEE</A> & <A HREF="https://www.qrz.com/db/AC8GY">AC8GY</A>
    </TD>
    <TD>
      <A HREF="https://home.arrl.org/action/Shop/Products#filter=%7B%22Facet%22%3A%7B%22Name%22%3A%22Publications%22,%22Value%22%3A%22WEB_FACET_1%22%7D,%22SubFacet%22%3A%7B%22Name%22%3A%22Books%22,%22Value%22%3A%22BOOKS%22%7D,%22Category%22%3Anull,%22SubCategory%22%3Anull%7D&searchTerm=&searchItemNameTerm=&searchDescriptionTerm=&productClass=">ARRL</A>
    </TD>  
    <TD>
      2020
    </TD>
    <TD>
      <A HREF="./BookContents/MicrocontrollerProjectsforAmateurRadio.png">PNG</A>
    </TD>
    <TD>    
    7
    </TD>    
    <TD>
      400 B&W
    </TD>
    <TD>
    <P><A HREF="https://en.wikipedia.org/wiki/Arduino">Arduino</A></P>
    </TD>
    <TD>
      <P><A HREF="https://groups.io/g/SoftwareControlledHamRadio">Files ?</A></P>
    </TD>  
    <TD>
      $39.95
    </TD>
  </TR>

  <TD>
      <A HREF="https://www.arrl.org/arduino2">More Arduino Projects for Ham Radio</A>
    </TD>
    <TD>
      <A HREF="https://www.qrz.com/db/KW5GP">KW5GP</A>
    </TD>
     <TD>
      <A HREF="https://home.arrl.org/action/Shop/Products#filter=%7B%22Facet%22%3A%7B%22Name%22%3A%22Publications%22,%22Value%22%3A%22WEB_FACET_1%22%7D,%22SubFacet%22%3A%7B%22Name%22%3A%22Books%22,%22Value%22%3A%22BOOKS%22%7D,%22Category%22%3Anull,%22SubCategory%22%3Anull%7D&searchTerm=&searchItemNameTerm=&searchDescriptionTerm=&productClass=">ARRL</A>
     </TD>  
     <TD>
      2017
    </TD>
    <TD>
      <A HREF="./BookContents/MoreArduinoProjectsforHamRadio.png">PNG</A>
    </TD>
    <TD>    
    14
    </TD>    
    <TD>
      500 B&W
    </TD>
    <TD>
      <P><A HREF="https://en.wikipedia.org/wiki/Arduino">Arduino</A></P>  
    </TD>    
   <TD>
     <A HREF="http://www.kw5gp.com/Arduino2/">Files</A>
    </TD>
    <TD>
      $34.95
    </TD>
  </TR>
  
  <TR>
    <TD> 
      <A HREF="https://www.academia.edu/41503314/Arduino_Projects_for_Amateur_Radio">Arduino Projects for Amateur Radio</A>
    </TD>
    <TD>
      <A HREF="https://www.qrz.com/db/W8TEE">W8TEE</A>,  <A HREF="https://www.qrz.com/db/W6DQ">W6DQ</A>, et al.
    </TD>
     <TD>
     <A HREF="https://www.oreilly.com/library/view/arduino-projects-for/9780071834063/">O'Reilly</A>,
     <A HREF="https://www.accessengineeringlibrary.com/content/book/9780071834056">Mc Graw Hill</A>
    </TD>
     <TD>
      2014
    </TD>
    <TD>
      <A HREF="./BookContents/ArduinoProjectsforAmateurRadio.pdf">PDF</A>
    </TD>
    <TD>    
    14
    </TD>    
    <TD>
      464 B&W
    </TD>
    <TD>
      <P><A HREF="https://en.wikipedia.org/wiki/Arduino">Arduino</A></P>  
    </TD>    
    <TD>
       <P><A HREF="https://groups.io/g/SoftwareControlledHamRadio/files/Arduino%20Projects%20for%20Amateur%20Radio%20Source%20files">Files</A></P>
    </TD>
    <TD>
      $25.45
    </TD>
  </TR>
  
  <TR>
    <TD>
      <A HREF="https://www.arrl.org/arduino">Arduino for Ham Radio</A>
    </TD>
    <TD>
      <A HREF="https://www.qrz.com/db/KW5GP">KW5GP</A>
    </TD>
     <TD>
      <A HREF="https://home.arrl.org/action/Shop/Products#filter=%7B%22Facet%22%3A%7B%22Name%22%3A%22Publications%22,%22Value%22%3A%22WEB_FACET_1%22%7D,%22SubFacet%22%3A%7B%22Name%22%3A%22Books%22,%22Value%22%3A%22BOOKS%22%7D,%22Category%22%3Anull,%22SubCategory%22%3Anull%7D&searchTerm=&searchItemNameTerm=&searchDescriptionTerm=&productClass=">ARRL</A>
     </TD>  
     <TD>
      2014
    </TD>
    <TD>
      <A HREF="./BookContents/ArduinoforHamRadio.png">PNG</A>
    </TD>
    <TD>    
    19
    </TD>    
    <TD>
      352 B&W
    </TD>
    <TD>
      <P><A HREF="https://en.wikipedia.org/wiki/Arduino">Arduino</A></P>  
    </TD>    
    <TD>
       <A HREF="http://www.kw5gp.com/Arduino/">Files</A>
    </TD>
    <TD>
      Out of Print $76.06
    </TD>
  </TR>
  
  <TR>
   <TD>
      <A HREF="https://home.arrl.org/action/Store/Product-Details/productId/114304">Ham Radio for Arduino and Picaxe</A>
    </TD>
    <TD>
      <A HREF="https://www.qrz.com/db/WA5ZNU">WA5ZNU</A>
    </TD>
     <TD>
      <A HREF="https://home.arrl.org/action/Shop/Products#filter=%7B%22Facet%22%3A%7B%22Name%22%3A%22Publications%22,%22Value%22%3A%22WEB_FACET_1%22%7D,%22SubFacet%22%3A%7B%22Name%22%3A%22Books%22,%22Value%22%3A%22BOOKS%22%7D,%22Category%22%3Anull,%22SubCategory%22%3Anull%7D&searchTerm=&searchItemNameTerm=&searchDescriptionTerm=&productClass=">ARRL</A>
     </TD>  
     <TD>
      2013
    </TD>
    <TD>
      <A HREF="./BookContents/HamRadioforArduinoandPicaxe.png">PNG</A>
    </TD>
    <TD>    
     19
    </TD>    
    <TD>
      352 B&W
    </TD>
    <TD>
      <P><A HREF="https://en.wikipedia.org/wiki/Arduino">Arduino</A></P>  
    </TD>     
    <TD>
       <A HREF="http://hamradioprojects.com/projects/">Files</A>
    </TD>
    <TD>
      $34.95
    </TD>
  </TR>
</TABLE>
    
    
<A NAME="P2"></A>
<HR>
<P align="center"><A HREF="#P1">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P3">--&gt;</A></P>  

# Project 2:  Micorocontrollers Books

<p align="center">
  <img  width="269" height="134" src="/Images/ArduinoPico.png"> 
</p>
    
## HackSpace Free Books [PDFs](https://hackspace.raspberrypi.com/books)   
+ Get Started with MicroPython on Raspberry Pi Pico, 139 pages [PDF](https://hackspace.raspberrypi.com/books/micropython-pico) 
  + The best Pico book to start with.
  + Also found in MagPi [books](https://magpi.raspberrypi.com/books)
  + Raspberry Pi Pico MicroPython {play list](https://www.youtube.com/watch?v=IgUupJIRKrk&list=PLKAB78-HH7CZDVrBwvS81cbCVF6rQuwA3)
+ Get Started With Arduino, 180 pages [PDF](https://hackspace.raspberrypi.com/articles/get-started-with-arduino-book)   

## Raspberry Pi
+ Raspberry Pi Pico Python SDK, 48 pages [PDF](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
+ Getting started with Raspberry Pi Pico, 80 pages [PDF](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)   
+ Raspberry Pi Pico C/C++ SDK, 171 pages [PDF](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf)   
+ Connecting to the Internet with Raspberry Pi Pico W, 30 pages [PDF](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf)
   
##  Elektor [Books](https://www.elektor.com/books)   

## Make [Books](https://www.makershed.com/collections/make-books-print)

## Best Arduino Books
+ Google: [best arduino books](https://www.google.com/search?q=best+arduino+books&sxsrf=AJOqlzXcME85zWR1o0DOzV2u7ydBnHq21A%3A1673719775242&ei=3-_CY7i-DpDJ0PEPwIGVoAE&oq=best+arduino+book&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgUIABCRAjIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIICAAQFhAeEA8yBggAEBYQHjIFCAAQhgM6CggAEEcQ1gQQsAM6BwgAELADEEM6DQgAEOQCENYEELADGAE6DwguEOUEEMgDELADEEMYAjoECCMQJzoECAAQQzoKCAAQgAQQhwIQFEoECEEYAEoECEYYAVDVJVjuNWCzV2gFcAB4AIABXIgBnwOSAQE1mAEAoAEByAEQwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz-serp) 
 
## Amazon Books
+ Pico book [list](https://www.amazon.com/s?k=raspberry+pi+pico+book&crid=3TYSWPL6AAMTA&sprefix=raspberry+pi+pico+book%2Caps%2C146&ref=nb_sb_noss_1)
+ Python book [list](https://www.amazon.com/s?k=Python+in+books&crid=30BE822W2L736&sprefix=python+in+books%2Caps%2C169&ref=nb_sb_noss_1)
+ Arduino book [list](https://www.amazon.com/s?k=arduino+in+books&crid=1KKMCHXX3CGXS&sprefix=Arduino+in+books%2Caps%2C165&ref=nb_sb_ss_ts-doa-p_1_16)
+ C++ book [list](https://www.amazon.com/s?k=c%2B%2B+in+books&crid=30I4G3VL5WZP6&sprefix=c%2B%2B+in+books%2Caps%2C168&ref=nb_sb_ss_ts-doa-p_1_12)

## Internet Archive
Sign up for a account and you can borrow books.
+ Raspberry Pi Pico [list](https://archive.org/search.php?query=Raspberry%20Pi%20Pico)
+ Arduino [list](https://archive.org/search.php?query=Arduino)
+ Microcontroller [list](https://archive.org/search.php?query=microcontroller&page=1)
+ Python [list](https://archive.org/search.php?query=Python)

  
<A NAME="P3"></A>
<HR>
<P align="center"><A HREF="#P2">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P4">--&gt;</A></P>  

# Project 3: Micorocontrollers in Magazines

<p align="center">
<img  width="747" height="286" src="/Images/Mags2.png">
</p>
    
## Raspberry Pi Press Free Magazines 
+ [Hackspace](https://hackspace.raspberrypi.com/) issue [39, 40, 44](https://hackspace.raspberrypi.com/issues?page=2), [52, 57, 61](https://hackspace.raspberrypi.com/issues?page=1)
+ [MagPi](https://magpi.raspberrypi.com/) issue [109](https://magpi.raspberrypi.com/issues?page=2), [119, 121](https://magpi.raspberrypi.com/issues)

## [Elektor](https://elektor.com/) magazine 
 + 2022 Dec issue, Arduino ([free 40 pages](https://www.elektormagazine.com/declassified-arduino-bonus-edition?utm_source=Elektor+International+%28English%29&utm_campaign=8eed08f225-EMAIL_CAMPAIGN_1_5_2023_10_5&utm_medium=email&utm_term=0_23bd160f48-8eed08f225-%5BLIST_EMAIL_ID%5D&mc_cid=8eed08f225&mc_eid=1bc428feb9) of the 140 page issue)
 + Back issues are available with a Green membership (no print, only PDFs) 

<img align="right" width="94" height="133" src="/Images/Make83s.png">

## [Make](https://makezine.com/) magazine
+ Volumn 83 contains the 2022 annual Boards Guide (79 boards) on microcontrollers and SBCs. 
+ Back issues are available with a digital subscription.
+ Make maganizes are [online](https://archive.org/details/Makezine)
  + Register and have access to borrow the issue you want.
  
<A NAME="P4"></A>
<HR>
<P align="center"><A HREF="#P3">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P5">--&gt;</A></P>  
  
# Project 4: Micorocontrollers Videos

<p align="center">
<img  width="256" height="57" src="/Images/YouTube_LogoS.png">
</p>
  
Videos on microcontrollers.
    
+ Exploring the Next Generation of Arduino Microcontrollers (Pico) [video](https://www.youtube.com/watch?v=HOi_AYEgSmo) - Glen Popiel, KW5GP
+ YouTube
  + Raspberry Pi Pico [list](https://www.youtube.com/results?search_query=raspberry+pi+pico)
  + ExplainingComputers Pico [list](https://www.youtube.com/@ExplainingComputers/search?query=Pico)
  + Hamshield: Arduino meets amateur radio [video](https://youtu.be/xLTSlcZK14I)

## [Elektor TV](https://www.youtube.com/@ElektorTV)
+ Elektor Lab [Talk Arduino](https://youtu.be/rfPZvhgw_CQ) January 26, 8:00 PST
 
## Arduino [Channel](https://www.youtube.com/channel/UCUpmmT1Gm_raVpqSvQYyd2Q)

## Raspberry Pi [Channel](https://www.youtube.com/raspberrypi)

## Make Magazine [Channel](https://www.youtube.com/user/makemagazine/videos)

## Adafruit Industries [Channel](https://www.youtube.com/channel/UCpOlOeQjj7EsVnDh3zuCgsA)


<A NAME="P5"></A>
<HR>
<P align="center"><A HREF="#P4">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P6">--&gt;</A></P>  

# Project 5: Forums

<p align="center">
<img  width="115" height="93" src="/Images/groupsio.png">
</p>

Forums related to microcontrollers.
    
## Groups.IO
+ SoftwareControlledHamRadio [group](https://groups.io/g/SoftwareControlledHamRadio)
  + This is the support group for the book Microcontroller Projects for Amateur Radio.
  + The [files](https://groups.io/g/SoftwareControlledHamRadio/files/Arduino%20Projects%20for%20Amateur%20Radio%20Source%20files) for book Arduino Projects for Amateur Radio are in the group files section.

  
<A NAME="P6"></A>
<HR>
<P align="center"><A HREF="#P5">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P7">--&gt;</A></P>  

# Project 6: Micorocontrollers Applications
    
<p align="center">
  <img width="522" height="441" src="/Images/AD9833s50b.png">  
</p>

<p align="center">
Two AD9833 Function Generators Boards & Raspberry Pi Pico Microcontroller Board.
</p>

## Microcontrollers are used to configure and operate ICs and electronic subsystem modules.

Building electronic projects has changed over the years.  Today ICs are very samll surface mount packages that are a challenge to work with by themselves.  Sometimes the IC can be found mounted on a small circuit board with other components as is shown in the above photo of two AD9833 [21 page data sheet PDF](https://www.analog.com/media/en/technical-documentation/data-sheets/ad9833.pdf) 0 MHz to 12.5 MHz Sine Square Wave DDS Signal Generator modules (module front side view & back side view).  Three AD9833 modules cost $12.99 with free shipping from [Amazon](https://www.amazon.com/dp/B09WV5LV3Q?ref=ppx_yo2ov_dt_b_product_details&th=1) 

Therefore, enstead of building a project with ICs it is common to use modules that contain the IC.  The modules bacome functional subsystems of the project.  For example, the AD9833 module contains seven other componets (25 MHz XTAL, caps & resistors) to make the AD9833 operational and eaiser to use.  
Also, in the past ICs had dedicated pins to control their functions.  To reduce cost and size those pins were replaced by serial interfaces (I2C, SPI, etc.)  The benefits are less pins, lower cost and smaller size.  In order to use the AD9833 a serial interface to a microcontroller or microporocessor with a three wire SPI interface is needed to configure and use the AD9833.  See the AD9833 Programmable Waveform Generator YouTube [video](https://youtu.be/PWj3QBuNFv8) show how to use the AD9833 module with a Arduino microcontroller.

In the above photo, the AD9833 module interface requires Vcc, DigitalGND, AnalogGND, three wire SPI (SDATA SPI serial data, SCLK SPI serial clock, FSYNC SPI frame synchronization) and the function generator output signal is at OUT.

YouTube
+ [Hamshield: Arduino meets amateur radio](https://youtu.be/xLTSlcZK14I)

## Microcontrollers are used to read, process, log and communicate sensor data.

For example, a microcontroller with a temperature sensor can be used as a remote weather station that uses a solar cel power system and Wi-Fi to report temperature to the Internet.

  
<A NAME="P7"></A>
<HR>
<P align="center"><A HREF="#P6">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P8">--&gt;</A></P>  

#  Project 7: RP2040 Microcontroller Introduction

<p align="center">
<img width="600" height="286" src="/Images/RP2040chip600.png">  
</p> 
    
Rasperry Pi Pico boards area  new popular low cost, powerful [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) that was created for education, makers, hobbyiest, etc. in January 2021. In less than two years over 2 million have been sold.  The RP2040 is the microcontroller IC used in the Pico boards.  The RP2040 is sold for $1 and is used by many other companies to create boards that include the RP2040.

The RP2040 is a dual core, 32-bit [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family) [Cortex M0+](https://developer.arm.com/Processors/Cortex-M0-Plus) ([Wikipedia](https://en.wikipedia.org/wiki/ARM_Cortex-M) processor that has very low power requirements. Therefore, it is a good choice for battery operation.

The Raspberry Pi [SBC](https://en.wikipedia.org/wiki/Single-board_computer), single board computers, are the third most popular personal computer behind Apple Mac OS, and Window PCs.  A SBC runs an operation system to interface to the user and runs various programs.  In contrast the RP2040 is a [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) design to interface to hardware to do a signal task. 

To use a microcontroller it is connected to additional electrical hardware using digital I/O, analog I/O, buses ([I2C](https://en.wikipedia.org/wiki/I%C2%B2C), [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface), [UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter), etc.). A compuer is used to develop the software to run one the microcontroller. The software is downloaded from the computer to the microcontroller board where is runs.  The software is saved on flash memory on the microcontroller board and runs when the board is power up and not connected to the computer.  When problems occur the computer is connected to the microcontroller board to debug it.

<p align="center">
  <img align="right" width="215" height="53" src="/Images/rpiLogo.png"> 
</p>

## [Raspberry Pi Foundation](https://en.wikipedia.org/wiki/Raspberry_Pi_Foundation)

Raspberry Pi Foundation helped redefine the personal computer market with the [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi) low cost single board computer running Linux.
In January 2021, Raspberry Pi Foundation entered the microcontroller market with a high performace low cost (1$ single unit) microcontroller RP2040 and its boards.  Raspberry Pi Foundation make the RP2040 available to other companies: Adafruit, Sparkfun, Ardinuo, etc. This has caused a explosion of low cost microcontroller [boards](https://en.wikipedia.org/wiki/RP2040) that include the RP2040.

  
<A NAME="P8"></A>
<HR>
<P align="center"><A HREF="#P7">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P9">--&gt;</A></P>  

# Project 8: Arduino Microcontroller Introduction

 <p align="center">
<img width="74" height="57" src="/Images/arduinoLogo.png"> 
</p>    
    
## Overview 
[Arduino](https://www.arduino.cc/) is a popular microcontroller that was created for education in ~2003. Over 10 million Uno boards have been sold since 2010.  

Arduino supports the RP2040 with the Arduino [Nano RP2040 Connect](https://store-usa.arduino.cc/products/arduino-nano-rp2040-connect-with-headers). 
+ Wikipedia: [Arduino](https://en.wikipedia.org/wiki/Arduino)

## Videos
+ Exploring the Next Generation of Arduino Microcontrollers (Pico) [video](https://youtu.be/HOi_AYEgSmo) - Glen Popiel, KW5GP
+ YouTube video [list](https://www.youtube.com/results?search_query=Arduino): Arduino
  - New Arduino Tutorials [List](https://www.youtube.com/playlist?list=PLGs0VKk2DiYw-L-RibttcvK-WBZm8WLEP) 68 videos

## Magazines
+ Hackspace issue [30](https://hackspace.raspberrypi.com/issues?page=3), [44](https://hackspace.raspberrypi.com/issues?page=2)
+ Internet Archive Arduino [list](https://archive.org/search.php?query=Arduino&sin=)

## Books
+ [Get Started with Arduino](https://hackspace.raspberrypi.com/articles/get-started-with-arduino-book)

  
<A NAME="P9"></A>
<HR>
<P align="center"><A HREF="#P8">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P10">--&gt;</A></P>  

# Project 9: RP2040 Development Boards Lists

Goal: Identify RP2040 microcontroller development boards that are available.
    
There is greater than 40 RP2040 microcontroller boards. 

+ Wikipedia list on [RP2040]([https://en.wikipedia.org/wiki/Adafruit_Industries](https://en.wikipedia.org/wiki/RP2040))
+ Earle F. Philhower, III GitHub [supported RP2040 boards](https://github.com/earlephilhower/arduino-pico)
+ Tom's Hardware [Best RP2040 Boards 2022](https://www.tomshardware.com/best-picks/best-rp2040-boards)
+ Electromaker [RP2040 Board Comparison - Which RP2040 Board Should You Buy](https://www.electromaker.io/blog/article/rp2040-board-comparison-which-rp2040-board-should-you-buy)
+ Electromaker [Electromakers guide to boards 2022](https://www.electromaker.io/board-guide?type=microcontroller&processor=RP2040)
+ Electromaker [Top 5 Alternatives to Raspberry Pi Pico](https://www.electromaker.io/blog/article/top-5-alternatives-to-raspberry-pi-pico)
+ Renzo Mischianti [Raspberry Pi Pico, W, and other rp2040 boards: pinout, specs, and Arduino IDE configuration – 1](https://www.mischianti.org/2022/09/26/raspberry-pi-pico-w-and-other-rp2040-boards-pinout-specs-and-arduino-ide-configuration-1/)
+ MUO [11 Alternatives to the Raspberry Pi Pico](https://www.makeuseof.com/alternatives-to-the-raspberry-pi-pico/)
+ All3DP [The Best RP2040 Boards of 2022 – Buyer’s Guide](https://all3dp.com/2/rp2040-board-buyers-guide/)

  
<A NAME="P10"></A>
<HR>
<P align="center"><A HREF="#P9">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P11">--&gt;</A></P>  

# Project 10: Raspberry Pi RP2040 Boards       
    
<p align="center">
  <img width="600" height="519" src="/Images/Picos600.png">  
</p>
The board on the bottom is a Pico and the board on the top is a Pico W.  Both boards have pins soldered on them.

[Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) boards
+ [Pico $4](https://www.adafruit.com/product/4864) has RP2040, clock chip, flash chip and 3.3V regulator chip
+ [Pico H $5](https://www.adafruit.com/product/5525) adds two 20 pin headers to the Pico.
+ [Pico W $6](https://www.adafruit.com/product/5526) adds WiFy chip to the Pico
+ [Pico WH $7](https://www.adafruit.com/product/5544) adds two 20 pin headers to the Pico W.
+ [RB2040 $1](https://www.adafruit.com/product/5041) is the RP2040 chip.

Wikipedia
+ [Raspberry Pi Foundation](https://en.wikipedia.org/wiki/Raspberry_Pi_Foundation)
+ [Raspberry Pi Pico](https://en.wikipedia.org/wiki/Raspberry_Pi#Raspberry_Pi_Pico)
+ [RP2040](https://en.wikipedia.org/wiki/RP2040)

[Assembly](https://www.elektormagazine.com/articles/assembly-language-on-the-pi-pico?utm_source=Elektor+International+%28English%29&utm_campaign=b25d197646-EMAIL_CAMPAIGN_2_16_2023_10_4&utm_medium=email&utm_term=0_23bd160f48-b25d197646-%5BLIST_EMAIL_ID%5D&mc_cid=b25d197646&mc_eid=1bc428feb9) Language on the Raspberry Pi Pico
 
 
  
<A NAME="P11"></A>
<HR>
<P align="center"><A HREF="#P10">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P12">--&gt;</A></P>  

# Project 11: [Adafruit Industries](https://www.adafruit.com/) [RP2040s](https://www.adafruit.com/?q=RP2040&sort=BestMatch) Boards

<p align="center">
<img width="479" height="229" src="/Images/AdafruitRP2040.jpg"> 
</p>
<p align="center">
<img align="right" width="220" height="75" src="/Images/Adafruit_logo.svg.png"> 
</p>       
    
Adafruit [(Wikipedia)](https://en.wikipedia.org/wiki/Adafruit_Industries) is develops and sells open source hardware and is localed in New Your city. Adafruit is an offical distributer of Raspberry Pi products.  Therefore, they sell the Raspberry Pi Pico family of products and the Raspberry Pi SBC produccts. Also, Adafruit develops there own RP2040

Above photo left to right:
  
<p align="center">
<img width="600" height="287" src="/Images/AdaP4884_600.png"> 
</p>  

+ [Adafruit P4884 Feather RP2040](https://www.adafruit.com/product/4884) with STEMMA QT
  + [ First Look at the Adafruit Feather RP2040 – Great Pico Alternative?](https://youtu.be/9a9Ug4g7vic) 

<p align="center">
<img width="600" height="324" src="/Images/AdaP4888_600.png"> 
</p>  

+ [Adafruit P4888 ItsyBitsy RP2040](https://www.adafruit.com/product/4888)
  + [Adafruit ItsyBitsy RP2040 Review - Great Mid-Size RP2040 Board!!](https://youtu.be/UCU1snzejbQ)
 
<p align="center">
<img width="600" height="493" src="/Images/AdaP4900_600.png"> 
</p>  
  
+ [Adafruit P4900 QT Py RP2040](https://www.adafruit.com/product/4900) with STEMMA QT
  + [First Look at the Adafruit QT Py RP2040 - Fantastic Tiny RP2040 Board!](https://youtu.be/qfbPyu_1L18)

<p align="center">
<img width="600" height="306" src="/Images/AdaP5056_600.png"> 
</p>  
  
+ [Adafruit P5056 Trinkey QT2040 - RP2040 USB Key with Stemma QT](https://www.adafruit.com/product/5056) with STEMMA QT
  
<p align="center">
<img width="600" height="326" src="/Images/AdaP5302_600.png"> 
</p>    
  
+ [Adafruit P5302 KB2040 - RP2040 Kee Boar Driver](https://www.adafruit.com/product/5302) with STEMMA QT
  + [New RP2040 Board from Adafruit – KB2040 Review!](https://youtu.be/BWsNLsmMKpY)
 
Some Adafriut product are available on Amazon.

Adafruit STEMMA QT is a easy to use (no soldering) I2C interface with small connectors on sensor boards and some RP2040 boards.
+ STEMMA QT [video](https://www.youtube.com/watch?v=6GXRRuFuFy0)

<p align="center">
  <img width="463" height="94" src="/Images/Python.png">  
</p>

Adafruit CircuitPython is based on [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) and is a fork of [MicroPython](https://micropython.org/) that support the Adafruit RP2040 boards, Raspberry Pi Pico boards (Adafruit sells them) and the large selection of Adafriut sensors boards.  CircuitPython works great with the Mu IDE.  CircuitPython has RP2040 functions like deep sleep that are not in CircuitPython.
+ [CircuitPython](https://circuitpython.org/)
  + [Getting Started with Raspberry Pi Pico and CircuitPython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython)
  + [CircuitPython library](https://www.adafruit.com/category/956) >280 Python libraries.

  
<A NAME="P12"></A>
<HR>
<P align="center"><A HREF="#P11">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P13">--&gt;</A></P>  

# Project 12: [Arduino](https://www.arduino.cc/) Nano RP2040 Connect Board

<p align="center"> 
<img width="600" height="557" src="/Images/ArdNANORPtb600.png">
</p>
<p align="center">
<img align="right" width="74" height="57" src="/Images/arduinoLogo.png"> 
</p>  
   
<p align="center">
Arduino Nano RP2040 Connect Microcontroller Board.
</p>

+ Above photo is an [Arduino Nano RP2040 Connect](https://store-usa.arduino.cc/products/arduino-nano-rp2040-connect-with-headers)
+ [YouTube Short First power on by WA9ONY](https://www.youtube.com/shorts/O2xxTe2i11w)
+ Arduino RP2040 librar [list](https://www.arduinolibraries.info/architectures/rp2040)

  
<A NAME="P13"></A>
<HR>
<P align="center"><A HREF="#P12">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P14">--&gt;</A></P>  
       
# Project 13: [Seeed Studio](https://www.seeedstudio.com/) RP2040 Boards

<P align="center">
<img width="600" height="527" src="/Images/SeedXIAO600.png"> 
</p>

<p align="center">
<img align="right" width="225" height="54" src="/Images/seedstudioLogo.png"> 
</p>
    
Some Seeed Studio products are available from [Amazon](https://www.amazon.com/s?k=Seeed+Studio&crid=PQF86EWIGSXL&sprefix=seeed+studio%2Caps%2C197&ref=nb_sb_noss_1)
+ [RP2040s](https://www.seeedstudio.com/catalogsearch/result/?q=rp2040)
+ [XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html?queryID=9178e9456690e66382d9d6934ff4ae0a&objectID=5026&indexName=bazaar_retailer_products)

  
<A NAME="P14"></A>
<HR>
<P align="center"><A HREF="#P13">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P15">--&gt;</A></P>  
       
# Project 14: [SparkFun](https://www.sparkfun.com/) RP2040 Boards

<p align="center">
<img align="right" width="169" height="83" src="/Images/sparkfunLogo.png"> 
</p>

<P>
&nbsp; 
</P>
 
Some SparkFun products are available from [Amazon](https://www.amazon.com/s?k=SparkFun&crid=6GWYUPXP9EMB&sprefix=sparkfun%2Caps%2C310&ref=nb_sb_noss_1)
  + [RP2040s](https://www.sparkfun.com/search/results?term=RP2040)
 
 <P align="center">
<img width="600" height="332" src="/Images/SparkFunProMicor600.png"> 
</p>  
  
  + [SparkFun Pro Micro - RP2040](https://www.sparkfun.com/products/18288)
    + [SparkFun Pro Micro RP2040 Review: The Best Small RP2040 Board?](https://youtu.be/kzDJy8ZabRM)
  
<P align="center">
<img width="600" height="259" src="/Images/SparkFunThingPlus600.png"> 
</p>    
  
  + [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/products/17745)
  + [WizFi360-EVB-Pico](https://www.sparkfun.com/products/19959)
  + [W5500-EVB-Pico](https://www.sparkfun.com/products/19958)

  
<A NAME="P15"></A>
<HR>
<P align="center"><A HREF="#P14">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P16">--&gt;</A></P>  
          
# Project 15: [Waveshare](https://www.waveshare.com/) RP2040 Boards

<p align="center">
<img align="right" width="299" height="61" src="/Images/waveshareLogo.png"> 
</p>
    
Some Waveshare products are available from [Amazon](https://www.amazon.com/s?k=Waveshare&crid=AJL406YJVRKX&sprefix=waveshare%2Caps%2C136&ref=nb_sb_noss_1)
+ [RP2040s](https://www.waveshare.com/catalogsearch/result/?q=RP2040)
  
<P align="center">
<img width="600" height="449" src="/Images/WsRP2040Zero600.png"> 
</p>
  
+ [RP2040-Zero](https://www.waveshare.com/rp2040-zero.htm)
  
<P align="center">
<img width="600" height="334" src="/Images/RP2040One600.png"> 
</p>  
  
+ [RP2040-One](https://www.amazon.com/gp/product/B0BLMPDMLD/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
  
<P align="center">
<img width="600" height="264" src="/Images/RP2040Plus600.png"> 
</p>  
  
+ [RP2040-Plus Mini Board](https://www.amazon.com/dp/B0B6BM7CVT?psc=1&smid=A2SA28G0M1VPHD&ref_=chk_typ_imgToDp)

  
<A NAME="P16"></A>
<HR>
<P align="center"><A HREF="#P15">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P17">--&gt;</A></P>  
       
# Project 16: Micorocontrollers Programming   
    
Software
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

  
<A NAME="P17"></A>
<HR>
<P align="center"><A HREF="#P16">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P18">--&gt;</A></P>  
       
# Project 17: Arduino IDEs on Linux Computer

<p align="center"><img width="960" height="540" src="/Images/ArduinnoIDEsS.png"></p>

The above screenshot shows the three [Arduino IDEs](https://www.arduino.cc/en/software) open on an Ubuntu computer.  The far left is the Web Editor, upper right corner is IDE V1,8.19 and bottom left corner is IDE 2.0.3.  All three IDEs have the example Blink sketch loaded.
 
The three versions of Arduino IDEs on an [Ubuntu Linux](/Images/UbuntuS.png) computer.
## [Web Editor](https://docs.arduino.cc/arduino-cloud/getting-started/getting-started-web-editor) 
+ Need to have an Arduino account (no cost).
+ Web Editor needs the Arduino Create Agent installed to communicate to the Arduino board.
+ To use the [Arduino Cloud](https://cloud.arduino.cc/home/) the [free Cloud account](https://cloud.arduino.cc/plans/) provides 100 MBytes of storage. 
+ Later the Arduino IoT Cloud will be used in projects.  The Arduino Cloud and Arduino IoT Cloud are different.
## IDE [V2.0.3](https://www.arduino.cc/en/software)
+ No program icon was created.
+ V2 has a debugger.
+ Editor auto completes.

<PRE> 
Version: 2.0.3
Date: 2022-12-05T09:27:52.215Z
CLI Version: 0.29.0 [76251df9]

Copyright © 2022 Arduino SA 
</PRE> 
 
## IDE [V1.8.19](https://www.arduino.cc/en/software) 
+ Icon installed in applications screen.
+ install needed the /dev/ttyACM* permison to be fixed as show in the below CLI history.
  + [Permission denied on /dev/ttyACM0](https://forum.arduino.cc/t/permission-denied-on-dev-ttyacm0/475568)

CLI history to fix permission denied issue. 
 
<PRE>
1272  cd arduino-1.8.19
1273  ls
1274  ./install.sh 
1275  sudo ./install.sh 
1276  ls -l /dev/ttyACM*
1277  group
1278  groups
1279  sudo adduser david dialout
1280  history
</PRE>

YouTubes
+ [Arduino Cloud Explained](https://youtu.be/uaLrmLCqGnc)
+ [Arduino IDE vs. Arduino IoT Cloud Editor](https://youtu.be/lL1caDBLlhA)
 
 
  
<A NAME="P18"></A>
<HR>
<P align="center"><A HREF="#P17">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P19">--&gt;</A></P>  
       
# Project 18: Build a Computer for Microcontroller Development

<p align="center"><img width="640" height="480" src="/Images/P400.jpg"></p>

+ The computer needs to run these IDEs
  + MicroPython - Thonny IDE
  + CircuitPython - Mu IDE
 
 + Limitations
   + Arduino Web Editor is not support because the Arduino Create Agent does not run of the Raspberry Pi computers.
   + Arduino V2 has no install for the Raspberry Pi computers.
 
To use the Pico a computer with a Pico [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) is needed.
To use the Pico.
1. Create a Pico program in the IDE.
2. Download the program into the Pico.
3. Run the program.
4. Debug the program in the IDE.

Use Raspberry Pi P400 computer.
Create a new microSD card with latest OS with full install.
The full install includes Thonny and Mu.

  
<A NAME="P19"></A>
<HR>
<P align="center"><A HREF="#P18">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P20">--&gt;</A></P>  
       
# Project 19: Setup GitHub

<p align="center"><img width="700" height="1076" src="/Images/GitHubL2_700.png"></p>

Goals
+ Create GitHub account
+ Create RP2040 and Arduino repo. 
+ Use GitHub web interface to create the README.md file.
 
 
[GitHub](https://github.com/) is a global home for all developers, GitHub is the complete developer platform to build, scale, and deliver secure software. Over 100 million people, including developers from 90 of the Fortune 100 companies, use GitHub to build amazing things together across 330+ million repositories. With all the collaborative features of GitHub, it’s never been easier for individuals and teams to write faster, better code.

Embedded World 2023 session: DevOps with arm Virtual Hardware enabled GitHub Actions by Clay Nelson
 
GitHub is a great way to document and share RP2040 and Arduino projects.
+ The GitHub home READ.md file provides a place to documenting the projects.
+ The GitHub provides free file storage ([repository](https://en.wikipedia.org/wiki/Repository_(version_control))) and version change control.
+ GitHub uses a web interface or a Linux CLI interface.
+ The Raspberry Pi P400 full install includes git CLI.

## GitHub Repo
+ [WA9ONY/RP2040_and_Arduino](https://github.com/WA9ONY/RP2040_and_Arduino)
+ Over 40 amateur radio Arduino [repositories](https://github.com/search?q=amateur+radio+arduino)
+ Over 40 ham radio Arduino [repositories](https://github.com/search?q=ham+radio+arduino)
+ Over 3,100 Raspberry Pi Pico [repositories](https://github.com/search?q=Raspberry+Pi+Pico)
  + [raspberrypi/pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples)
+ Over 257,000 Arduino [repositories](https://github.com/search?q=Arduino) 
+ Over 1,100 ham radio [repositories](https://github.com/search?q=ham+radio)
+ Over 1,000 amateur radio [repositories](https://github.com/search?q=amateur+radio)
  
## Resources
+ Articles
  + Wikipedia [GitHub](https://en.wikipedia.org/wiki/GitHub)
  + [SSH key for GitHub](https://garywoodfine.com/setting-up-ssh-keys-for-github-access/) files upload
+ Videos
  + YouTube [list](https://www.youtube.com/results?search_query=GitHub)
+ Books
  + Amazon [list](https://www.amazon.com/s?k=Github+in+books&crid=2SACFZLPDLFD9&sprefix=github+in+books%2Caps%2C148&ref=nb_sb_noss_1)   

  
<A NAME="P20"></A>
<HR>
<P align="center"><A HREF="#P19">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P21">--&gt;</A></P>  
        
# Project 20: Learn Micropython on the Pico

<p align="center">
  <img  width="200" height="300" src="/Images/MicroPythonPico_Cover.jpg">  
</p>

Goals
+ Learn how to program the Pico in [MicropPython](https://micropython.org/).
+ Learn how to use the [Thonny](https://thonny.org/) IDE.
+ Learn about the [Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) I/O.

## Resources
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
  + GitHub: [raspberrypi/pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples)

  
<A NAME="P21"></A>
<HR>
<P align="center"><A HREF="#P20">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P22">--&gt;</A></P>  
       
# Project 21: Setup Pico with MicroPython

<p align="center">
  <img width="640" height="480" src="/Images/dataLogVTemp2.jpg">  
</p>

Goal
+ Setup the Pico to run [MicoPython](https://micropython.org/) with the Raspberry Pi P400 computer.
+ Configure the Pico for MicoPython.
+ Use [Thonny](https://thonny.org/) to create, edit and debug MicoPython programs to run on the Pico.

Steps
+ Download the [MicoPython UF2 file](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
+ Hold the Pico Boot switch down when plugging the Pico into the P400.
+ The Pico will mount as a memory device.
+ Drage and drop the MicoPython UF2 file of the Pico memory.
+ The Pico will unmount and be ready to use MicoPython with Thonny with is all ready installed on the P400.
 
Links
+ Get Started with MicroPython on Raspberry Pi Pico, 139 pages [PDF](https://hackspace.raspberrypi.com/books/micropython-pico) 
  + The best Pico book to start with.
+ [MicroPython on the Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
 
  
<A NAME="P22"></A>
<HR>
<P align="center"><A HREF="#P21">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P23">--&gt;</A></P>  

# Project 22: Run Pico on Batteries

<p align="center">
  <img width="640" height="480" src="/Images/voltsTemp.jpg">  
</p>

Goal
+ Design a circuit so that the Pico automatically runs on the USB micro connector or a battery input.
+ The Pico automatically switch to the highest voltage.
+ Protect both sources from loading down the other souce.

Design
+ Vbus is the USB voltage.
+ Vsys is the Vbus with a Shottky diode on the Pico PCB.
+ Vsys goes to the Pico voltage regulator that provides 3.3 Volts to the Pico, flash and clock chips.
+ Vsys is rate for 1.8 V to 5.5 V.
+ Connect the battery Vbattery to Vsys using a Shottky diode 1N5817.  Therefore, the highest voltage Vbus or Vbattery will power the Pico.
+ The above image shows [Treedix Compatible with Raspberry PI PICO Expansion Board PCB Shield Board Gold Plated Finish with Pin Header](https://www.amazon.com/gp/product/B08YDNMP46/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1) 
 
 
<A NAME="P23"></A>
<HR>
<P align="center"><A HREF="#P22">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P24">--&gt;</A></P>  

# Project 23: Power the Pico on Solar Cells

<p align="center">
  <img width="640" height="480" src="/Images/solar1.jpg"> 
  <img width="640" height="480" src="/Images/solar2.jpg">  
</p>

Goal
+ Use a low cost [solar cells](https://www.amazon.com/gp/product/B0B5G2BD5P/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1) that are design for remove cameras that provide upto 5V, 5 Watts.
+ Find a solar cell with a micro USB connector that will plug directly into the Pico microcontroller board.
+ Test the solar cell/battery power configuration.
+ Find a water proof box for the Pico and battery.

Results
+ Plastic [0.30 Caliber Ammo Box](https://www.harborfreight.com/030-caliber-ammo-box-63135.html?_br_psugg_q=ammo+box)
+ The solar cell panel plugs into the Pico micro USB connector.
+ More testing will be done. 
 
  
<A NAME="P24"></A>
<HR>
<P align="center"><A HREF="#P23">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P25">--&gt;</A></P>  

# Project 24: Use Pico A/Ds to Measure Vbus, Vsys and Vbattery Voltage

<p align="center">
  <img width="640" height="480" src="/Images/adVoltsDivider.jpg">  
</p>

Goal
+ Use the Pico three A/D converters to measure Vbus, Vsys and Vbattery voltage.
+ Design a 50% voltage divider to prevent damage to the A/D inputs that have a maximum of 3.3 Volts.
+ Test how low Vbattery can go before the Pico stops operating.
 
Implementation: 
+ The Raspberry Pi Pico A/D inputs have a maximum voltage rating of 3.3 Volts.
+ The Vbus is the USB voltage which can be upto 5.25 Volts.
+ A voltage divider of two 1 Mohm 1% 1/4 watt resistors are used to reduce the voltage in half.
+ The two  1 Mohm 1% resistors will provide a small load of 2 Mohms to the voltage sources being measured.
+ The software has a single point calibration adjustment to agree with an external DMM reading. 
+ The above image is of the six resistors and the Schottky diode (1N5817) for the battery supply portection from the USB 5 Volts. 
+ [Treedix Compatible with Raspberry PI PICO Expansion Board PCB Shield Board Gold Plated Finish with Pin Header](https://www.amazon.com/gp/product/B08YDNMP46/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1) is being used.
+ Two AA batteries are connected to the Vsys through the 1N5817 Schottky diode.

Results 
+ Pico will operate down to ~1.9 volts on two AA batteries. This is very impressive.
+ The internal Schottky diode between Vbus and Vsys has a very low volage drop of ~.2 Volts.
+ The 1N5817 Schottky diode voltage drop is ~.4 Volts.
  
 
<A NAME="P25"></A>
<HR>
<P align="center"><A HREF="#P24">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P26">--&gt;</A></P>  

# Project 25: Use Pico A/D to Measure CPU Temperature

<p align="center">
  <img width="640" height="480" src="/Images/dataLogVTemp.jpg">  
</p>

Goal
+ Use the A/D converter to measure CPU temperature.
+ Use the A/D converter to measure the Vbus, Vsys and Vbattery voltage.
+ Use the internal real-time clock to time mark the data readings.
+ Save time, Vbus, Vsys, Vbattery and temperature to data log on the Pico flash memory.

Data log is saved to Pico flash memory.
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

  
<A NAME="P26"></A>
<HR>
<P align="center"><A HREF="#P25">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P27">--&gt;</A></P>  

# Project 26: Run the Arduino IDE & Arduno Uno R3

<p align="center">
  <img width="241" height="341" src="/Images/ProgrammingArduino3rd.png">     
</p>
<p align="center">   
  <img align="right" width="92" height="94" src="/Images/Arduino1_8.png"> 
</p>

The 3rd edition is 2023 and contains a brief section on the Arduino NANO RP2040 Connect. 
 
Book's purpose:
+ Learn how to use Arduino IDE.
+ Learn how to program the Arduno Uno R3.
+ Lear Arduino C++.

Resources
+ [Arduino IDE V1.8](https://www.arduino.cc/en/software) runs on a Linux computer (Intel NUC8).
+ Arduino Uno R3 microcontroller board is used in the book.
+ [Programming Arduino: Getting Started with Sketches, Third Edition 3rd Edition, 2023](https://www.amazon.com/gp/product/B0BKV9RMVT/ref=ppx_yo_dt_b_d_asin_image_o00?ie=UTF8&psc=1) 176 pages 
  + [Amazon Simon Monk page of books](https://www.amazon.com/stores/Simon-Monk/author/B003VOT2DI?ref=ap_rdr&store_ref=ap_rdr&isDramIntegrated=true&shoppingPortalEnabled=true)
  + [Monk Makes LTD](https://www.monkmakes.com/#)
  + [SimonMonk.org](http://simonmonk.org/) 
  + I enjoy Simon Monk's books. 
+ 1st & 2nd editions [downloads](http://www.arduinobook.com/progardui2ed/)
+  Simon Monk [GitHub](https://github.com/simonmonk) 

  
<A NAME="P27"></A>
<HR>
<P align="center"><A HREF="#P26">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P28">--&gt;</A></P>  
    
# Project 27: Using the GiHub Web Interface

<p align="center">
  <img width="340" height="97" src="/Images/GitHub_logo.png"> 
</p>

The free GitHub account supports two types of interfaces.
+ GitHub web interface operated with a web browser.
+ GitHub to git interface. On a Linux computer git is a CLI command.  
  
The GitHub has a web inferface to 
+ Create the repo README.md file, this file you are reading.
+ Create, edit & delete files in the repo.  
+ Upload and delete files in the repo.
+ Create folders in the repo.

The GitHuib web interface changes to the repo all require a Commit Changes to take effect.
  
On the repo home page is a README.md file that is shown to the user when the repo is shown in a browser.  The README.md explains the purpose and how to use the repao.
 
README.md file 
+ README.md file formating syntax
  + Basic writing and formatting [syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
  + GitHub Flavored Markdown [Spec](https://github.github.com/gfm)
  + markdown-it [demo](https://markdown-it.github.io/)
+ My README.md file is supported by two folders: 
  + BookContents contains PDFs and PNGs of the eight books related to ham radio.
  + Images contains images used in the README.md file.
+ Some HTML code works in the .md file.
+ To create a folder a new file is created in the new folder at the same time.    

  
<A NAME="P28"></A>
<HR>
<P align="center"><A HREF="#P27">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P29">--&gt;</A></P>  
    
# Project 28: Arduino Cloud

<p align="center">
<img width="157" height="54" src="/Images/ArduinoCloud.png"> 
</p> 
<p align="center"> 
<img width="600" height="557" src="/Images/ArdNANORPtb600.png">
</p>
 
 Arduino Cloud is Arduino’s integrated cloud platform to develop, deploy and manage IoT devices.
 + [Supported boards](https://store-usa.arduino.cc/pages/cloud-compatible-boards)
 + Above image is the Arduino NANO RP2040 Connect which supports Arduino IoT Cloud.
 
 Webinar
 + [Arduino Cloud Explained](https://www.crowdcast.io/e/arduino-cloud-explained)
   + Thu, Jan 12, 2023 8:00 AM PST
 + [Arduino Cloud for Education](https://arduino-cc.zoom.us/webinar/register/WN_2VO0jFXFSbWy29bsHT3_-Q)
   + Q & A [pdf](https://maildoc.io/file/d55ecc8d3ba124bb32fb8b6f834377a1c9b2dcae3a1d7bd85bfbe1a57b389e28?u=9312464&hash=a2847c0d8d911d2a4a55eda6ef168f0aa6d27410&iti=ead01cdc-af8f-4a91-aeda-ed95ac450cf8&w=V0E5T05ZQGdtYWlsLmNvbQ)
 
 Links
 + [Arduino Cloud How it Works](https://cloud.arduino.cc/how-it-works/)
 + [Use Cases](https://cloud.arduino.cc/use-cases/)

 YouTube
 + [Arduino Cloud play list 16 videos](https://www.youtube.com/watch?v=uaLrmLCqGnc&list=PLT6rF_I5kknObk6lnQMpk5NIUB_vEHcNW)
 + [Smart Lights and Automated Lighting using Arduino Cloud](https://youtu.be/eDcUefyDLZw)
 + [Making Your Plants Smart with Arduino Cloud](https://youtu.be/RsmPT4kAUl8)
 + [How to Integrate Amazon Alexa with Arduino Cloud](https://youtu.be/OMvZjwFYimo)
 + [Arduino IoT Cloud 2021 - Getting Started with Arduino & ESP32](https://youtu.be/UFCmTZUoZ1M)
 
  
<A NAME="P29"></A>
<HR>
<P align="center"><A HREF="#P28">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="#P30">--&gt;</A></P>  
    
# Project 29: Arduino Microcontroller Boards

<p align="center">
<img width="600" height="557" src="/Images/ArdNANORPtb600.png"> 
</p> 

Arduino NANO RP2040 Connect on [Amazon](https://www.amazon.com/gp/product/B095J4KFVT/ref=ppx_yo_dt_b_asin_image_o01_s00?ie=UTF8&psc=1)
YouTube
+ [First Look at the Arduino Nano RP2040 Connect – It’s finally here!](https://youtu.be/rw_LifhqGjw) 
+ [How To Use the RGB LED on the Arduino Nano RP2040 Connect - Tutorial 1: Rainbow LED Effect](https://youtu.be/mZxJxPZuhMs)

 <p align="center">
<img width="600" height="248" src="/Images/ArdPortentaH7rev2back600.png">   
<img width="600" height="251" src="/Images/ArdPortentaH7rev2front600.png"> 
</p>  

Arduino Portenta H7 Rev 2 on [Amazon](https://www.amazon.com/dp/B088KPDM8S?psc=1&ref=ppx_yo2ov_dt_b_product_details).

Portenta H7 is expensive and is a part of the [PRO](https://www.arduino.cc/pro/) family product line that is aimed at professional use.

The top image is the Portenta H7 Rev 2 back side with two high density connectors that plug into a [Portenta breakout board](https://www.amazon.com/gp/product/B09FBV5GH7/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1).
 
<p align="center">
<img width="600" height="257" src="/Images/ArdNANO33BLE600.png"> 
</p> 

Arduino NANO 33 BLE on [Amazon](https://www.amazon.com/dp/B07WV59YTZ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
  
<p align="center">
<img width="600" height="254" src="/Images/ardMKR1000wifi600.png"> 
</p> 

Arduino MKR1000 WIFI on [Amazon](https://www.amazon.com/dp/B071LRYYHH?psc=1&ref=ppx_yo2ov_dt_b_product_details)
 
<p align="center">
<img width="600" height="250" src="/Images/ArdMICRO600.png"> 
</p>  

Arduino Micro on [Amazon](https://www.amazon.com/dp/B00AFY2S56?ref=ppx_yo2ov_dt_b_product_details&th=1)
  
<p align="center">
<img width="600" height="265" src="/Images/ArdNANOfront600.png"> 
<img width="600" height="279" src="/Images/ArdNANOback600.png">  
</p> 

Arduino NANO on [Amazon](https://www.amazon.com/dp/B0097AU5OU?psc=1&ref=ppx_yo2ov_dt_b_product_details)

<p align="center">
<img width="600" height="442" src="/Images/ArdUNOWIFI_600.png"> 
</p>  

Arduino Arduino UNO WiFi Rev2 on [Amazon](https://www.amazon.com/dp/B07MK598QV?psc=1&ref=ppx_yo2ov_dt_b_product_details)
 
<p align="center">
<img width="600" height="443" src="/Images/ArdUNOSMD600.png"> 
</p>  

Arduino UNO SMD is a Arduino UNO R3 with a surface mount chip on [Amazon](https://www.amazon.com/dp/B007R9TUJE?psc=1&ref=ppx_yo2ov_dt_b_product_details).
  
<p align="center">
<img width="600" height="443" src="/Images/ArdUNOR3600.png"> 
</p>  
  
Arduino UNO R3, over 10 million have been sold.
 
On [Amazon](https://www.amazon.com/dp/B008GRTSV6?psc=1&ref=ppx_yo2ov_dt_b_product_details).
 
The Elegoo clone of the board is in the image below in project 30. 

 
<A NAME="P30"></A>
<HR>
<P align="center"><A HREF="#P29">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="README2.md#P31">--&gt;</A></P>  
    
# Project 30: Arduino Clone Microcontroller Boards

Arduino is an [open-source hardware](https://en.wikipedia.org/wiki/Open-source_hardware) and software company.
Therefore, Arduino designs are  used by other manufactures to build products that are almost identical to the Arduino products except for the Arduino registered [trademark](https://en.wikipedia.org/wiki/Trademark) which is only on Arduino products.

<p align="center">
<img width="600" height="431" src="/Images/ElegooUNOR3_600.png"> 
</p>  
  
Elegoo UNO R3 is a clone of the Arduino UNO R3 except it uses Elegoo logo instead of the Arduino trademark.

Elegoo UNO R3 USB interface identifies itself an Arduino UNO R3.
 
[ELEGOO UNO R3 Project Most Complete Starter Kit w/ Tutorial Compatible with Arduino IDE (63 Items)](https://www.amazon.com/gp/product/B01CZTLHGE/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1)

Elegoo YouTube Videos
+ [Get Started in Electronics #1 - Elegoo Arduino Uno Super Starter Kit](https://youtu.be/A21eaw4V8_4)
+ [UNO](https://www.youtube.com/playlist?list=PLkFeYZKRTZ8bWpkBHe7qp4rJczTJyvUI5)
+ [UNO V2](https://www.youtube.com/playlist?list=PLkFeYZKRTZ8b88C3gXKaLbGaJUB-jZBRU) 
+ [MEGA](https://www.youtube.com/playlist?list=PLkFeYZKRTZ8abqae2cQZ1-ztcuZuIt4G7)
 
[Elegoo files](https://www.elegoo.com/pages/arduino-kits-support-files)
 
 
<p align="center">
<img width="600" height="537" src="/Images/LafvinNANOtb600.png"> 
</p>  
  
[LAFVIN Nano V3.0, Nano Board ATmega328P 5V 16M Micro-Controller Board Compatible with Arduino IDE (Nano x 3 with USB Cable)](https://www.amazon.com/dp/B07G99NNXL?psc=1&ref=ppx_yo2ov_dt_b_product_details)
 
 <p align="center">
<img width="600" height="249" src="/Images/ArdNANO600.png"> 
</p>  

Aideepen V3.0 NANO on [Amazon](https://www.amazon.com/dp/B0BLW3881B?psc=1&ref=ppx_yo2ov_dt_b_product_details)
  

<HR>
<P align="center"><A HREF="#P29">&lt;--</A> <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="#INDEX">Index</A> - <A HREF="http://www.stargazing.net/david/RPi/index.html">RPi</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> <A HREF="README2.md#P31">--&gt;</A></P>  

End of Projects 1 -30.  Projects 31+ are in [README2.md](README2.md).
