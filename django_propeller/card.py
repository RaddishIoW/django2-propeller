# -*- coding: utf-8 -*-

"""This module contains classes for constructing propeller cards"""

from django.utils.safestring import mark_safe

from .utils import render_tag, add_css_class
from .components import Button, FAB, Image
from .text import text_concat
from .exceptions import PropellerException


class CardTitle(object):

    """Renders a Card Title"""

    text = ""
    size = 3

    def as_html(self):
        """Returns card title as html"""
        tag = 'h%d' % self.size
        attrs = {'class': 'pmd-card-title-text'}
        content = self.text
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class CardSubtitle(object):

    """Renders a Card Subtitle"""

    text = ""

    def as_html(self):
        """Returns card subtitle as html"""
        tag = 'span'
        attrs = {'class': 'pmd-card-subtitle-text'}
        content = self.text
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class CardBody(object):

    """Renders a Card Body"""

    text = ""

    def as_html(self):
        """Returns card body as html"""
        tag = 'div'
        attrs = {'class': 'pmd-card-body'}
        content = self.text
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class CardHeader(object):

    """Renders a Card Header"""

    content_left = []
    content_middle = []

    def get_left_content(self):
        """Returns left content of card header as html"""
        tag = 'div'
        attrs = {'class': 'media-left'}
        content = ''
        for itm in self.content_left:
            content = text_concat(content, mark_safe(itm.as_html()))
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )

    def get_middle_content(self):
        """Returns middle content of card header as html"""
        tag = 'div'
        attrs = {'class': 'media-body media-middle'}
        content = ''
        for itm in self.content_middle:
            content = text_concat(content, mark_safe(itm.as_html()))
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )

    def as_html(self):
        """Returns card header as html"""
        tag = 'div'
        attrs = {'class': 'pmd-card-title'}
        content = text_concat(self.get_left_content(), self.get_middle_content())
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class CardMediaActions(object):

    """Renders Card Media Actions"""

    items = []

    def as_html(self):
        """Returns card media actions as html"""
        tag = 'div'
        attrs = {'class': 'pmd-card-actions'}
        content = ''
        for btn in self.items:
            if isinstance(btn, FAB):
                content = text_concat(content, mark_safe(btn.as_html()))
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class CardActions(object):

    """Renders Card Actions"""

    items = []

    def as_html(self):
        """Returns card actions as html"""
        tag = 'div'
        attrs = {'class': 'pmd-card-actions'}
        content = ''
        for btn in self.items:
            if isinstance(btn, Button):
                content = text_concat(content, mark_safe(btn.as_html()))
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class CardMediaImage(object):

    """Renders a Card Media Image"""

    image = None

    def as_html(self):
        """Returns card media image as html"""
        if isinstance(self.image, Image):
            return self.image.as_html()
        return None


class CardMedia(object):

    """Renders Card Media"""

    content = None
    style_inline = False

    def get_media_body_inline(self):
        """Returns media body inline as html"""
        tag = 'div'
        attrs = {'class': 'media-body'}
        content = ''
        if self.style_inline:
            if not isinstance(self.content, list):
                raise PropellerException("Propeller Card: content must be a list")
            for itm in self.content:
                if isinstance(itm, (CardTitle, CardSubtitle)):
                    content = text_concat(content, mark_safe(itm.as_html()))
            content = text_concat(content, mark_safe('</div>'))
            content = text_concat(content, mark_safe('<div class="media-right media-middle">'))
            for itm in self.content:
                if isinstance(itm, CardMediaImage):
                    content = text_concat(content, mark_safe(itm.as_html()))
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )

    def get_media_body(self):
        """Returns media body as html"""
        if self.style_inline:
            return self.get_media_body_inline()

        tag = 'div'
        attrs = {'class': 'media-body'}
        content = ''
        if not isinstance(self.content, list):
            raise PropellerException("Propeller Card: content must be a list")
        for itm in self.content:
            if isinstance(itm, CardMediaImage):
                content = text_concat(content, mark_safe(itm.as_html()))

        return render_tag(tag, attrs=attrs, content=mark_safe(content), )

    def as_html(self):
        """Returns card media as html"""
        tag = 'div'
        attrs = {'class': 'pmd-card-media'}
        content = self.get_media_body()
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class Card(object):

    """Card is a class that generates a Propeller Card"""

    primary_title = None
    secondary_title = None
    header = None
    media = None
    body = None
    actions = None
    media_actions = None
    style_inverse = False
    style_inline = False
    width = 4

    def get_actions(self):
        """Returns actions of card as html"""
        actions = ''
        if self.media_actions:
            actions = text_concat(actions, self.media_actions.as_html())
        if self.actions:
            actions = text_concat(actions, self.actions.as_html())
        return actions

    def get_content(self):
        """Returns content of card as html"""
        content = ''
        if self.header and not self.style_inline:
            content = text_concat(content, self.header.as_html())
        if self.media:
            content = text_concat(content, self.media.as_html())
        if not self.style_inline:
            if self.primary_title or self.secondary_title:
                content = text_concat(content, '<div class="pmd-card-title">')
                if self.primary_title:
                    content = text_concat(content, self.primary_title.as_html())
                if self.secondary_title:
                    content = text_concat(content, self.secondary_title.as_html())
                content = text_concat(content, '</div>')
            if self.body:
                content = text_concat(content, self.body.as_html())
        content = text_concat(content, self.get_actions())
        return content

    def as_html(self):
        """Returns card as html"""
        tag = 'div'
        classes = 'pmd-card'
        if self.style_inline:
            classes = add_css_class(classes, 'pmd-card-media-inline')
        if self.style_inverse:
            classes = add_css_class(classes, 'pmd-card-inverse')
        else:
            classes = add_css_class(classes, 'pmd-card-default')
        classes = add_css_class(classes, 'pmd-z-depth')
        classes = add_css_class(classes, 'col-md-%d' % self.width)
        attrs = {'class': classes}
        content = self.get_content()
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )
