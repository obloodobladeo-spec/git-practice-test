weapons= []
weapon_x_pos = 0
weapon_y_pos = 10
weapons.append([weapon_x_pos, weapon_y_pos])

running = True
while(running):
    weapons = [[w[0], w[1] - 1] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] >= 5]
    print(weapons)

