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

I always start wit all of "0000"

1^2
2^2
3^2
4^2
but those include duplicates


for mask in masks:
    