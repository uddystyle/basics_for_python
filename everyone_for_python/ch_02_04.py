from matplotlib import pyplot as plt
tokyo_temps = [15.1, 15.4, 15.2, 15.4, 17.0, 16.9]
# plt.plot(tokyo_temps)

tokyo_temps[5]-tokyo_temps[0]
# print(tokyo_temps[-1]-tokyo_temps[0])
# print(tokyo_temps[-1]-tokyo_temps[0])

e_tokyo_temps = [13.6, 13.5, 14.2, 14.8, 14.8]
tokyo_temps2 = e_tokyo_temps+tokyo_temps
# plt.plot(tokyo_temps2)
# plt.show()

mcz = ["れに", "あかり", "かなこ", "しおり", "あやか", "ゆきな"]
print(mcz)

mcz[5] = "ももか"
print(mcz)

del mcz[0]
print(mcz)

# slice

momotamai = mcz[1:3]
print(momotamai)
print(mcz)
print(mcz[:2])
print(mcz)
print(mcz[1:])


city_temps = [
    [14.8, 14.8, 15.1, 15.4, 15.2, 15.4, 17.0, 16.9],
    [10.0, 10.4, 11.5, 11.2, 10.9, 10.6, 11.8, 12.2],
    [16.0, 15.5, 15.9, 16.4, 15.9, 15.6, 17.5, 17.1]
]

print(city_temps[1])

kumamoto_avg = city_temps[2][7] - city_temps[2][0]
print(kumamoto_avg)

# plt.plot(city_temps[0])
# plt.plot(city_temps[1])
# plt.plot(city_temps[2])
# plt.show()

monk_fish_team = [158, 157, 163, 157, 145]
# print(sum(monk_fish_team))

# print(max(monk_fish_team))
# print(min(monk_fish_team))
# print(len(monk_fish_team))

monk_sum = sum(monk_fish_team)
monk_len = len(monk_fish_team)
monk_mean = monk_sum / monk_len
print(monk_mean)
plt.bar([0, 1, 2, 3, 4], monk_fish_team)
plt.plot([0, len(monk_fish_team)], [monk_mean, monk_mean], color='red')
plt.show()
