import calculate
# from calculate import *
from calculate import HUNDRED, THOUSAND, add, subtract, print_name

if __name__=="__main__":

  print("2+3:", add(2, 3))
  print("3-2:", subtract(3, 2))
  print("100+1000:", add(HUNDRED, THOUSAND))

  print("type of calculate:", type(calculate))
  print_name()