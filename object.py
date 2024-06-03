import requests as rq
import re
import pandas as pd

from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
url = 'https://books.toscrape.com/catalogue/page-1.html'




# def getAllArticleList(bookContent):
#     articles =  bookContent.find_all('article')

#     for article in articles:
#         aObject = getArtilceObject(article)
#         print(f'aObject = {aObject}')




def getArticleTitle(article):
    title = article.find('h3').a['title']
    return title

print(getArticleTitle)

def getArticlePrice(article):
    pattern = r"([£$€])(\d+(?:\.\d+)?)"
    priceText = article.find('p',attrs={"class":"price_color"}).string
    match = re.search(pattern, priceText) 
    price = float(match.group(2))
    return price

print(getArticlePrice)


'''def getArtilceRating(article):
    rating = article.find('p', attrs= {"class":"star-rating"})['class'][1]
    allRating = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    numRating = allRating[rating]
    return numRating'''


def getArtilceObject(articles):

    atitle = getArticleTitle(articles)
    aPrice = getArticlePrice(articles)
    #aRating = getArtilceRating(articles)

    artileObj = {
        "title" : atitle,
        "price" : aPrice,
        #"rating": aRating
    }
    print(artileObj)
    return artileObj



'''def getAllArticleList(bookContent):
    articles =  bookContent.find_all('article')

    articleList = [getArtilceObject(article) for article in articles]

    return articleList


def MainFun(pageCount):
    ScrapUrl = f'https://books.toscrape.com/catalogue/page-{pageCount}.html'

    bookResp = rq.get(ScrapUrl, headers=headers)
    # print(f'status code = {bookResp.status_code}')
    if(bookResp.status_code == 200):
        print('do object opreation')
        bookContent = BeautifulSoup(bookResp.content, "html.parser")

        articles = getAllArticleList(bookContent)
        # print(articles[0]['price'])
        # sumTotal =  sum(book['price'] for book in articles)
        # print(sumTotal)

        # print(f'avg = {sumTotal/ len(articles)}')

        pdArticle = pd.DataFrame(articles)
        # # print(pdArticle.price)
        # # print(pdArticle.describe)
        # print(pdArticle[pdArticle.price > 50])
        pdArticle.to_csv(f'articles{pageCount}.csv')
    else:
        print('please check URL , somthing went wrong')

# {
#     title: '',
#     price: '',
#     rating: 3
# }

def getPageNumber():
    page =rq.get(url, headers=headers)
    bPage = BeautifulSoup(page.content, "html.parser")
    bForm = bPage.findAll('form', attrs={"method":"get"})
    bPageCount = int(bForm[0].findAll('strong')[2].string)
    print(bPageCount)
    for i in range(1,bPageCount):
        MainFun(i)

getPageNumber()



# {
#     title: '',
#     price: '',
#     rating: 3
# }
'''