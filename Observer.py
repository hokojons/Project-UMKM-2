from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None:
        pass

class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float) -> None:
        print(f"\n[Display Saat Ini] Suhu terkini: {temperature:.1f}°C")

class StatisticsDisplay(Observer):
    def __init__(self):
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
        self.total_temp = 0.0
        self.num_readings = 0

    def update(self, temperature: float) -> None:
        # Update statistik
        self.max_temp = max(self.max_temp, temperature)
        self.min_temp = min(self.min_temp, temperature)
        self.total_temp += temperature
        self.num_readings += 1
        
        # Hitung rata-rata
        avg_temp = self.total_temp / self.num_readings if self.num_readings > 0 else 0.0
        
        # Tampilkan statistik
        print("\n[Display Statistik]")
        print(f"Rata-rata: {avg_temp:.1f}°C")
        print(f"Maksimum: {self.max_temp:.1f}°C") 
        print(f"Minimum: {self.min_temp:.1f}°C")