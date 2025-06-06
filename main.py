#Вгадай число
import random

#Відгадування числа
def Choose_the_Number(random_number):
    for i in range(1, 7, 1): #Цикл для відгадування
        number = int(input("Введіть число: "))
        if number == random_number:
            print(f"Ви відгадали число з {i} сроб/и! Загадане число було {random_number}!")
            break
        elif number > random_number:
            print(f"Занадто велике!\nЗалишилося {7-i} спроб/и!")
        else:
            print(f"Занадто маленьке!\nЗалишилося {7-i} спроб/и!")
    print("Гру завершено! Вітаю")

def main():
    # Загадування числа
    random_number = random.randint(1, 100)
    print("Я загадав число від 1 до 100! В тебе є 7 спроб, щоб його відгадати!")
    ask = input("Бажаєш зіграти?\n")
    if ask == "Так":
        Choose_the_Number(random_number)
    else:
        print("Шкода(\nЗустрінемось!")

if __name__ == "__main__":
    main()

