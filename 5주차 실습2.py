import numpy as np

#행렬 A와 B의정의
A = np.array([
    [1,0,2],
    [2,-1,3],
    [4,1,8]     

])

B = np.array([
    [-11, 2, 2],
    [-4, 0, 1],
    [6,-1,-1]
        ])

l = np.eye(3, dtype=int)

AB = A@B
BA = B@A

print("A = ")
print(A)
print("\nB = ")
print(B)
print("\nAB = ")
print(AB)
print("\nBA = ")
print(BA)

print("\nAB = l :", np.array_equal(AB, l))
print("BA = l :", np.array_equal(BA, l))

if np.array_equal(AB, l) and np.array_equal(BA, l):
    print("\nA와 B는 서로 역행렬이다.")
    print("즉, B = A^(-1)이고, A = B^(-1)이다.")

else:
    print("\nA와 B는 서로 역행렬이 아니다.")