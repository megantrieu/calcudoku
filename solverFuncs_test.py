import unittest
import solverFuncs

class TestsProject3(unittest.TestCase):
   
   def test_check_valid_2(self):
      puzzle = [[1, 3, 2, 4, 5],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
      cages2 = [[5, 2, 0, 5],
               [3, 1, 1],
               [8, 3, 2, 3, 4]]
      self.assertFalse(solverFuncs.check_cages_valid(puzzle,cages2))

   def test_rows(self):
      clist = [1,2,3,4,5]
      self.assertTrue(solverFuncs.check_row(clist))

   def test_rows2(self):
      clist = [1,3,2,5,5]
      self.assertFalse(solverFuncs.check_row(clist))
 
   def test_all_rows(self):
      puzzle1 = [[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3],[1, 2, 4, 3, 5],[4, 3, 5, 2, 1]]
      self.assertTrue(solverFuncs.check_rows_valid(puzzle1))

   def test_all_rows2(self):
      puzzle1 = [[3, 5, 2, 1, 1], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3],[1, 2, 4, 3, 5],[4, 3, 5, 2, 1]]
      self.assertFalse(solverFuncs.check_rows_valid(puzzle1))

   def test_all_col(self):
     puzz = [[0,8,3,2,1],[1,5,6,2,4],[2,3,4,5,6],[3,7,9,2,4],[5,4,3,2,1]]
     self.assertFalse(solverFuncs.check_columns_valid(puzz))

   def test_all_col2(self):
     puzz = [[0,2,3,4,5],[0,4,5,1,3],[1,3,4,2,6]]
     self.assertTrue(solverFuncs.check_columns_valid(puzz))

   def test_all_col3(self):
     puzz = [[1,8,3,4,1],[1,5,6,2,4]]
     self.assertFalse(solverFuncs.check_columns_valid(puzz))

   def test_cages(self):
      puzzle1 = [[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3],[1, 2, 4, 3, 5],[4, 3, 5, 2, 1]]
      cages1 = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13], [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], [13, 4,12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
      self.assertTrue(solverFuncs.check_cages_valid(puzzle1,cages1))
   
   def test_valid(self):
      #fails the column test
      puzzle1 = [[3,5,2,1,4], [5,1,3,4,2],[2,4,1,5,3],[3,2,4,3,5],[4,3,5,2,1]]
      cages1 = [[9,3,0,5,6],[7,2,1,2],[10,3,3,8,13],[14,4,4,9,14,19],[3,1,7],[8,3,10,11,16],[13,4,12,17,21,22],[5,2,15,20],[6,3,18,23,24]]
      self.assertFalse(solverFuncs.check_valid(puzzle1, cages1))

   def test_check_cages_valid(self):
      puzzle = [[1, 2, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]]
      cages = [[7, 2, 0, 5],[3, 2, 1, 6],[7, 2, 2, 7],[8, 2, 3, 4],[9, 3, 10, 11, 12],[6, 2, 8, 13],[5, 2, 9, 14],[4, 2, 15, 16],[9, 2, 17, 18],[10, 3, 20, 21, 22],[7, 3, 19, 23, 24]]
      self.assertTrue(solverFuncs.check_cages_valid(puzzle, cages))
   
   def test_check_cages_valid1(self):
      puzzle = [[2, 1, 4, 3, 5],
                [7, 0, 3, 1, 4],
                [3, 4, 2, 5, 1],
                [1, 3, 5, 4, 2],
                [4, 5, 1, 2, 3]] 
   
      cages = [[7, 2, 0, 5],
               [3, 2, 1, 6],
               [7, 2, 2, 7],
               [8, 2, 3, 4],
               [9, 3, 10, 11, 12],
               [6, 2, 8, 13],
               [5, 2, 9, 14],
               [4, 2, 15, 16],
               [9, 2, 17, 18],
               [10, 3, 20, 21, 22],
               [7, 3, 19, 23, 24]]
             
      self.assertFalse(solverFuncs.check_cages_valid(puzzle, cages))
   
   def test_check_valid_2(self):
      puzzle = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

      cages = [[9,  3, 0,  5,  6],
               [7,  2, 1,  2],
               [10, 3, 3,  8,  13],
               [14, 4, 4,  9,  14, 19],
               [3,  1, 7],
               [8,  3, 10, 11, 16],
               [13, 4, 12, 17, 21, 22],
               [5,  2, 15, 20],
               [6,  3, 18, 23, 24]]

      self.assertTrue(solverFuncs.check_valid(puzzle, cages))

   def test_check_rows0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(solverFuncs.check_rows_valid(puzzle))
      
   def test_check_columns0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(solverFuncs.check_columns_valid(puzzle))
      
   def test_check_cages0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(solverFuncs.check_cages_valid(puzzle, cages))
      
   def test_check_valid0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(solverFuncs.check_valid(puzzle, cages))
      
  # def test_get_cages0(self):
  #    cages = [[5, 2, 0, 5],
  #             [3, 1, 1],
  #            [8, 3, 2, 3, 4]]
  #   self.assertEqual(cages, solverFuncs.get_cages())

  # def test_check_valid_2(self):
  #    puzzle = [[1, 3, 2, 4, 5],
  #              [0, 0, 0, 0, 0],
  #              [0, 0, 0, 0, 0],
  #              [0, 0, 0, 0, 0],
  #              [0, 0, 0, 0, 0]]
  #   cages2 = [[5, 2, 0, 5],
  #             [3, 1, 1],
  #             [8, 3, 2, 3, 4]]
  #    self.assertTrue(solverFuncs.check_cages_valid(puzzle,cages2))

if __name__ == '__main__':
   unittest.main()
