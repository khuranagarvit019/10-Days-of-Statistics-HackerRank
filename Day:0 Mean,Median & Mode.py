# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

a = int(input())
l1 = list(map(int, input().split()))
print(np.mean(l1))
print(np.median(l1))
print(int(stats.mode(l1)[0]))
