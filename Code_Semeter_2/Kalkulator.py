from abc import ABC, abstractmethod

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> float:
        pass

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
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

class CalculatorContext:
    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy
    
    def calculate(self, a: int, b: int) -> float: 
        return self.strategy.execute(a, b)

def main():
    while True:
        print("\n=== Kalkulator ===")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (X)")
        print("4. Bagi (/)")
        print("5. Keluar")
        
        try:
            pilihan = input("Masukan Pilihan (1/2/3/4/5): ")

            if pilihan == "5":
                print("Terima kasih telah menggunakan kalkulator!")
                break

            if pilihan not in ("1", "2", "3", "4"):
                print("Pilihan tidak valid, silakan coba lagi")
                continue

            a = float(input("Masukan angka pertama: "))
            b = float(input("Masukan angka kedua: "))

            if pilihan == "1":
                strategy = AddOperation()
            elif pilihan == "2":
                strategy = SubtractOperation()
            elif pilihan == "3":
                strategy = MultiplyOperation()
            elif pilihan == "4":
                strategy = DivideOperation()

            calculator = CalculatorContext(strategy)
            hasil = calculator.calculate(a, b)
            print(f"Hasil: {hasil}")

        except ValueError:
            print("Error: Masukan harus berupa angka")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()