input_file = open('pipes.txt')
output_file = open('time.txt', 'w')
pipes = input_file.readlines()
workers = list(int(i) for i in pipes[-1].split())
pipes = list(map(lambda x: float(x.strip()), pipes[:-2]))
new_pipes = list(pipes[i] * 60 for i in range(len(pipes)) if i + 1 in workers)
nok = 1
for i in new_pipes:
    nok *= i
s = 0
for pipe in new_pipes:
    s += nok / pipe
print(nok / s, file=output_file)
