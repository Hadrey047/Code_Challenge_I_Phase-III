

class Article:
    
    all_article = []
    
    def __init__(self,author="Bolaji Salami",magazine="Love Lines",title="Love is not enough"):
        self.author = author 
        self.magazine = magazine
        self.title = title 
        Article.all_article.append(self)
     
        
    def article_title(self):
        return self.title
    
    def article_all(self):
        return self.all_article
    

    
    


