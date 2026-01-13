from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

class TemperatureSensor:
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def register_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Registered observer: {observer.__class__.__name__}")

    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Removed observer: {observer.__class__.__name__}")

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        self._temperature = temperature
        print(f"\nTemperature updated to: {temperature}°C")
        self.notify_observers()

class CurrentConditionsDisplay(Observer):
    def __init__(self, temperature_sensor: TemperatureSensor):
        self._temperature_sensor = temperature_sensor
        self._temperature_sensor.register_observer(self)
    
    def update(self, temperature: float):
        self.display(temperature)
    
    def display(self, temperature: float):
        print(f"[Current Conditions] Temperature: {temperature:.1f}°C")

class StatisticsDisplay(Observer):
    def __init__(self, temperature_sensor: TemperatureSensor):
        self._temperature_sensor = temperature_sensor
        self._temperatures = []
        self._temperature_sensor.register_observer(self)
    
    def update(self, temperature: float):
        self._temperatures.append(temperature)
        self.display()
    
    def display(self):
        if not self._temperatures:
            return
            
        avg = sum(self._temperatures) / len(self._temperatures)
        min_temp = min(self._temperatures)
        max_temp = max(self._temperatures)
        
        print("\n[Temperature Statistics]")
        print(f"Average: {avg:.1f}°C")
        print(f"Minimum: {min_temp:.1f}°C")
        print(f"Maximum: {max_temp:.1f}°C")
        print(f"Readings: {len(self._temperatures)}")

def main():
    # Create sensor
    sensor = TemperatureSensor()
    
    # Create displays
    current_display = CurrentConditionsDisplay(sensor)
    stats_display = StatisticsDisplay(sensor)
    
    print("Temperature Monitoring System")
    print("Enter temperatures (type 'exit' to quit, 'remove' to remove current display)")
    
    while True:
        user_input = input("\nEnter temperature (°C): ").strip().lower()
        
        if user_input == 'exit':
            print("Exiting system...")
            break
        elif user_input == 'remove':
            sensor.remove_observer(current_display)
            print("Current conditions display removed")
            continue
        
        try:
            temperature = float(user_input)
            sensor.set_temperature(temperature)
        except ValueError:
            print("Invalid input. Please enter a number or 'exit'")

if __name__ == "__main__":
    main()