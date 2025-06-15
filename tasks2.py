import heapq

def merge_k_lists(lists):
    """
    Args:
        lists: Список відсортованих списків.
    Returns:
        Один відсортований список, що містить елементи з усіх списків.
    """
    min_heap = []
    
    # Додаємо перший елемент кожного списку до купи
    # Зберігаємо у форматі (значення, індекс_списку, індекс_елемента)
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))            
    merged_list = []
    
    # Поки купа не порожня
    while min_heap:
        # Витягуємо найменший елемент
        val, list_idx, element_idx = heapq.heappop(min_heap)
        
        # Додаємо його до результату
        merged_list.append(val)
        
        # Якщо в початковому списку є ще елементи, додаємо наступний до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))            
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)