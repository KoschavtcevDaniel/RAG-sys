import tkinter as tk
from tkinter import ttk
import agent
import time


def center_window(window, width=400, height=300):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def answering():
    start_time = time.time()
    answer = agent.answer_question(entry.get())
    output_label.config(text=f"Ответ: {answer}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    time_label.config(text=f"Время выполнения: {elapsed_time:.4f} сек.")

# Создаем главное окно
root = tk.Tk()
root.title("ИИ помощник")
root.resizable(False, False)

# Центрируем окно
center_window(root, 800, 500)

# Устанавливаем стиль
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))

# Настраиваем цвета фона и текста
bg_color = "#ADD8E6"
text_color = "#00008B"

# Устанавливаем цвет фона для всего окна
root.configure(bg=bg_color)

# Основной фрейм с отступами
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Время выполнения
time_label = ttk.Label(
    main_frame,
    text="",
    foreground="black",
    font=("Helvetica", 10)
)
time_label.pack(pady=(0, 10))

# Заголовок
title_label = ttk.Label(main_frame, text="Введите текст", style="Header.TLabel")
title_label.pack(pady=(0, 20))

# Поле ввода
entry = ttk.Entry(main_frame, width=40)
entry.pack(pady=10)

# Кнопка
submit_button = ttk.Button(main_frame, text="Получить ответ", command=answering)
submit_button.pack(pady=10)

# Поле вывода
output_label = ttk.Label(
    main_frame,
    text="",
    foreground=text_color,
    wraplength=400,  # Автоматический перенос текста
    justify="center"
)
output_label.pack(pady=10)

# Запуск главного цикла
root.mainloop()