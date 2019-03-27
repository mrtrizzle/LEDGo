# LEDGo
A JS / Python control interface for a fadecandy-driven 8x8 LED matrix

[![LED GO](https://img.youtube.com/vi/OWNRfNsfjfw/0.jpg)](https://www.youtube.com/watch?v=OWNRfNsfjfw)



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