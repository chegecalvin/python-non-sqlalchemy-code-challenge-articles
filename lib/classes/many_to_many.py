class Article:
    all=[]

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    def get_title(self):
        return self._title
    
    def set_title(self,title):
        if not isinstance(title,str):
            return None
        if not (5<=len(title)<=50):
            return None
        if hasattr(self,'_title'):
            return None
        
        self._title=title
    title=property(get_title,set_title)

    def get_author(self):
        return self._author
    
    def set_author(self,author):
        self._author=author
    author=property(get_author,set_author)

    def get_magazine(self):
        return self._magazine
    
    def set_magazine(self,magazine):
        self._magazine=magazine
    magazine=property(get_magazine,set_magazine)
        
class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if not isinstance (name,str) or len(name) == 0:
            return None
        if hasattr (self,'_name'):
            return None
        self._name=name
    name = property(get_name,set_name)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        author_articles = self.articles()
        if not author_articles:
            return None
        return list(set(article.magazine.category for article in author_articles))
        
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if isinstance(name,str) and 2 <= len(name) <= 16:
            self._name=name
    name=property(get_name,set_name)

    def get_category(self):
        return self._category
    
    def set_category(self,category):
        if isinstance (category,str) and len(category) > 0:
            self._category=category
    category=property(get_category,set_category)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        magazine_articles = [article.title for article in self.articles()]
        if not magazine_articles:
            return None
        return magazine_articles

    def contributing_authors(self):
        author_count = {}
        for article in Article.all:
            if article.magazine == self:
                if article.author in author_count:
                    author_count[article.author] += 1
                else:
                    author_count[article.author] = 1
                    
        contributers = [author for author, count in author_count.items() if count > 2]

        if not contributers:
            return None
        return contributers
            