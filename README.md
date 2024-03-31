# Prime-Numbers-Backend
Backend for prime numbers generation &amp; visualization project.  
Project's main purpose is to generate textures with prime numbers on it for our Roblox game.
## Contents  
* [Prerequisites](#prerequisites)
* [Prime numbers generation](#prime-numbers)
* [Texture generations](#texture-generation)
* [Python algorithm implementation & comparison module](#python-sieve)
* [Credits](#credits)  
## Prerequisites
Install the required pip packages with the following command:
``` pip install -r requirements.txt```
## Prime numbers  
The Sieve of Eratosthenes is used to generate prime numbers up to *n*, where *n* can be any number.   
The algorithm is implemented in C++ due to its speed in comparison to Python.  
The source code can be found in src/sieve.cpp. It returns a vector of unsigned lls which contain all the prime numbers up to n.  
The code is compiled using CMake and PyBind11 into a Python module for subsequent use in texture generation.
## Texture-generation
Texture generation is performed using the PyPillow module.  
Firstly, the process reads the target image for number placement. Then, it calls the pre-compiled C++ code to obtain a list of prime numbers.  
It transforms the list into a string and creates a new temp image with semi-transparent numbers of it.  
Finally, it merges these two layers into a new one and saves the result as './result_image.jpg' by default 

You can customize the font, save and source pathes in image_generation.py.  
To run the code, simply cd into the repository and run ```python src/image_generation.py```.
## Python sieve
To evaluate the time saved by using the C++ implementation, we also implemented the Sieve of Eratosthenes in Python.  

Additionally, a module that compares the C++ and Python implementations has been developed. Run ```python src/comparison.py``` and it will show you Matplotlib comparison graph.
## Credits:  
[Nerd Fonts Cascadia Code Font](https://www.nerdfonts.com/font-downloads)
