#!/usr/bin/env python3

import time, random, sys, argparse
import includes.colormaps as cm
import numpy as np
import glc

def f(x, y,alpha):
    return (
        np.sin(np.cos(alpha)*x-np.sin(alpha)*y)
        + np.cos(np.sin(alpha)*x+np.cos(alpha)*y)
        + np.sin(np.cos(2*alpha)*x+np.sin(alpha)*y)
        + np.cos(-np.sin(2*alpha)*x+np.cos(alpha)*y)
        +4)/8

def SineCosine(argv):
    parser = argparse.ArgumentParser(prog="SineCosine.py",
                        description='A spherical trigonometric rotation')
    parser.add_argument('-f','--framerate', default=.75, type=int, metavar='F',
                        help='framerate used in the animation ')    
    args = parser.parse_args(argv)
    x = np.linspace(0, 2 * np.pi, 8).reshape(-1, 1)
    y = np.linspace(0, 2 * np.pi, 8)
    alpha = 0;
    c = glc.InitOPC()
    img = np.zeros( (8,8,3) )
    while True:
        try: #break on keytsroke
            alpha = np.mod(alpha+np.pi/90,2*np.pi)
            img = np.round(cm.viridis(f(x, y, alpha))[:,:,0:3]*255);
            c.put_pixels(glc.image2pixels(img))
            time.sleep(1.0/args.framerate)
        except KeyboardInterrupt:
            glc.destOPC(c,img)
            break

if __name__ == "__main__":
        SineCosine(sys.argv[1:])
