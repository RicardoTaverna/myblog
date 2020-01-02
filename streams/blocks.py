"""Streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """ Title and text and noting else """

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add aditional text')

    class Meta: 
        template = "streams/title_and_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and buttons"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=50)),
                ("text", blocks.CharBlock(required=True, max_length=240)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta: 
        template = "streams/card_block.html"
        icon = "doc-full"
        label = "Gallery"


class RichtextBlock(blocks.RichTextBlock):
    """ Richtext with all the features"""
    

    class Meta: 
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full Richtext"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """ Richtext without all the features"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]        

    class Meta: 
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple Richtext"
    
class CTABlock(blocks.StructBlock):
    """A simple call to action section"""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"