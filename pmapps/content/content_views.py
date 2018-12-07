from haystack import views

from content.models import Book


class BookSearchView(views.SearchView):
    def extra_context(self):
        context = super().extra_context()
        side_list = Book.objects.filter()
        context['side_list'] = side_list
        # context.pop('fuzzy_min_sim')

        return context