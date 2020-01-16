from django.db import models

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_names='form_fields')

class FormPage(AbstractEmailForm):

    template = 'contact/contact_page.html'

    intro = RichTextField(blank=true)
    tank_you_text = RichTextField(blank=true)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields'),
        FieldPanel('tank_you_text'),
    ]