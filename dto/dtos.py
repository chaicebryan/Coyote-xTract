class Article:

    def __int__(self, id, author, title, description, text, creation_date, last_modified, category, source):
        self.id = id
        self.author = author
        self.title = title
        self.descrption = description
        self.text = text
        self.creation_date = creation_date
        self.last_modified = last_modified
        self.category = category
        self.source = source

class GuardianArticle(Article):

class BBCArticle(Article):

class RedditArticle(Article):

class IGNArticle(Article):

