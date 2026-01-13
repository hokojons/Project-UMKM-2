from typing import List
from Observer import Observer

class TemperatureSensor:
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0

    def register_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
        self.notify_observers()