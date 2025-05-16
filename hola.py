word = 'hello word'
for chd in word:
    print(chd)

ch_list = [ch for ch in word]
print(ch_list)

def fibonacci(n):
    a, b = 0, 1
    while a <=n:
        yield a
        a, b = b, a+b

fibo_sequence = list(fibonacci(20))
print(fibo_sequence)