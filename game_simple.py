import tkinter as tk
from tkinter import ttk
import time

class SimpleGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Простая Игра: День и Ночь")
        self.center_window(600, 400)  # Центрируем окно

        # Переменные для состояния игры
        self.is_running = False
        self.is_night = False
        self.lives = 10

        # Настройка графики
        self.canvas = tk.Canvas(self.root, width=600, height=300)
        self.canvas.pack()

        self.day_image = tk.PhotoImage(file="day.png")  # Замените на путь к вашему изображению дня
        self.night_image = tk.PhotoImage(file="night.png")  # Замените на путь к вашему изображению ночи
        self.current_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.day_image)

        # Статус бар
        self.status_bar = tk.Label(self.root, text=f"Жизнь: {self.lives}", font=("Helvetica", 14))
        self.status_bar.pack(side=tk.BOTTOM)

        # Кнопки управления
        self.start_button = tk.Button(self.root, text="Старт", command=self.start_game)
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.root, text="Пауза", command=self.pause_game)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.root, text="Стоп", command=self.stop_game)
        self.stop_button.pack(side=tk.LEFT)

        self.update_game()

    def center_window(self, width, height):
        # Получаем размеры экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Находим координаты для размещения окна по центру
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # Устанавливаем геометрию окна
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def update_game(self):
        if self.is_running:
            # Изменить состояние день/ночь
            self.is_night = not self.is_night
            if self.is_night:
                self.canvas.itemconfig(self.current_image, image=self.night_image)
                self.lives -= 1
            else:
                self.canvas.itemconfig(self.current_image, image=self.day_image)

            # Проверка на окончание игры
            if self.lives <= 0:
                self.stop_game()
                self.status_bar.config(text="Вы погибли!")
            else:
                self.status_bar.config(text=f"Жизнь: {self.lives}")

            # Изменение каждые 3 секунды
            self.root.after(3000, self.update_game)

    def start_game(self):
        if not self.is_running:
            self.is_running = True
            self.update_game()

    def pause_game(self):
        self.is_running = False

    def stop_game(self):
        self.is_running = False
        self.lives = 10
        self.status_bar.config(text=f"Жизнь: {self.lives}")
        self.canvas.itemconfig(self.current_image, image=self.day_image)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = SimpleGame()
    game.run()