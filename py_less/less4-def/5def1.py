def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)  #[:] создает копию списка
"""Несмотря на то что передача копии позволяет сохранить содержимое списка, обыч-
но функциям следует передавать исходный список (если у вас нет веских причин
для передачи копии). Работа с существующим списком более эффективна, потому
что программе не приходится тратить время и память на создание отдельной копии
(лишние затраты особенно заметны при работе с большими списками)."""
show_completed_models(completed_models)