__author__ = 'Xinyue'

from cvxpy import *
from bcd import bcd
import numpy as np

n = 4
m = 3
theta = Variable(n)
theta.value = np.ones((n,1))/float(n)
x = Variable(m)
x.value = np.ones((m,1))/float(m)
P = Variable(m,m)
P.value = np.ones((m,m))
P0 = []
P0.append(np.matrix([[0.2,0.7,0.1],[0.3,0.3,0.4],[0.1,0.8,0.1]]))
P0.append(np.matrix([[0.25,0.35,0.4],[0.1,0.1,0.8],[0.45,0.05,0.5]]))
P0.append(np.matrix([[0.1,0.25,0.65],[0.2,0.1,0.7],[0.3,0.3,0.4]]))
P0.append(np.matrix([[0.23,0.67,0.1],[0.01,0.24,0.75],[0.2,0.45,0.35]]))

x0 = [0.25,0.3,0.45]
cost = norm(x-x0)
constr = [theta >= 0, sum_entries(theta) == 1, x >= 0, sum_entries(x) == 1, P*x == x]
right = 0
for i in range(n):
    right += theta[i]*np.transpose(P0[i])
constr += [P == right]
prob = Problem(Minimize(cost), constr)
prob.solve(method = 'bcd',solver = 'SCS', rho = 1.2, proximal = 0, mu_max = 1e4)

print x.value
print theta.value