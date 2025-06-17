# Damping by Dania Bressler and Angelina Lin

# Overview
Our code is a model of a musical string such as that of a violin. 
To model the string, we created a system of balls connected to each other by many springs.
The balls are modeled by spheres and the springs are modeled by cylinders. 
We show the movement of the string by calculating the forces that are applied on each spring due to the other springs and damping force, calculating the change in momentum due to the forces, and updating the position of the springs due to the momentum. 


# User inputs
The user first adjusts the three sliders (mass, tension, and pull distance) as they wish. 
The mass slider allows the user to change the mass of the entire string (mass of all of the spheres together). 
The tension slider allows the user to change the spring constant k of the spheres. 
The pull distance slider allows the user to change the distance that the string is pulled down when it is ”plucked.” Since the pull distance slider is automatically set to 0, the user must adjust the slider in order for the string to oscillate.
Once the user has made the adjustments they wish, they press start, which will initiate the plucking of the string
After the start button is pressed/the string is pushed, the string will oscillate back and forth on the violin. 
Beneath the model, two graphs will form: 
The first graph will graph a point representing the frequency vs tension of the string. 
The second graph will show the y-position vs time of two spheres on the string (blue center ball and orange fifth ball from the left).
The reset button allows the string to return to its original state. After the reset button is pushed, the point on the frequency vs tension graph will remain while the y-position vs time graph will clear. 
The benefit of having the frequency point remain is that repeating the program multiple times will allow for a graph with multiple points that show the relationship between frequency and tension.
Our string has a natural stretch length and a damping force that are properties of the string that cannot be altered by the user.
