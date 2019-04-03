# LEDGo
A JS / Python control interface for a fadecandy-driven 8x8 LED matrix

[![LED GO](https://img.youtube.com/vi/OWNRfNsfjfw/0.jpg)](https://www.youtube.com/watch?v=OWNRfNsfjfw)

## Hardware Collection

* Fadecandy case from [thingiverse](https://www.thingiverse.com/thing:1346770)
* Sockets from Conrad [on board](https://www.conrad.de/de/wuerth-elektronik-stiftleiste-standard-wr-bhd-polzahl-gesamt-16-rastermass-254-mm-61201621621-1-st-1088165.html) and [counterpart](https://www.conrad.de/de/wuerth-elektronik-buchsenleiste-rastermass-254-mm-polzahl-gesamt-16-anzahl-reihen-2-1-st-1088171.html?sc.ref=Product%20Details)

## TODO Brainstorming

- [x] Connection status to fadecandy server / LED matrix

**Drawing**: 

- [ ] Some default color palettes  
- [x] Drawing by hold-and-pull
  - [ ] Also for mobile?
- [ ] Selfmade animations by drawing multiple keyframes
- [ ] Saving Images?

**Other**: 

- [x] Activation of animations
- [x] Include Perlin Noise as animation  
  - [ ] Think of a way to parameterize the script (at least chose between 4 matplotlib colormaps)
- [ ] Sliding text to matrix
- [x] Optimize for mobile usage (on smartphone)
- [ ] Flask Restart option (see [Stackoverflow](https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself)) - needed if accessed by multiple devices?


## Color Palette Sliders

1. 4 Sliders: Hue (0-360), Variance (Hue / # colors), Saturation (0-100), Lightness (0- 90)
2. Calc HSL-Color for Color `c_i` = `hsl(hue + i* variance, saturation, lightness)` with `i=0,...,k`

(see [codepen](https://codepen.io/mburridge/pen/PVVMXJ?editors=1010))