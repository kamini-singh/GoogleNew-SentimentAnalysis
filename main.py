from requests_html import HTMLSession
class GoogleSearchNews:
    def paginate(self, url):
        session= HTMLSession()
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }
        resp=session.get(url, headers=header)
        yield resp
    def scrape_articles(self):
        pages =self.paginate("https://www.google.com/search?q=biden&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwjAvsKDyOXtAhXBhOAKHXWdDgcQpwUIKQ&biw=1604&bih=760&dpr=1.2")
        for page in pages:
            articles= page.html.find("a.WlydOe")
            for article in articles:
                title= article.find("div.mCBkyc")[0].text
                print(title)
news= GoogleSearchNews()
news.scrape_articles()
