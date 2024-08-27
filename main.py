from datetime import datetime

class Task:
    def __init__(self, task_id, description, deadline):
        #класс для задач с уник ID, описанием и дедлайном. По умолчанию задача со статусом - не выполненна.

        self.task_id = task_id
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        #Отметка задачи как выполненной.
        self.completed = True

    def __str__(self):
        #Представление задачи строкой (спасибо ЧАТ за подсказку этого момента).
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"№{self.task_id} | Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        #создаем класс  менеджера задач с пустым списком задач и счетчиком
        self.tasks = []
        self.next_id = 1

    def add_task(self, description, deadline):
        #Добавление новой задачи с уникальным номером в список
        task = Task(self.next_id, description, deadline)
        self.tasks.append(task)
        self.next_id += 1

    def mark_task_as_completed(self, task_id):
        #Отметка задачи (с определенным номером) как выполненная
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_completed()
                return True
        return False

    def get_current_tasks(self):
        # Возврат списка невыполненных задач
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        # Вывод списка всех задач
        for task in self.tasks:
            print(task)


def input_valid_deadline():
    # проверка на прошлость дедлайна
    while True:
        deadline_str = input("Введите срок выполнения задачи (в формате YYYY-MM-DD): ")
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            if deadline >= datetime.today().date():
                return deadline_str
            else:
                print("Ошибка: Дедлайн не может быть в прошлом. Попробуйте снова.")
        except ValueError:
            print("Ошибка: Неверный формат даты. Попробуйте снова.")


def main():
    manager = TaskManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить новую задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать текущие задачи")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            deadline = input_valid_deadline()
            manager.add_task(description, deadline)
            print("Задача добавлена!")

        elif choice == "2":
            manager.show_tasks()
            try:
                task_id = int(input("Введите номер задачи, которую хотите отметить как выполненную: "))
                if manager.mark_task_as_completed(task_id):
                    print("Задача отмечена как выполненная!")
                else:
                    print("Задача с таким номером не найдена.")
            except ValueError:
                print("Ошибка: Введите корректный номер задачи.")

        elif choice == "3":
            print("\nТекущие задачи:")
            current_tasks = manager.get_current_tasks()
            if not current_tasks:
                print("Все задачи выполнены!")
            else:
                for task in current_tasks:
                    print(task)

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 4.")

if __name__ == "__main__":
    main()
