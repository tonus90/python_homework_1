# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('file.txt', 'r') as file:
    lines_list = file.readlines()
    print(f'В документе - {len(lines_list)} строк')
    for i in range(len(lines_list)-1):
        list_words = lines_list[i].split()
        print(f'В {i+1} строке - {len(list_words)} слов')
    