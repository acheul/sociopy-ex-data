import sys
sys.path.append("../") # 상대경로일 경우, 파일의 위치가 아닌 런타임이 실행되는 위치 기준!
from demo_pack import *

if __name__=="__main__":
  print("2+3:", add(2, 3))
  print("3-2:", subtract(3, 2))
  print("100+1000:", add(figures.HUNDRED, figures.THOUSAND))