import tkinter as tk
from datetime import datetime

class SimpleGame:
    def __init__(self, user_name):
        self.root = tk.Tk()
        self.root.title("Простая Игра: День и Ночь")
        self.center_window(600, 500)  # Центрируем окно

        # Переменные для состояния игры
        self.is_running = False
        self.is_night = False
        self.lives = 10

        # Настройка графики
        self.canvas = tk.Canvas(self.root, width=600, height=300)
        self.canvas.pack()

        # Замените на путь к вашим изображениям дня и ночи
        self.day_image = tk.PhotoImage(file="day.png")  
        self.night_image = tk.PhotoImage(file="night.png")  
        self.current_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.day_image)

        # Создаем метку с текстом "Добро пожаловать" и имя пользователя
        current_time = datetime.now().strftime("%H:%M:%S")
        welcome_label = tk.Label(self.root, text=f"Добро пожаловать, {user_name}!\nТекущее время: {current_time}", font=("Helvetica", 16))
        welcome_label.pack(pady=10)  # Установите отступы сверху и снизу

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
            # Смена состояние день/ночь
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

def start_game_with_name():
    user_name = name_entry.get()
    root.destroy()  # Закрываем текущее окно ввода
    game = SimpleGame(user_name)  # Запускаем игру с именем
    game.run()  # Запускаем главный цикл игры

# Создаем главное окно
root = tk.Tk()
root.title("Введите данные")

# Установка размеров окна
root.geometry("300x400")

# Устанавливаем расположение окна по центру экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (300 // 2)
y = (screen_height // 2) - (200 // 2)
root.geometry(f"300x400+{x}+{y}")

# Поля ввода
name_label = tk.Label(root, text="Введите ваше имя:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

age_label = tk.Label(root, text="Введите ваш возраст:")
age_label.pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

gender_label = tk.Label(root, text="Выберите пол:")
gender_var = tk.StringVar(value="муж")
male_radio = tk.Radiobutton(root, text="Муж", variable=gender_var, value="муж")
male_radio.pack(pady=5)
female_radio = tk.Radiobutton(root, text="Жен", variable=gender_var, value="жен")
female_radio.pack(pady=5)

# Кнопка "Начать игру"
start_button = tk.Button(root, text="Начать игру", command=start_game_with_name)
start_button.pack(pady=20)

# Запускаем основной цикл
root.mainloop()