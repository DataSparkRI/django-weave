from django.db import models

class AttributeColumnManager(models.Manager):
    def years(self):
        return self.exclude(year=None).exclude(year='') \
                   .values_list('year', flat=True).order_by('year').distinct()

class CCDataStoryManager(models.Manager):
    def get_query_set(self):
        return super(CCDataStoryManager, self).get_query_set().filter(page__isnull=False)

class CCReportManager(models.Manager):
    def get_query_set(self):
        return super(CCReportManager, self).get_query_set().filter(report__isnull=False)

class CCUserGeneratedManager(models.Manager):
    def get_query_set(self):
        return super(CCUserGeneratedManager, self).get_query_set().filter(weavefile__isnull=False)

class CCUnassignedManager(models.Manager):
    def get_query_set(self):
        return super(CCUnassignedManager, self).get_query_set().filter(page__isnull=True, report__isnull=True, weavefile__isnull=True)
