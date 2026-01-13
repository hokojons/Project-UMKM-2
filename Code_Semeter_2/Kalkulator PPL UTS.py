from abc import ABC, abstractmethod

# Step 1: Interface
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> float:
        pass

# Step 2: Strategy Implementations
class AddOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a + b

class SubtractOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a - b

class MultiplyOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a * b

class DivideOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Tidak bisa dibagi dengan nol!")
        return a / b

# Step 3: Calculator Context
class Calculator:
    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy

    def calculate(self, a: int, b: int) -> float:
        return self.strategy.execute(a, b)

# Step 4: User Input
def main():
    print("=== Kalkulator Sederhana ===")
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))

        print("\nPilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            strategy = AddOperation()
        elif pilihan == "2":
            strategy = SubtractOperation()
        elif pilihan == "3":
            strategy = MultiplyOperation()
        elif pilihan == "4":
            strategy = DivideOperation()
        else:
            print("Pilihan tidak valid.")
            return

        calculator = Calculator(strategy)
        hasil = calculator.calculate(a, b)
        print(f"Hasil: {hasil}")

    except ValueError as e:
        print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    main()
