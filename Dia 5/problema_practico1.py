def devolver_distintos(num1, num2, num3):
    if sum([num1, num2, num3] > 15):
        return max(num1, num2, num3)
    if sum([num1, num2, num3] < 10):
        return min(num1, num2, num3)
    if sum([num1, num2, num3] >= 10) and sum([num1, num2, num3] <= 15):
        return sum([num1, num2, num3]) / 3