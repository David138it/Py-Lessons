#Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.
total_minuts=int(input())
hour=60
print(total_minuts,"мин - это",total_minuts//hour,"час",total_minuts%hour,"минут.")
