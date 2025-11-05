WHITE = '\u001b[47m'
END = '\u001b[0m'

with open('python2025-lab-1/s.txt') as file:
    numbers = [float(line) for line in file]

even_sum = sum(abs(numbers[i]) for i in range(0, len(numbers), 2))
odd_sum = sum(abs(numbers[i]) for i in range(1, len(numbers), 2))

even_percent = round((even_sum / (even_sum + odd_sum)) * 100, 2)

diagram_length = 50
even_bars = int((even_percent / 100) * diagram_length)

print(f"Процент четных позиций {even_percent}%")
print("Процент нечетных позиций ", 100-even_percent, "%", sep="")
print(f"[{WHITE}{' ' * even_bars}{END}{' ' * (diagram_length - even_bars)}]")
