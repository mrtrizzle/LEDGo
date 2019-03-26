
var pixelGrid = null;

// Shorthand for $(document).ready(function)
$(function () {
   
   var $pixelGrid = $('#pixel-grid');
   
   
   pixelGrid = {
		canvas: null,
      c2d: null,
      canvasW: 428,
      canvasH: 428,
      numPixelsX: 8,
      numPixelsY: 8,
      pixelSize: 50,
      pixelSpacing: 4,
      pixels: [],
      
      init: function() {
         var canvas = document.createElement('canvas');
         this.handleSizes();
         canvas.width = this.canvasW;
         canvas.height = this.canvasH;
         $pixelGrid.append(canvas);
         this.canvas = canvas;
         this.c2d = canvas.getContext('2d');
         
         this.initPixels();
         this.renderLoop();
         
         $pixelGrid.addClass('appear');
         
         canvas.addEventListener('click', this.bind(this, this.handleClick));
         
         console.log("Init done..");
      },

      handleSizes: function() {
         if($(window).width() <= 500) {
            var size = $(window).width()
            this.canvasW = size * 0.9;
            this.canvasH = size * 0.9;

            this.pixelSize = (this.canvasH / this.numPixelsX) - this.pixelSpacing;
         }  
      },
      
      bind: function(scope, fn) {
         return function() {
            return fn.apply(scope, arguments);
         }
      },
      
      initPixels: function () {
         for(var y = 0; y < this.numPixelsY; y++) {
            for(var x = 0; x < this.numPixelsX; x++) {
					var pixel = this.createPixel(x, y);
               this.pixels.push(pixel);
            }
         }
      },
      
      handleClick: function(e) {         
         x = Math.floor(e.offsetX / (this.pixelSize+this.pixelSpacing));
         y = Math.floor(e.offsetY / (this.pixelSize+this.pixelSpacing));
         
         /*
         var col = 'rgb('+Math.floor(Math.random() * 256) + "," +
             Math.floor(Math.random() * 256) +","+
             Math.floor(Math.random() * 256) +")";
             */

         var col = 'rgb(' + r.getValue() + "," + g.getValue() + "," + b.getValue() + ")";
         
         if (x < this.numPixelsX &&
             y < this.numPixelsY) {
            this.setPixel(x,y,col);
         }
         
      },
      
      createPixel: function (x, y) {
         return {
            xPos: x * this.pixelSize + (x * this.pixelSpacing),
            yPos: y * this.pixelSize + (y * this.pixelSpacing),
            alpha: 100,
            bgColor: 'rgb(50,50,50)',
            color: 'rgb(0,0,0)',
            
            getShownColor : function() {
               if (this.color == 'rgb(0,0,0)') {
                  return this.bgColor;
               } else {
                  return this.color;
               }
            }
         };
      },

      renderLoop: function () {
         
         this.clearCanvas();
         this.renderPixels();

         //window.requestAnimationFrame(function () { this.renderLoop(); }.bind(this));
      },
      
      renderPixels: function () {
         for(var i = 0; i < this.pixels.length; i++) {
            this.drawPixel(this.pixels[i]);
         }
      },
      
      drawPixel: function (pixel) {   
         if (pixel.color == 'rgb(0,0,0)'){
            this.c2d.fillStyle = pixel.bgColor;   
         } else {
            this.c2d.fillStyle = pixel.color;  
         }
         this.c2d.fillRect(pixel.xPos, pixel.yPos, this.pixelSize, this.pixelSize);
      },
      
      clearCanvas: function () {
         this.c2d.fillStyle = this.bgColor;
         this.c2d.fillRect(0, 0, this.canvasW, this.canvasH);
      },
      
      setPixel:function(x,y,color) {
         var oldColor = this.pixels[x+y*this.numPixelsY].color;

         this.flaskPixelUpdate(x,y, color);
         
         var id = setInterval(this.bind(this,frame),10);
         var alpha = 0.0;
         
         function frame() {
            if (alpha > 1) {
               clearInterval(id);
               this.pixels[x+y*this.numPixelsY].color = color;
            } else {
               alpha += 0.05;
               var rgba = color.replace(')', ','+alpha+')').replace('rgb', 'rgba');
               this.colorDrawPixel(this.pixels[x+y*this.numPixelsY], rgba);
            };
         }
      },


      flaskPixelUpdate: function(x,y,color) {
         console.log("Sending pixel update to backend...");
         
         $.ajax({
            method: 'POST',
            url: setPixel,
            data: {'x': x, 'y': y, 'color': color},
            dataType: "json"
            }).done();
         
      }, 
      
      colorDrawPixel:function(pixel, color) {
         this.c2d.fillStyle = pixel.getShownColor();
         this.c2d.fillRect(pixel.xPos, pixel.yPos, this.pixelSize, this.pixelSize);
         
         this.c2d.fillStyle = color;
         this.c2d.fillRect(pixel.xPos, pixel.yPos, this.pixelSize, this.pixelSize);
      },

      clearGrid: function() {
         for(var y = 0; y < this.numPixelsY; y++) {
            for(var x = 0; x < this.numPixelsX; x++) {
               this.pixels[x+y*this.numPixelsY].color = 'rgb(0,0,0)';
            }
         }
         this.renderPixels();
      },

      colorAllPixels: function(color) {
         console.log("matrix fill!");
         for(var y = 0; y < this.numPixelsY; y++) {
            for(var x = 0; x < this.numPixelsX; x++) {
               this.pixels[x+y*this.numPixelsY].color = color;
            }
         }
         this.renderPixels();
      }
   };
   
   // Init pixel grid animation
   pixelGrid.init();
   
});