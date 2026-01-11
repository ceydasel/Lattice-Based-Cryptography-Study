#Lattice Basis Visualizer
import numpy as np
import matplotlib.pyplot as plt
print("Enter two basis vectors (Example: [1, 2] and [3, 0]):")
x1 = int(input("x for v1: "))
y1 = int(input("y for v1: "))
v1 = np.array([x1, y1]) 
x2 = int(input("x for v2: "))
y2 = int(input("y for v2: "))
v2 = np.array([x2, y2])
M = np.array([v1, v2])
det = int(np.linalg.det(M))
print(f"Determinant (Area) of this Lattice: {det}")
norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)
print(f"length of v1: {norm_v1:.2f}")
print(f"length of v2: {norm_v2:.2f}")
print("[DRAWING] Calculating grid points...")
print("Orthogonalization")
u1 = v1
mu = np.dot(v2, u1) / np.dot(u1, u1)
u2 = v2 - (mu * u1)
print(f"orthogonal u1: {u1}")
print(f"orthogonal u2: {u2}")
print(f"Gram-Schmidt Coefficient(mu): {mu:.4f}")
dot_product = np.dot(u1, u2)
print(f"check orthogonality (u1.u2): {dot_product:.4f} (should be 0)")
for i in range(-5 , 6):
    for j in range(-5, 6):
        p = (i * v1) + (j * v2)
        plt.scatter(p[0], p[1], color = 'black', alpha = 0.5)
        print(p)
print("[ATTACK] Babai Algorithm is searching for a target...")
print("Turning a bad base into a good base")
v1_red = v1.copy()
v2_red = v2.copy()
loop_count = 0
while True:
    if np.linalg.norm(v2_red) < np.linalg.norm(v1_red):
        v1_red, v2_red = v2_red, v1_red
        print(f"A swap was done, the new one is:{v1_red} ")
    mu = np.dot(v2_red, v1_red) / np.dot(v1_red, v1_red)
    mu_rounded = round(mu)
    if mu_rounded == 0:
        break
    v2_red = v2_red - (mu_rounded * v1_red)
    print(f"reduction: v2 = v2 - {mu_rounded} * v1 -> new v2: {v2_red}")
    loop_count += 1
    if loop_count > 100: break
print(f"improved base: v1 = {v1_red}, v2 = {v2_red}")
target = np.array([5, 6])
plt.scatter(target[0], target[1], color = 'orange', marker ='x', s = 100, label = 'Target(t)')
coeffs = np.linalg.solve(M.T, target)
print(f"real coefficients: {coeffs}")
coeffs_rounded = np.round(coeffs).astype(int)
print(f"Rounded Integers: {coeffs_rounded}")
babai_point = (coeffs_rounded[0] * v1) + (coeffs_rounded[1] * v2)
plt.scatter(babai_point[0], babai_point[1], color = 'red', marker = '*', s =150, label = 'Babai prediction')
plt.arrow(0 ,0, v1[0], v1[1], color = 'red', length_includes_head=True, label = 'v1')
plt.arrow(0, 0, v2[0], v2[1], color = 'green', length_includes_head=True, label = 'v2')
plt.arrow(0, 0, u1[0], u1[1], color = 'blue', linestyle = '--', width = 0.02, label = 'GS u1')
plt.arrow(0, 0, u2[0], u2[1], color = 'blue', linestyle = '--', width = 0.02, label = 'GS u2')
plt.arrow(0, 0, v1_red[0], v1_red[1], color = 'yellow', width = 0.03, label = 'Reduced v1')
plt.arrow(0, 0, v2_red[0], v2_red[1], color = 'yellow', width = 0.03, label = 'Reduced v2')
plt.title(f"det: {det}, target: {target}, guess: {babai_point}")
plt.grid(True)
plt.legend()
plt.show()




        
        


 