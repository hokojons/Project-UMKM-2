from abc import ABC, abstractmethod
from typing import List

# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None:
        pass

# Kelas Subject
class TemperatureSensor:
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._max_temp = float('-inf')
        self._min_temp = float('inf')
        self._total_temp = 0.0
        self._num_readings = 0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
        
        # Update statistics
        if temperature > self._max_temp:
            self._max_temp = temperature
        if temperature < self._min_temp:
            self._min_temp = temperature
        self._total_temp += temperature
        self._num_readings += 1
        
        self.notify_observers()

    def get_temperature(self) -> float:
        return self._temperature

    def get_max_temp(self) -> float:
        return self._max_temp

    def get_min_temp(self) -> float:
        return self._min_temp

    def get_avg_temp(self) -> float:
        return self._total_temp / self._num_readings if self._num_readings > 0 else 0.0

# Current Conditions Display
class CurrentConditionsDisplay(Observer):
    def __init__(self, sensor: TemperatureSensor):
        self._sensor = sensor
        sensor.register_observer(self)

    def update(self, temperature: float) -> None:
        print(f"\nCurrent Conditions Display:")
        print(f"Current temperature: {temperature:.1f}°C")

# Statistics Display
class StatisticsDisplay(Observer):
    def __init__(self, sensor: TemperatureSensor):
        self._sensor = sensor
        sensor.register_observer(self)

    def update(self, temperature: float) -> None:
        print(f"\nStatistics Display:")
        print(f"Average temperature: {self._sensor.get_avg_temp():.1f}°C")
        print(f"Maximum temperature: {self._sensor.get_max_temp():.1f}°C")
        print(f"Minimum temperature: {self._sensor.get_min_temp():.1f}°C")

# Demo penggunaan sistem
def main():
    # Buat sensor suhu
    sensor = TemperatureSensor()

    # Buat dan daftarkan display
    current_display = CurrentConditionsDisplay(sensor)
    stats_display = StatisticsDisplay(sensor)

    print("Sistem Pemantau Suhu")
    print("--------------------")
    
    # Simulasi input suhu dari pengguna
    while True:
        try:
            input_str = input("\nMasukkan suhu (angka) atau 'q' untuk keluar: ")
            if input_str.lower() == 'q':
                break
            
            temperature = float(input_str)
            sensor.set_temperature(temperature)
            
        except ValueError:
            print("Input tidak valid. Masukkan angka atau 'q' untuk keluar.")

if __name__ == "__main__":
    main()