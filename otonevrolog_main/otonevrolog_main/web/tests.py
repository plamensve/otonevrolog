from datetime import datetime

# Получаване на текущата дата
current_date = datetime.now()

# Получаване на деня от седмицата като число (понеделник е 0, неделя е 6)
day_of_week_number = current_date.weekday()

# Получаване на деня от седмицата като текст (пример: "Monday", "Tuesday")
day_of_week_text = current_date.strftime("%A")

print("Днес е:", day_of_week_text)  # Името на деня
print("Ден от седмицата (число):", day_of_week_number)  # Числото на деня

