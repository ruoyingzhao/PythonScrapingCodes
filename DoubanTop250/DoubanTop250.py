import requests, bs4, openpyxl

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='Films'
sheet.append(['序号','片名','评分','简介','豆瓣链接'])

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

for x in range(10):
    url = 'https://movie.douban.com/top250'
    params={'start':str(x*25),'filter':''}
    res=requests.get(url, headers=headers, params=params)
    bs = bs4.BeautifulSoup(res.text,'html.parser')
    bs=bs.find('ol',class_='grid_view')
    
    list1=bs.find_all('div',class_='item')
    for film in list1:
        num = film.find('em', class_='').text
        title=film.find('span',class_='title').text
        rating=film.find('span', class_='rating_num').text
        url=film.find('a')['href']
        if film.find('span', class_='inq') != None:
            summary=film.find('span', class_='inq').text
        else:
            summary=''
        
        print(num,'\n', title, '\n', rating, '\n', summary, '\n', url)
        print('----------------\n')
        
        sheet.append([num, title, rating, summary, url])
        
wb.save('豆瓣电影Top250.xlsx')