"""
Specifying ordering

Specify default ordering for a model using the ``ordering`` attribute, which
should be a list or tuple of field names. This tells Django how to order
``QuerySet`` results.

If a field name in ``ordering`` starts with a hyphen, that field will be
ordered in descending order. Otherwise, it'll be ordered in ascending order.
The special-case field name ``"?"`` specifies random order.

The ordering attribute is not required. If you leave it off, ordering will be
undefined -- not random, just undefined.
"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Author(models.Model):
    class Meta:
        ordering = ('-pk',)


@python_2_unicode_compatible
class Article(models.Model):
    author = models.ForeignKey(Author, null=True)
    second_author = models.ForeignKey(Author, null=True)
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    class Meta:
        ordering = ('-pub_date', 'headline')

    def __str__(self):
        return self.headline


class OrderedByAuthorArticle(Article):
    class Meta:
        proxy = True
        ordering = ('author', 'second_author')


class Reference(models.Model):
    article = models.ForeignKey(OrderedByAuthorArticle)

    class Meta:
        ordering = ('article',)
