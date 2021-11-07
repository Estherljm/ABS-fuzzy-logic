# Objective 
Design a model of an anti-lock braking system by using Mamdani fuzzy inference system and input parameters such as speed, distance, 
surface condition and slip ratio to predict the output which will be the brake force. 

# Parameters of proposed system 
![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/flowchart.png)

# Implementation 
1. Creation of membership functions of each input and output 
![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img1.png)

![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img2.png)

2. Create fuzzy rules (Total 24 rules) 

![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img5.png)

Example of the 24th rule 

![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img3.png)

3. Summarization of rules 

Applied to combine all the rules using maximum method or so called maximum
![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img4.png)

4. Defuzzification 

In this system, the mean of maxima is used such that when more than one is present, the average value of the maxima is calculated, and this finally becomes the defuzzied output. 

![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img6.png)

# Test Results
Example of a test case with these input parameters: 

![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img8.JPG)

Graph of the fuzzy ABS output 

![alt text](https://github.com/Estherljm/ABS-fuzzy-logic/blob/master/img7.png)

In such circumstances, the output of the fuzzy anti-lock braking system is 5.0. This means that a medium duration intermittent brake is performed by the anti-lock braking system where the
car stops and moves every 5 seconds until vehicle comes to a gradual stop allowing the avoidance of the obstacle ahead.
