with open("Day 24/input.txt", newline="") as file:
    hailstones = file.read().splitlines()

hailstones = [[list(map(int, hailstone.split(" @ ")[0].split(", "))), list(map(int,hailstone.split(" @ ")[1].split(", ")))] for hailstone in hailstones]

BOUNDS = [200000000000000, 400000000000000]

def intersect(x0a,y0a,dxa,dya,x0b,y0b,dxb,dyb):
    d = (dxa*dyb-dxb*dya)
    if d == 0:
        return None
    t = (dyb*(x0b-x0a)-dxb*(y0b-y0a))/d
    point = (x0a+dxa*t,y0a+dya*t)
    if ((point[0] < x0a and dxa > 0) or (point[1] < y0a and dya > 0) or
        (point[0] > x0a and dxa < 0) or (point[1] > y0a and dya < 0) or
        (point[0] < x0b and dxb > 0) or (point[1] < y0b and dyb > 0) or
        (point[0] > x0b and dxb < 0) or (point[1] > y0b and dyb < 0)
        ):
        return None
    return point

number_of_intersections = 0
for idx, hailstone_A in enumerate(hailstones):
    for hailstone_B in hailstones[idx+1:]:
        intersect_location = intersect(hailstone_A[0][0], hailstone_A[0][1], hailstone_A[1][0], hailstone_A[1][1],
                  hailstone_B[0][0], hailstone_B[0][1], hailstone_B[1][0], hailstone_B[1][1],
                  )
        if intersect_location is None:
            continue
        if BOUNDS[0] <= intersect_location[0] <= BOUNDS[1] and BOUNDS[0] <= intersect_location[1] <= BOUNDS[1]:
            number_of_intersections +=1
print(number_of_intersections)

# part two
def system_of_equations(vars):
    x,y,z,dx,dy,dz=vars[:6]
    times = vars[6:]
    equations = []
    for hailstone, time in zip(hailstones, times):
        equations += [x-hailstone[0][0] + dx*time-hailstone[1][0]*time,
             y-hailstone[0][1] +dy*time-hailstone[1][1]*time,
             z-hailstone[0][2] +dz*time-hailstone[1][2]*time,
     ] 
    return equations

def jacobian_of_equations(vars):
    x,y,z,dx,dy,dz=vars[:6]
    times = vars[6:]
    equations = []
    for time_idx, hailstone in enumerate(hailstones):
        equations +=[
            [1,0,0,times[time_idx], 0, 0, *[0]*len(hailstones[:time_idx]), dx-hailstone[1][0], *[0]*len(hailstones[time_idx+1:])],
            [0,1,0,0, times[time_idx], 0, *[0]*len(hailstones[:time_idx]), dy-hailstone[1][1], *[0]*len(hailstones[time_idx+1:])],
            [0,0,1,0, 0, times[time_idx], *[0]*len(hailstones[:time_idx]), dz-hailstone[1][2], *[0]*len(hailstones[time_idx+1:])]
        ]
    return equations

import numpy as np
from scipy.optimize import least_squares, root
n_hailstones_to_use = min(len(hailstones),10)
hailstones=hailstones[:n_hailstones_to_use]

x0 = np.array((0.0,0.0,0.0,0.0,0.0,0.0, *[1.0]*n_hailstones_to_use))
x0 = x0.astype(np.float64)

sol = least_squares(system_of_equations, x0, bounds=([*[-np.inf]*6, *[0]*n_hailstones_to_use],np.inf), 
                    gtol=1e-15, jac=jacobian_of_equations, ftol=1e-13)
print(sol)
print(sol.x)
print(sol.x[0]+sol.x[1]+sol.x[2])


# let's try the sympy way too (solution above only started working after I built the sympy solution)
import sympy
from sympy import symbols

hailstones = hailstones[:10]
x,y,z,dx,dy,dz=symbols("x,y,z,dx,dy,dz", integer=True)

times = [symbols(f"t{i}",positive=True) for i in range(len(hailstones))]
equations = []
for hailstone, time in zip(hailstones, times):
    equations += [x-hailstone[0][0] + dx*time-hailstone[1][0]*time,
            y-hailstone[0][1] +dy*time-hailstone[1][1]*time,
            z-hailstone[0][2] +dz*time-hailstone[1][2]*time,
    ] 

solution = sympy.solve(equations, dict=True)[0]
print(solution.keys())
print(solution[x] + solution[y] + solution[z])





