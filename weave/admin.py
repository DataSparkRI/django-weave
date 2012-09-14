from django.contrib import admin
from django.conf import settings
from weave.models import ClientConfiguration, GeometryCollection, \
                            AttributeColumn, CCDataStory, CCReport, \
                            CCUserGenerated, CCUnassigned

class ClientConfigurationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    def change_view(self, request, object_id, extra_context=None):
        context = {
            'weave_settings': settings.WEAVE
        }
        return super(ClientConfigurationAdmin, self).change_view(request,
            object_id, extra_context=context)

    list_display = ('name', 'cc_type', )

admin.site.register(ClientConfiguration, ClientConfigurationAdmin)
admin.site.register(AttributeColumn)
admin.site.register(GeometryCollection)
admin.site.register(CCDataStory)
admin.site.register(CCReport)
admin.site.register(CCUserGenerated)
admin.site.register(CCUnassigned)
