# Problem
[Manual], (button_wiring), {joltage} 
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}


1. Starting point is all [.....]
2. (3) => (...#)
3. press as few buttons as possible to get to manual
4. buttons can be pressed multiple times 



# Try 1

1. clean every part from the input into a binary number

2. get the manual and search for the nearest binary number from the button_wirings => start with that
3. add/ substract further button_wirings to get closer and closer to the manual number

## Result 
Searched = 0110
wiring = 0001 , 1001, 0010, 0011, 1010, 1100

Doesnt work!
Nearest nummber to 0110 is 0010.
with this it leads to 4 button presses:
0010 -1100> 1110 -0001> 1111 -1001> 0110

But the best option woul be
1010 -1100> 0110 
only two button presses



# Try 2
Bruteforce it
1. look if there is a direct wiring representing the manual
2. if not try out every possibility if two together represent the manual
3. if not try out every possibility if 3 toghether represent the manual (options explode because the same button_wiring can be prest multiple times)
.....


# Try 3
Create sorted sets. The symetric diffrence between set A and B has to be the manual
set A = 1100
set B = 1010

set c = symmetric diffrence = 0110

this works if there are only two sets

for three sets and more it doesnt
set A = 1101
set B = 1010
set C = 1001

symmetric diffrence = 0110
but the result with on of princaple would lead to: 1110

does steps help?

symmetric diffrence A and B => set X = 0111
symmetric diffrence X and C => set Y = 1110

that would work!

## Rules
1. pressing something twice canels it out
set A = 1101
set B = 1010
set C = 1001

1. Set A
2. Set B
3. Set C
4. Set A

1101 - 1010 -> 0111 - 1001 -> 1110 - 1101 -> 0011

Results is the same as just pressing
2. Set B
3. Set C

1010 - 1001 -> 0011

So all even pressed buttons can be ignored


# Try 3.1 
Its like fibbonacy sequence
and if i safe the steps i can view them all
problem there are still many possibilities looping through them  is slow


Saving masks as i go

create a struct:
presses : masks[]
0 : [0000]
1 : [1101, 1010, 1001 ]
2 : [0111, 0100, 0011 (rest is repetative)]
3 : ....


With diffrent options come diffren possabilities

---

# Part 2

[Manual], (button_wiring), {joltage} 
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}


1. find how to reach joltage with the fewest button presses
2. button tells index where to add + 1 -> (3) => (0,0,0,1)
3. press as few buttons as possible to get to joltage
4. buttons can be pressed multiple times 

like part one build every possibility.

This will get to big to brute force

## Rules
Add more rules if any of the joltage params gets higher then the jolate we are searching it can be deleted.
{1, 1} -> {2, 1} (Not possible to go down)

Add rules if on param can only be increased by one button. it has to be presst the exact amount of times of the pra value:
(0) (1,2) (0,2) (2) {0,3,x} -> joltage[1] can only be increased by pressing the second button.
(1,2) * 3 = {0,3,3} can then be used as startung possition skipping all other option up to button press 3

(Could also happen for multiple joltage params.)

## Implementation
use set to search for already existing joltage options (sets are efficient) store all states ever reached and check them.

Two options:
Either build up to the searched joltage (start from: {0,0,0,0} add untill {x,x,x,x} is reached)
Or start with the searched and reach {0,0,0,0} subbstracting every option

if searched is found the button presses can be added to the total sum and the loop can be broken to go to the next line



## Try 2
building a knoadge piramyd

starting states : 1100, 0001, 0011
1101: 1100, 0001
1111: 1100, 0011
0012: 0001, 0011
.......

Too big


## Try 3
make lists per button press

unique states:
1: (001, 010, 100)
2: (011, 101, 110, 002, 020, 200)
....
....
....



## Try 4
DONT BRUTE Force

Math: 
buttons

vec_button_1*c + vex_button_2*c + ....... + vec_button_n*c = vec_searched 


Example:

line: [ignored], (0,1), (1,0), (1,1) {7,3}

searched Vector: searched(7,3)
Button Vector: a(0,1), b(1,0), x(1,1)


equation: a*cn + b*cn + x*cn = searched


c has to be a possitiv int for each vector
searched it the lowest possible sum of (c1...cn) 


## Find solution
1. Linear Combination
2. Weighted Sum (Weighted Average)
3. Knapsack Problem / Subset Sum

## Best: system of linear equations or a linear inverse problem
How? i dont know


