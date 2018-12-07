from haystack import indexes
from content.models import Book


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects.all()