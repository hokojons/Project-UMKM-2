from subject import TemperatureSensor
from Observer import CurrentConditionsDisplay, StatisticsDisplay

def main():
    # Inisialisasi sensor dan display
    sensor = TemperatureSensor()
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()
    
    # Daftarkan observer
    sensor.register_observer(current_display)
    sensor.register_observer(stats_display)
    
    print("=== SISTEM PEMANTAU SUHU ===")
    print("Masukkan suhu (angka) atau 'keluar' untuk berhenti")
    
    while True:
        user_input = input("\nInput suhu: ").strip().lower()
        
        if user_input == 'keluar':
            print("Program dihentikan")
            break
            
        try:
            temperature = float(user_input)
            sensor.set_temperature(temperature)
        except ValueError:
            print("Input tidak valid! Masukkan angka atau 'keluar'")

if __name__ == "__main__":
    main()