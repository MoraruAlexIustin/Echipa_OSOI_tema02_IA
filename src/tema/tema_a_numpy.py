import numpy as np
import time

np.random.seed(149)

if __name__=="__main__":
    # --- Crearea array-urilor ---
    print("=== A.1 ===")

    A = np.random.randint(1, 11, size=(4, 3))
    B = np.random.randint(1, 11, size=(3, 5))
    print(f"A:\n {A}")
    print(f"B:\n{B}")

    print("=== A.2 ===")

    C=A@B
    print(f"C:\n{C}")

    print("=== A.3 ===")

    S=C.sum()
    print(f"Suma: {S}")

    print(f"Medie coloane: {C.mean(axis=0)}")

    Maxim=C.max()
    print(f"Maxim: {Maxim}")

    print("=== A.4(bonus) ===")

    M = np.random.randint(1, 10, size=(3, 3))
    I = np.linalg.inv(M)
    print(f"Inversa:\n{I}")
    D = np.linalg.det(M)
    print(f"Determinant:\n{D}")
    T = M@I
    ID = np.allclose(T,np.identity(3))
    print(f"Test: {ID}")
    