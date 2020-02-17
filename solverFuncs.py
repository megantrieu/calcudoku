def check_row(row):
   for j in range(len(row)):
      check = row[j]
      for i in range(len(row)):
         if check == row[i]:
            if i == j:
              pass
            elif check == 0 and row[i] ==0:
              pass
            else:
               return False
   return True

def check_rows_valid(puzzle):
   for each_list in puzzle:
     if check_row(each_list) == False:
       return False
   return True

def check_columns_valid(puzzle):
   check_list = []
   for j in range(len(puzzle)):
     for i in range(len(puzzle)):
        check_list.append(puzzle[i][j])
     if check_row(check_list) == True:
       check_list = []
     else:   
        return False
   return True

def get_cages():
   num_cages = int(input("Number of cages: "))
   cages = []
   for i in range(num_cages):
      add_cage = input("Cage number " + str(i)+": ").split()
      add_cage = [int(a) for a in add_cage] 
      cages.append(add_cage)
   return cages

def check_cage(puzzle, cage):
   cage_sum = cage[0]
   check_sum = 0
   nums = cage[2:]
   hasZero = False
   for v in range(len(nums)):
      check_sum += puzzle[int(nums[v])//5][int(nums[v])%5]
      if puzzle[int(nums[v])//5][int(nums[v])%5] == 0:
         hasZero = True
   if hasZero == False and check_sum != int(cage_sum):
     return False
   elif hasZero == True and check_sum >= int(cage_sum):
     return False
   else: 
     return True 
     

def check_cages_valid(puzzle, cages):
   for cage in cages:
      if check_cage(puzzle,cage) == False:
         return False
   return True
        

def check_valid(puzzle, cages):
   if check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle,cages) == True:
      return True
   else:
      return False
