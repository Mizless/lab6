"""8.Формируется матрица F следующим образом: скопировать в нее А и если в С количество простых
чисел в нечетных столбцах больше, чем количество нулевых  элементов в четных строках,
то поменять местами Е и С симметрично, иначе С и В поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A-1*AT – K * F, иначе вычисляется выражение (AТ +G-1-F-1)*K, где G-нижняя треугольная матрица,
полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно."""

import random
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def IsPrime(k):

    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

print("\n----Результат работы программы----\n ----Локальное время", time.ctime(), "----")

try:
    row_q = int(input("Введите количество строк(столбцов) квадратной матрицы: "))
    K = int(input("Введите число K = "))
    start = time.time()
    A = np.zeros((row_q, row_q), dtype = int)
    F = np.zeros((row_q, row_q), dtype = int)

    for i in range(row_q): #   формируем матрицу A
        for j in range(row_q):
            A[i][j] = random.randint(0, 10)
            # A[i][j] = i * 10 + j
    print("Матрица A:\n", A)

    F = np.copy(A)   #   формируем матрицу F
    print("Матрица F:\n", F)

    C = np.zeros((row_q // 2, row_q // 2), dtype = int)   #   формируем матрицу C
    for i in range(row_q // 2):
        for j in range(row_q // 2):
            C[i][j] = F[i][row_q // 2 + (row_q % 2) + j]
    print("\nМатрица C:\n", C)

    q_prime, q_zero = 0, 0

    for i in range(row_q):   #   проверяем условие
        for j in range(row_q):
            if IsPrime(F[i][j]) and j % 2 == 0:
                    q_prime += 1
            elif F[i][j] == 0 and j % 2 == 1:
                    q_zero += 1
    if q_prime > q_zero:  #   меняем подматрицы местами
        for i in range(row_q // 2):
            for j in range(row_q // 2):
                F[i][j + row_q // 2 + row_q % 2], F[row_q - 1 - i][j + row_q // 2 + row_q % 2] = F[row_q - 1 - i][j + row_q // 2 + row_q % 2], F[i][j + row_q // 2 + row_q % 2]
    else:
        for i in range(row_q // 2):
            for j in range(row_q // 2):
                F[i][j], F[i][row_q // 2 + row_q % 2 + j] = F[i][row_q // 2 + row_q % 2 + j], F[i][j]
    print("\nМатрица F:\n", F)

    try:
        if np.linalg.det(A) > np.trace(F):
            print("\n---(A-1 * AT – K * F)---\n", (np.transpose(A) * np.linalg.inv(A)) - F * K) #   1 формула A-1 * AT – K * F
            A = (np.transpose(A) * np.linalg.inv(A)) - F * K

        else:
            print("\n---(AТ + G-1 - F-1) * K---\n", (np.transpose(A) + np.linalg.inv(np.tril(A, k = 0)) - np.linalg.inv(F)) * K)
            A = (np.transpose(A) + np.linalg.inv(np.tril(A, k = 0)) - np.linalg.inv(F)) * K      #   2 формула (AТ +G-1-F-1)*K

        print("\n---Ответ---")
        for i in A:
            for j in i:
                print("%5d" % j, end = ' ')
            print()
    except np.linalg.LinAlgError:
        print('\nОдна из матриц является вырожденной, вычисления невозможны.')

    finish = time.time()
    result = finish - start
    print("\nВремя работы программы: " + str(result) + " seconds.")

    """ВИЗУАЛИЗАЦИЯ"""

    """MatPlotLib"""
    plt.title("Plot")  #   1 пример matplotlib
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    for j in range(row_q):
        plt.plot([i for i in range(row_q)], A[j][::], marker='x')
    plt.show()

    plt.title("Scatter")  #   2 пример matplotlib
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    for j in range(row_q):
        plt.scatter([i for i in range(row_q)], A[j][::])
    plt.show()

    plt.title("Bar")  #   3 пример matplotlib
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    for i in range(row_q):
        plt.bar([i for i in range(row_q)], A[::-1][i], width=1)
    plt.show()

    """SEABORN"""

    sns.set_style("whitegrid")  #   1 пример seaborn
    sns.boxplot(data = A)
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    plt.show()

    sns.heatmap(data = A, annot = True)  #   3 пример seaborn
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    plt.show()

    sns.set_theme(style="darkgrid")  #   2 пример seaborn
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    sns.lineplot(data = A)
    plt.show()

except ValueError:
    print("\nДанные введены неверно.")




