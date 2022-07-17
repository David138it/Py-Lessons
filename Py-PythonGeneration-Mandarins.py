#n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
schools=int(input())
mandarinok=int(input())
print(mandarinok//schools)
print(mandarinok%schools)