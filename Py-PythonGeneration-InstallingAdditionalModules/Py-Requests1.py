#Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла. Первое слово в тексте последнего файла: "We". Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. Все файлы располагаются в каталоге по адресу: https://stepic.org/media/attachments/course67/3.6.3/. Загрузите содержимое последнего файла из набора, как ответ на это задание
import requests
with open("dataset_3378_3.txt") as infile:
    url=infile.readline().strip()
    print(url)
    print("#Посмотрел, что ты мне там за ссылку дал#")
    read=requests.get(url)
    print(read)
    print("#Щас почитаю что там понаписали тебе в сссылке, которую ты мне дал#")
while True:
    newUrl="https://stepic.org/media/attachments/course67/3.6.3/"+read.text
    print(newUrl)
    print("#Блин, опять новая ссылка. что мне дал?#")
    read=requests.get(newUrl)
    print(read)
    print("#Лааааадно, я сам тебе его прочитаю#")
    if len(read.text)>20:
        print("#Нашайника, у нас проблемы, чот сильно много фигни#")
        break
with open("Сonclusion.txt",'w') as outfile:
    print("#Куда б тебе записать инфу???#")
    outfile.write(str(read.text))
    print("#А, вот куда записался#")