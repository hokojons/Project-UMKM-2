def input_matrix():
    n = int(input("Jumalah Baris "))
    print("\n Format 1 2 3 4 ")
    print("\n Contoh 1x 2y 3z = 4 " )
    
    matriks = []
    for i in range(n):
        while True:
            try:
                row = input(f"Masukan koefisien Perstama ke {i+1}: ").split()
                row = [float(i) for i in row]
                if len(row) != n + 1:
                    print(f"Error: Harus Memasukkan {n} Koefisien dan 1 hasil")
                    continue
                matriks.append(row)
                break
            except ValueError:
                print(f"Error: Masukan Harus Berupa Angka")
    return matriks

def print_matrix(matrix, decimals=2):
    for row in matrix:
        print("[", end="")
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print(" |", end="")  # ← Tambah spasi
            print(f" {num:.{decimals}f}", end="")  # ← Tambah spasi
        print(" ]")

def elimination(matrix):
    n = len(matrix)

    print("\nMatrix awal")
    print_matrix(matrix)

    for col in range(n):
        max_row = col 
        for row in range(col +1, n):
            if abs(matrix[row][col]) > abs(matrix[max_row][col]):
                max_row = row
        
        if max_row != col:
            matrix[col],matrix[max_row] = matrix[max_row], matrix[col]
            print(f"\nPertukaran Baris {col + 1} dengan baris {max_row + 1}:")
            print_matrix(matrix)
        
        for row in range(col + 1, n):
            if matrix[col][col] == 0:  # ← Checks pivot element
                continue

            factor = matrix[row][col] / matrix[col][col]
            for c in range(col, n + 1):
                matrix[row][c] -= factor * matrix[col][c]

            print(f"\nEliminasi baris {row+1} dengan faktor {factor:.2f}:")
            print_matrix(matrix)
    for row in range(n):
        all_zero = True
        for col in range(n):
            if abs(matrix[row][col]) > 1e-10: 
                all_zero = False
                break
        
        if all_zero and abs(matrix[row][n]) > 1e-10:
            print("\nSistem tidak memiliki solusi")
            return None
        elif all_zero:
            print("\nSistem memiliki banyak solusi")
            return None
    
    # Substitusi mundur
    solutions = [0] * n
    for row in reversed(range(n)):
        solutions[row] = matrix[row][n]
        for col in range(row + 1, n):
            solutions[row] -= matrix[row][col] * solutions[col]
        solutions[row] /= matrix[row][row]
    
    return solutions

def main():
    print("=== SOLVER SISTEM PERSAMAAN LINEAR ===")
    print("Metode Eliminasi Gauss (Tanpa Library Eksternal)\n")
    
    matrix = input_matrix()
    solutions = elimination(matrix)
    
    if solutions is not None:
        variables = ['x', 'y'   , 'z', 'w', 'v'][:len(solutions)]
        
        print("\nSolusi sistem persamaan:")
        for var, val in zip(variables, solutions):
            print(f"{var} = {val:.4f}")
        
        # Verifikasi
        print("\nVerifikasi:")
        for i in range(len(solutions)):
            lhs = 0
            for j in range(len(solutions)):
                lhs += matrix[i][j] * solutions[j]
            print(f"Persamaan {i+1}: {lhs:.4f} = {matrix[i][len(solutions)]:.4f} {'✓' if abs(lhs - matrix[i][len(solutions)]) < 1e-6 else '✗'}")

if __name__ == "__main__":
    main()  