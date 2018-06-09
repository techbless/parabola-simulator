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
    draw(args)
  ```
  
	args[0] : initial position of X
	args[1] : initial position of Y
	args[2] : initial position of Z
	args[3] : initial velocity of X
	args[4] : initial velocity of Y
	args[5] : initial velocity of Z
	args[6] : acceleration of gravity
	args[7] : time that you want to know position and velocity after the ball have been thrown
