from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class AttributeColumnManager(models.Manager):
    def years(self):
        return self.exclude(year=None).exclude(year='') \
                   .values_list('year', flat=True).order_by('year').distinct()


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
        return self.display_name

    @property
    def full_display_name(self):
        return self.display_name

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
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(default='')  # TODO: add minimal config
    content_format = models.CharField(max_length=4, choices=FORMAT_CHOICES, default='json')

    def save(self, *args, **kwargs):
        from weave.util import unique_slugify
        unique_slugify(self, self.name)
        super(ClientConfiguration, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.name
