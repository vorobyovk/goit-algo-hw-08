import heapq

def min_cost_to_connect_cables(cable_lengths):
    """
    Args:
        cable_lengths: Список, що містить довжини кабелів.
    Returns:
        Загальні мінімальні витрати на з'єднання всіх кабелів.
    """
    if len(cable_lengths) < 2:
        return 0
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cable_lengths)    
    total_cost = 0    
    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)        
        # Вартість їх з'єднання
        cost = first + second
        total_cost += cost        
        # Додаємо новий, з'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, cost)        
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cables)
print(f"Довжини кабелів: {cables}")
print(f"Мінімальні витрати на з'єднання: {min_cost}")

# Покрокове пояснення для [4, 3, 2, 6]:
# 1. З'єднуємо 2 і 3. Витрати: 5. Загальні витрати: 5. Кабелі: [4, 6, 5]
# 2. З'єднуємо 4 і 5. Витрати: 9. Загальні витрати: 5 + 9 = 14. Кабелі: [6, 9]
# 3. З'єднуємо 6 і 9. Витрати: 15. Загальні витрати: 14 + 15 = 29. Кабелі: [15]