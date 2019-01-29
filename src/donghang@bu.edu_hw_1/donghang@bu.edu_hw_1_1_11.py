#Population projection

total = 365 * 24 * 60 * 60
t_birth = total // 7
t_death = total // 13
t_immigrant = total // 45

population = 312032486
i = 0
while i < 5:
    population = population + t_birth + t_immigrant - t_death
    print(population)
    i += 1