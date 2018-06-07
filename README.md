# ia1
codes for artificial intelligence 1 activities

see **ia1-descricao.pdf** [ptbr] 

# q1 - 8-puzzle game

I have implemented three algorithms to solve the eight puzzle. The input is self-explanatory: you give a state as a list of numbers from 0 to 8 separated by spaces. Anything away from this will give an error.

A list like 1 2 3 4 5 6 7 0 8 have the following representation:
    
    1 2 3
    4 5 6
    7 0 8

Example of a working input:
```/usr/bin/python3.6 /data/Documents/UFAL/repos/ia1/q1/main.py
---------- 8-PUZZLE GAME ----------
Type 'exit' to get out.
> 1 2 3 4 5 6 7 0 8
---------- 8-PUZZLE GAME: running ----------
[info] initial state:  [1, 2, 3, 4, 5, 6, 7, 0, 8]
[info] final state  :  [1, 2, 3, 4, 5, 6, 7, 8, 0]
[info] bfs running...
[info] it can be solved, try it!
[ bfs ] a solution was found!
[ bfs ] total of iterations:  1
[ bfs ] depth of solution:  1
[ bfs ] tempo total:  0.0001704692840576172
[info] dfs running...
[info] it can be solved, try it!
[ dfs ] a solution was found!
[ dfs ] total of iterations:  1
[ dfs ] depth of solution:  1
[ dfs ] total time:  0.00015854835510253906
[info] iddfs running...
[info] it can be solved, try it!
[iddfs] used limit:  10000
[iddfs] growth rate:  1000
[iddfs] depth of solution:  1
[iddfs] a solution was found!
[iddfs] total time:  0.00019407272338867188
> 
```

- If your input have odd permutations, the program will tell that it cannot be solved.
- If your input have lots of permutations (a even number, ok), then probably it will take a lot of time to be solved--depending on the nature of these permutations.
- The dfs algorithm will be the slowest, always.
- The iddfs is ineficient because I didn't save the states already covered...
- I used threads so that I could solve the problem with each algorithm 'simultaneously' without the need to wait another to complete.


# q2e3 - inference engine with backward and forward chaiing + explanation 'tree'
  
I have implemented the inference methods backward and forward chaining to solve from user rules input, as I exemplify below with backward chaining:
 
```
/usr/bin/python3.6 /data/Documents/UFAL/repos/ia1/q2e3/main.py
Type 'yes' below if you want to tell your own rules (or 'no' for file as input).
> no
Type the file name below, please. Verify that it is in the same folder as this script.
> rules_base_06
Rules and facts loaded!
>>> RULES <<<
	
        1: IF d AND a AND nao_tem
           THEN z
	
        2: IF x AND nao_tem AND y AND e
           THEN w
	
        3: IF z AND w
           THEN goal
	
        4: IF z AND w AND i
           THEN goal
	
        5: IF f
           THEN v
	
        6: IF v AND g
           THEN u
	
        7: IF c AND b AND u
           THEN y
	
        8: IF a AND f AND c AND d AND b
           THEN x
	
        9: IF q AND p
           THEN m
	
        10: IF d AND a
           THEN z
	
        11: IF x AND e AND h AND y
           THEN w


>>> FACTS <<<


	a
	b
	c
	d
	e
	f
	g
	h
	i





    Type now which strategy do you want (type 1 or 2): 
        1. Forward chaining
        2. Backward chaining
        3. Other (not implemented)
    
> 2

        Type now what you want to prove (with the given database).
        
        Ex.: 'will_rain' or 'temperature_less_than_20'
        
        Anything like that, named as variable. 
        
>goal
Running now backward chaining on "goal"...
Based on the existing database, we have goal = True.
Type 'yes' if you want to see the explanation ('no' otherwise).
> yes


goal: 
\_z 
| \________d 
| \________a 
\_w 
| \________y 
| | \_______________c 
| | \_______________b 
| | \_______________u 
| | | \______________________v 
| | | | \_____________________________f 
| | | \______________________g 
| \________x 
| | \_______________a 
| | \_______________f 
| | \_______________c 
| | \_______________d 
| | \_______________b 
| \________h 
| \________e 
Done.

Process finished with exit code 0
```

- Unfortunately, I didn't implement an editor to modify the rules given. To do that the user has to modify manually the file used as input.
- My explanation module is a crude one, but gets the job done for goals proved TRUE.

# recommender system -- not ok

A tried to replicate the following work: [A Fuzzy Logic Based Personalized Recommender System](https://ijcsits.org/papers/vol2no52012/22vol2no5.pdf), but couldn't get the database nor confirm if I really could replicate--I couldn't use my inference engine from last question **q2e3**. I spent a reasonable amount of time trying to get this one off the paper, but without success.
