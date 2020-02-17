# Project 3 - Calcudoku Solver
# 
# Name: Megan Trieu
# Instructor: Mork 

from solverFuncs import *

def main():
   cages = get_cages()
   puzz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
   backtrack = 0
   box = 0
   check = 0
   insert_num = 1
   while box < 25:
      if puzz[box//5][box%5] < 5:
         puzz[box//5][box%5] += 1
         check += 1
         if check_valid(puzz,cages) == True:
           box += 1
      elif puzz[box//5][box%5] == 5:
            puzz[box//5][box%5] = 0
            backtrack +=1
            box -=1

   puzz_print=[]
   cell = 0
   while cell < 25:
      puzz_print.append(puzz[cell//5][cell%5])
      cell += 1
 
   puzz_print = [str(j) for j in puzz_print]
   print("")
   print("---Solution---")
   print("")
   for val in range(5):
      print(" ".join(puzz_print[(val*5):((val+1)*5)])+" ")
  
   print("\nchecks:",check, "backtracks:", backtrack)

if __name__ == '__main__':
   main()
