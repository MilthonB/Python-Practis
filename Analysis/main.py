from bs4 import BeautifulSoup
import re
import csv
import os



# file_path = './pages/sopas.html'
file_paths = os.listdir('./pages/')

for file in file_paths:
    # print(file_paths)
    if file == '.gitkeep': continue
    
    name_file = file.split('.')[0]

    file_path = f'./pages/{file}' 
    print(name_file)

    data = []
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        html_content = file.read()

    # Usar BeautifulSoup para parsear el HTML
    soup = BeautifulSoup(html_content, 'html.parser')


    # Buscar todos los <section> y obtener su id
    # count = 0
    datain =  []
    for section in soup.find_all('section'):
        section_id = section.get('id')
        span_text = ''
        img_url = ''


        if(section_id == 'descProduct'):
            span = section.find('span')
            span_text = re.sub(r'\s+',' ',span.get_text()) 
            # span_text = 'None' 
            # print(span_text)
            datain.append(span_text)

        if(section_id == 'imgProductSec'):
            # print(section_id)
            img =  section.find('img')
            img_url = img.get('src') if img  else None
            # print(img_url)
            datain.append(img_url)

        if(datain):
            data.append([img_url,span_text])
            datain =  []

    # print(data)
    with open(f'./output/{name_file}.csv', mode='w', newline='', encoding='utf-8') as files:
        write =  csv.writer(files)
        write.writerow(['imrUrl','name'])
        write.writerows(data)