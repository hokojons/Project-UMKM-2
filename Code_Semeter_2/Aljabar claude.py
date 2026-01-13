def input_matrix():
    n = int(input("Jumlah Baris: "))
    print("\n Format: a1 a2 a3 ... b")
    print(" Contoh: 1x + 2y + 3z = 4 → masukkan: 1 2 3 4\n")
    
    matriks = []
    for i in range(n):
        while True:
            try:
                row = input(f"Masukkan koefisien persamaan ke-{i+1}: ").split()
                row = [float(x) for x in row]
                if len(row) != n + 1:
                    print(f"Error: Harus memasukkan {n} koefisien dan 1 hasil")
                    continue
                matriks.append(row)
                break
            except ValueError:
                print("Error: Masukkan harus berupa angka")
    return matriks

def print_matrix(matrix, decimals=2):
    """Fungsi untuk mencetak matriks dengan format yang rapi"""
    for row in matrix:
        print("[", end="")
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print(" |", end="")  # Pemisah untuk augmented matrix
            print(f" {num:.{decimals}f}", end="")
        print(" ]")

def elimination(matrix):
    n = len(matrix)
    
    print("\nMatriks awal:")
    print_matrix(matrix)
    
    # Forward elimination
    for col in range(n):
        # Pivoting: cari baris dengan nilai absolut terbesar
        max_row = col
        for row in range(col + 1, n):
            if abs(matrix[row][col]) > abs(matrix[max_row][col]):
                max_row = row
        
        # Tukar baris jika diperlukan
        if max_row != col:
            matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
            print(f"\nPertukaran baris {col + 1} dengan baris {max_row + 1}:")
            print_matrix(matrix)
        
        # Eliminasi untuk membuat elemen di bawah pivot = 0
        for row in range(col + 1, n):
            if abs(matrix[col][col]) < 1e-10:  # Cek pivot hampir nol
                continue
            
            factor = matrix[row][col] / matrix[col][col]
            for c in range(col, n + 1):
                matrix[row][c] -= factor * matrix[col][c]
            
            if abs(factor) > 1e-10:  # Hanya tampilkan jika faktor signifikan
                print(f"\nEliminasi baris {row + 1} dengan faktor {factor:.2f}:")
                print_matrix(matrix)
    
    # Cek konsistensi sistem
    for row in range(n):
        all_zero = True
        for col in range(n):
            if abs(matrix[row][col]) > 1e-10:
                all_zero = False
                break
        
        if all_zero and abs(matrix[row][n]) > 1e-10:
            print("\nSistem tidak memiliki solusi (inconsistent)")
            return None
        elif all_zero:
            print("\nSistem memiliki banyak solusi (infinite solutions)")
            return None
    
    # Back substitution
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
        variables = ['x', 'y', 'z', 'w', 'v'][:len(solutions)]
        
        print("\nSolusi sistem persamaan:")
        for var, val in zip(variables, solutions):
            print(f"{var} = {val:.4f}")
        
        # Verifikasi solusi
        print("\nVerifikasi:")
        original_matrix = matrix  # Matrix sudah dimodifikasi, tapi untuk verifikasi masih bisa digunakan
        for i in range(len(solutions)):
            lhs = sum(matrix[i][j] * solutions[j] for j in range(len(solutions)))
            rhs = matrix[i][len(solutions)]
            status = '✓' if abs(lhs - rhs) < 1e-6 else '✗'
            print(f"Persamaan {i+1}: {lhs:.4f} = {rhs:.4f} {status}")

if __name__ == "__main__":
    main()