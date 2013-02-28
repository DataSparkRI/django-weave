from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from weave.managers import AttributeColumnManager, CCDataStoryManager, CCReportManager, \
                            CCUserGeneratedManager, CCUnassignedManager


class BaseAttributeColumn(models.Model):
    """
    Abstract model to represent the fields necessary for Weave's configuration
    entries.

    The only difference from Weave's schema is the introduction of
    `unique_together`. Any fields added in addition to these must be nullable,
    or have a default value set, otherwise updates through Weave's admin console
    will fail.
    """
    DATA_TYPE_CHOICES = (
        ('number', 'number'),
        ('string', 'string')
    )

    name = models.CharField(max_length=256)
    keyType = models.CharField(max_length=256)
    dataType = models.CharField(max_length=256, choices=DATA_TYPE_CHOICES)
    dataTable = models.CharField(max_length=256)
    geometryCollection = models.CharField(max_length=256)
    year = models.CharField(max_length=256, null=True, blank=True)
    min = models.CharField(max_length=256, null=True, blank=True)
    max = models.CharField(max_length=256, null=True, blank=True)
    connection = models.CharField(max_length=256)
    sqlQuery = models.CharField(max_length=2048)
    title = models.CharField(max_length=256, blank=True, default='', null=True)

    class Meta:
        unique_together = (
            ('name', 'keyType', 'year', 'dataTable', ),
        )
        abstract = True


class AttributeColumn(BaseAttributeColumn):
    """
    Additional fields to add functionality on top of BaseAttributeColumn.

    Adds a GFK to allow this `AttributeColumn` to be linked to a source model.
    Using a Django model will introduce a surrogate key not strictly necessary
    for Weave.
    """
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    source = generic.GenericForeignKey('content_type', 'object_id')

    objects = AttributeColumnManager()

    @property
    def weave_display_name(self):
        return self.title

    @property
    def full_display_name(self):
        return self.title

    def __unicode__(self):
        return u"%s" % self.full_display_name


class GeometryCollection(models.Model):
    """A geometry collection that's been imported through the Weave Admin
    console.
    """
    name = models.CharField(max_length=256)
    keyType = models.CharField(max_length=256)
    importNotes = models.CharField(max_length=256, blank=True)
    connection = models.CharField(max_length=256)
    schema = models.CharField(max_length=256)
    tablePrefix = models.CharField(max_length=256)
    projection = models.CharField(max_length=256, default="EPSG:4326")

    def __unicode__(self):
        return u'Geometry Collection: %s' % (self.name, )


class ClientConfiguration(models.Model):
    FORMAT_CHOICES = (
        ('json', 'json'),
        ('xml', 'xml'),
        ('file', 'file')
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(default='', blank=True)  # TODO: add minimal config
    # name of the file, relative to Tomcat's/weave's docroot. This will be passed on as
    # as a url to the weave client
    content_file = models.CharField(max_length=100, unique=True, null=True, blank=True)
    content_format = models.CharField(max_length=4, choices=FORMAT_CHOICES, default='file')

    def cc_type(self):
        is_user_generated = self.weavefile_set.all().count() > 0
        in_datastory = self.page_set.all().count() > 0
        in_report = self.report_set.all().count() > 0

        return 'ug: %s / ds: %s / rpt: %s' % (is_user_generated, in_datastory, in_report)
    cc_type.short_description = 'CC Type'
      

    def save(self, *args, **kwargs):
        from weave.util import unique_slugify
        unique_slugify(self, self.name)
        super(ClientConfiguration, self).save(*args, **kwargs)

    @property
    def location_for_client(self):
        """ The url or path that should be passed to the Weave client to load this config """
        if self.content_format not in ('file', ):
            raise NotImplemented('Only file-based configs may be saved at this time')
        return "/weave_docroot/%s" % self.content_file

    def __unicode__(self):
        return "%s" % self.name

class CCDataStory(ClientConfiguration):
    class Meta:
        proxy = True
        verbose_name_plural = 'Client configurations (Datastory)'
        verbose_name = 'Client configuration (Datastory)'

    def __unicode__(self):
        return "%s" % self.name

    objects = CCDataStoryManager()

class CCReport(ClientConfiguration):
    class Meta:
        proxy = True
        verbose_name_plural = 'Client configurations (Report)'
        verbose_name = 'Client configuration (Report)'

    def __unicode__(self):
        return "%s" % self.name

    objects = CCReportManager()

class CCUserGenerated(ClientConfiguration):
    class Meta:
        proxy = True
        verbose_name_plural = 'Client configurations (User-generated)'
        verbose_name = 'Client configuration (User-generated)'

    def __unicode__(self):
        return "%s" % self.name

    objects = CCUserGeneratedManager()


class CCUnassigned(ClientConfiguration):
    class Meta:
        proxy = True
        verbose_name_plural = 'Client configurations (Unassigned)'
        verbose_name = 'Client configuration (Unassigned)'

    def __unicode__(self):
        return "%s" % self.name

    objects = CCUnassignedManager()
