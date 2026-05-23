try:
    from main import calculate_min_cable
except ImportError:
    try:
        from laba7course2 import calculate_min_cable
    except ImportError:
        exit()

def run_advanced_analysis():
    filename = 'communication_wells.csv'
    length = calculate_min_cable(filename)
    
    if length == -1 or isinstance(length, str):
        print("Аналіз неможливий: помилка у вхідних даних або мережа роз'єднана.")
        return

    price_per_meter = 210 
    total_cost = length * price_per_meter
    km_length = length / 1000
    
    if length < 1000:
        comparison = "Це менше за довжину одного футбольного поля."
    elif length < 5000:
        comparison = "Це приблизно як висота гори Монблан."
    else:
        comparison = "Це солідна відстань для міської інфраструктури."

    print(f"=== ДОДАТКОВЕ ЗАВДАННЯ: ЕКОНОМІЧНИЙ АНАЛІЗ ===")
    print(f"Аналіз файлу: {filename}")
    print("-" * 45)
    print(f"Загальна дистанція:   {length} м ({km_length} км)")
    print(f"Бюджет на закупівлю:  {total_cost:,} грн")
    print(f"Масштаб проєкту:      {comparison}")
    print("-" * 45)
    print("Аналіз завершено успішно.")

if __name__ == "__main__":
    run_advanced_analysis()