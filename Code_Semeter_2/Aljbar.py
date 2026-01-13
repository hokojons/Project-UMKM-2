def input_matrix():
    """Fungsi untuk memasukkan matriks dari pengguna"""
    n = int(input("Masukkan jumlah variabel: "))
    print("\nFormat persamaan: a1 a2 a3 ... b")
    print("Contoh: 2x + 3y - z = 5 → masukkan: 2 3 -1 5\n")
    
    matrix = []
    for i in range(n):
        while True:
            try:
                row = input(f"Masukkan koefisien persamaan ke-{i+1}: ").split()
                row = [float(x) for x in row]
                if len(row) != n + 1:
                    print(f"Error: Harus memasukkan {n} koefisien dan 1 hasil")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Masukkan angka yang valid")
    return matrix

def print_matrix(matrix, decimals=2):
    """Fungsi untuk mencetak matriks"""
    for row in matrix:
        print("[", end="")
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print(" |", end="")  # Garis pemisah untuk augmented matrix
            print(f" {num:.{decimals}f}", end="")
        print(" ]")

def gaussian_elimination(matrix):
    """Fungsi untuk melakukan eliminasi Gauss""" 
    n = len(matrix)
    
    print("\nMatriks awal:")
    print_matrix(matrix)
    
    for col in range(n):
        # Pivoting: cari baris dengan nilai absolut terbesar di kolom saat ini
        max_row = col
        for row in range(col + 1, n):
            if abs(matrix[row][col]) > abs(matrix[max_row][col]):
                max_row = row
        
        # Tukar baris jika diperlukan
        if max_row != col:
            matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
            print(f"\nPertukaran baris {col+1} dengan baris {max_row+1}:")
            print_matrix(matrix)
        
        # Eliminasi untuk membuat elemen di bawah pivot menjadi 0
        for row in range(col + 1, n):
            if matrix[col][col] == 0:
                continue
            
            factor = matrix[row][col] / matrix[col][col]
            for c in range(col, n + 1):
                matrix[row][c] -= factor * matrix[col][c]
            
            print(f"\nEliminasi baris {row+1} dengan faktor {factor:.2f}:")
            print_matrix(matrix)
    
    # Cek solusi
    for row in range(n):
        all_zero = True
        for col in range(n):
            if abs(matrix[row][col]) > 1e-10:  # Tolerance untuk floating point
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
    solutions = gaussian_elimination(matrix)
    
    if solutions is not None:   
        variables = ['x', 'y', 'z', 'w', 'v'][:len(solutions)]
        
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