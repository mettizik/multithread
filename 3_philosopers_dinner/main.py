#!/usr/bin/python3
from philosopher import RoundTable, Philosopher

philosopers = []
philosopers.append(Philosopher('Albert', 100))
philosopers.append(Philosopher('Zigfrid', 80))
philosopers.append(Philosopher('Nizche', 82))
philosopers.append(Philosopher('Zigmund', 76))
philosopers.append(Philosopher('Jozeph', 24))

table = RoundTable()
for phil in philosopers:
    table.append(phil)

print('PHILOSOPHERS || {:<10} || {:<10} || {:<10} || {:<10} || {:<10} ||'.format(
    philosopers[0].name(), philosopers[1].name(), 
    philosopers[2].name(), philosopers[3].name(), 
    philosopers[4].name()))

while True:
    import time
    time.sleep(0.1)
    print('\rMEALS COUNT  || {:<10} || {:<10} || {:<10} || {:<10} || {:<10} ||'.format(
        philosopers[0].meals_count, philosopers[1].meals_count,
        philosopers[2].meals_count, philosopers[3].meals_count, 
        philosopers[4].meals_count), end='')
