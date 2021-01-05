my_rating = [7, 7, 5, 4, 2]
print(my_rating)

rate_it = int(input('поставь рейтинг от 1 до 10: '))

n = 0
while n < len(my_rating):
    if my_rating.count(rate_it) > 0 and rate_it == my_rating[n]:
        my_rating.insert(my_rating.index(my_rating[n])+my_rating.count(rate_it), rate_it)
        break
    elif rate_it > my_rating[n]:
        my_rating.insert(my_rating.index(my_rating[n]), rate_it)
        break
    elif rate_it < my_rating[len(my_rating)-1]:
        my_rating.insert(len(my_rating), rate_it)
        break
    n+=1

print(my_rating)