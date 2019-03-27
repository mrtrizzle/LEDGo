# LEDGo
A JS / Python control interface for a fadecandy-driven 8x8 LED matrix

[![LED GO](https://img.youtube.com/vi/OWNRfNsfjfw/0.jpg)](https://www.youtube.com/watch?v=OWNRfNsfjfw)

## Hardware Collection

* Fadecandy case from [thingiverse](https://www.thingiverse.com/thing:1346770)
* Sockets from Conrad [on board](https://www.conrad.de/de/wuerth-elektronik-stiftleiste-standard-wr-bhd-polzahl-gesamt-16-rastermass-254-mm-61201621621-1-st-1088165.html) and [counterpart](https://www.conrad.de/de/wuerth-elektronik-buchsenleiste-rastermass-254-mm-polzahl-gesamt-16-anzahl-reihen-2-1-st-1088171.html?sc.ref=Product%20Details)

## TODO Brainstorming

- [ ] Connection status to fadecandy server / LED matrix
- [ ] Some default color palettes  
- [ ] Drawing by hold-and-pull
- [ ] Activation of animations
- [ ] Selfmade animations by drawing multiple keyframes
- [ ] Sliding text to matrix
- [x] Optimize for mobile usage (on smartphone)


## Color Palette Sliders

1. 4 Sliders: Hue (0-360), Variance (Hue / # colors), Saturation (0-100), Lightness (0- 90)
2. Calc HSL-Color for Color `c_i` = `hsl(hue + i* variance, saturation, lightness)` with `i=0,...,k`

(see [codepen](https://codepen.io/mburridge/pen/PVVMXJ?editors=1010))