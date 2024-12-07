'''
Применим метод Монте-Карло, чтобы вычислить приближенное значение числа π.
'''

import torch
from math import pi
import matplotlib.pyplot as plt 

n_point = 100
points = torch.rand((n_point, 2)) * 2 - 1

n_point_circle = 0 
points_circle = []

for point in points:
	r = torch.sqrt(point[0]**2 + point[1]**2)
	if r <= 1:
		points_circle.append(point)
		n_point_circle += 1

points_circle = torch.stack(points_circle)

plt.plot(points[:,0].numpy(), points[:,1].numpy(), 'y.')
plt.plot(points_circle[:,0].numpy(), points_circle[:,1].numpy(), 'c.')

i = torch.linspace(0, 2*pi, n_point)
plt.plot(torch.cos(i).numpy(), torch.sin(i).numpy())
# plt.axes().set_aspect('equal')

pi_estimated = 4 * (n_point_circle / n_point)
# print(f'pi = {pi_estimated}')
plt.title(f'π = {pi_estimated}, n_points = {n_point}')
plt.show()

def estimate_pi_mc(n_iteration):
	n_point_circle = 0
	pi_iteratiion = []
	for i in range(1, n_iteration + 1):
		point = torch.rand(2) * 2 - 1
		r = torch.sqrt(point[0]**2 + point[1]**2)
		if r <= 1:
			n_point_circle += 1
		pi_iteratiion.append(4 * (n_point_circle / i))
	plt.plot(pi_iteratiion)
	plt.plot([pi] * n_iteration, '--')
	plt.xlabel('итерация')
	plt.ylabel('оценка π')
	plt.title(f'история оценивания: π = {pi_iteratiion[-1]}')
	plt.grid()
	plt.show()

estimate_pi_mc(10_000)