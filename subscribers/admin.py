from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Subscribers

# Register your models here.

class SubscriberAdmin(ModelAdmin):
    """Subscriber admin"""

    model = Subscribers
    menu_label = "Subscriber"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    list_display = ("email", "full_name")
    search_fields = ("email", "full_name")

modeladmin_register(SubscriberAdmin)