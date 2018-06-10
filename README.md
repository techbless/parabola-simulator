# Ball-In-Gravity-Trailing

## Status

[![Travis](https://img.shields.io/jenkins/s/https/jenkins.qa.ubuntu.com/view/Precise/view/All%20Precise/job/precise-desktop-amd64_default.svg)]() [![apm](https://img.shields.io/apm/l/vim-mode.svg)]()


## What you need before starting

  * Python3
  * Matplotlib
  * Numpy
  * Virtual Environment(recommended)
  
  
## How to run

    1. clone the repository into your desktop.
	2. make a python vertual environment.
	3. get into the vertualenv
	4. import ball_physics.py in the code where you will use ball_physics function.
	5. use the function such as "draw(args)"
  
  * The availiable function list is below.
  
  
## How to Import API
  * Use Below Code
   ```python
    import ball_physics as bp
   ```
   
## Availiable Function

  #### `draw(args)`
  
  * args should be passed to draw() as tuple
  * example below
  
  ```python
    args = (10, 10, 10, 5, 5, 80, 9.8)
    draw(args)
  ```
    
	args[0] : initial position of X
	args[1] : initial position of Y
	args[2] : initial position of Z
	args[3] : initial velocity of X
	args[4] : initial velocity of Y
	args[5] : initial velocity of Z
	args[6] : acceleration of gravity
  
  
  #### `where(args)`
  
  * args should be passed to draw() as tuple
  * example below
  
  ```python
    args = (10, 10, 10, 5, 5, 80, 9.8, 20)
    where(args)
  ```
  
	args[0] : initial position of X
	args[1] : initial position of Y
	args[2] : initial position of Z
	args[3] : initial velocity of X
	args[4] : initial velocity of Y
	args[5] : initial velocity of Z
	args[6] : acceleration of gravity
	args[7] : time that you want to know position and velocity after the ball have been thrown
	
## Example

  #### draw 5 5 5 10 15 80 9.8
  
  	init X: 5, init Y: 5, init Z: 5
	int VX: 10, init VY: 15, initVZ:80
	acceleration of gravity: 9.8
	
  ![example/draw](https://github.com/Yunbin-Chang/Ball-In-Gravity-Trailing/blob/master/example/draw.PNG)
  
  #### where 5 5 5 10 15 80 9.8 10
  
  	init X: 5, init Y: 5, init Z: 5
	int VX: 10, init VY: 15, initVZ:80
	acceleration of gravity: 9.8
  	time after a ball has been thrown: 10.
	
  ![example/where](https://github.com/Yunbin-Chang/Ball-In-Gravity-Trailing/blob/master/example/where.PNG)

## Should Notice Before Use

	From Chris Yunbin Chang as one of the developer of this program, saying that This program never guarantee any errorneous, mis-working, anything that can ouccur while using this program.

## License

   	MIT License

	Copyright (c) 2018 Chris Yunbin Chang

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.

