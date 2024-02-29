class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._set_title(title)
        if not isinstance(author, Author):
            raise TypeError("author must be of type Author")
        self._author = author
        self._magazine = magazine
        self._author.add_articles(self)
        self._magazine.add_articles(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._set_title(new_title)

    def _set_title(self, new_title):
        if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        else:
            self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("author must be of type Author")
        else:
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("magazine must be of type Magazine")
        else:
            self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a string with at least 1 character")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_author_name):
        if not isinstance(new_author_name, str) or len(new_author_name) == 0:
            raise ValueError("Name must be a string with at least 1 character")
        else:
            self._name = new_author_name

    @property
    def articles(self):
        return self._articles

    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")

    @property
    def magazines(self):
        unique_magazines_set = {article.magazine for article in self._articles}
        return list(unique_magazines_set)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    @property
    def topic_areas(self):
        if not self._articles:
            return None
        unique_categories_set = {article.magazine.category for article in self._articles}
        return list(unique_categories_set)


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name
        else:
            raise ValueError("Name must be between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be a string with length more than 0 characters")

    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        unique_authors_set = {article.author for article in self._articles}
        return list(unique_authors_set) if unique_authors_set else None

    @property
    def article_titles(self):
        if not self._articles:
            return None
        unique_titles = [article.title for article in self._articles]
        return unique_titles

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        double_authors = [author for author, count in author_counts.items() if count > 2]

        if double_authors:
            return double_authors
        else:
            return None

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._set_title(title)
        if not isinstance(author, Author):
            raise TypeError("author must be of type Author")
        self._author = author
        self._magazine = magazine
        self._author.add_articles(self)
        self._magazine.add_articles(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._set_title(new_title)

    def _set_title(self, new_title):
        if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        else:
            self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("author must be of type Author")
        else:
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("magazine must be of type Magazine")
        else:
            self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a string with at least 1 character")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_author_name):
        if not isinstance(new_author_name, str) or len(new_author_name) == 0:
            raise ValueError("Name must be a string with at least 1 character")
        else:
            self._name = new_author_name

    @property
    def articles(self):
        return self._articles

    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")

    @property
    def magazines(self):
        unique_magazines_set = {article.magazine for article in self._articles}
        return list(unique_magazines_set)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    @property
    def topic_areas(self):
        if not self._articles:
            return None
        unique_categories_set = {article.magazine.category for article in self._articles}
        return list(unique_categories_set)


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name
        else:
            raise ValueError("Name must be between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be a string with length more than 0 characters")

    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        unique_authors_set = {article.author for article in self._articles}
        return list(unique_authors_set) if unique_authors_set else None

    @property
    def article_titles(self):
        if not self._articles:
            return None
        unique_titles = [article.title for article in self._articles]
        return unique_titles

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        double_authors = [author for author, count in author_counts.items() if count > 2]

        if double_authors:
            return double_authors
        else:
            return None

