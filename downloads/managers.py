from django.db.models import Manager
from django.db.models.query import QuerySet


class ReleaseQuerySet(QuerySet):
    def published(self):
        return self.filter(is_published=True)

    def draft(self):
        return self.filter(is_published=False)

    def downloads(self):
        """ For the main downloads landing page """
        return self.select_related('release_page').filter(
            is_published=True,
            show_on_download_page=True,
        ).order_by('-release_date')

    def python2(self):
        return self.filter(version=2, is_published=True)

    def python3(self):
        return self.filter(version=3, is_published=True)

    def pre_release(self):
        return self.filter(pre_release=True)

    def released(self):
        return self.filter(is_published=True, pre_release=False)


class ReleaseManager(Manager):
    def get_query_set(self):
        return ReleaseQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_query_set().published()

    def draft(self):
        return self.get_query_set().draft()

    def downloads(self):
        """ For the main downloads landing page """
        return self.get_query_set().downloads()

    def python2(self):
        return self.get_query_set().python2()

    def python3(self):
        return self.get_query_set().python3()

    def pre_release(self):
        return self.get_query_set().pre_release()

    def released(self):
        return self.get_query_set().released()
