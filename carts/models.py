#carts/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
import books
import users


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(users.models.User, null = True)
    item_count = models.PositiveIntegerField(default=0)
    order_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null = True)
    item = models.ForeignKey(books.models.Book, null = True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item


class SavedItem(models.Model):
    cart = models.ForeignKey(Cart, null = True)
    item = models.ForeignKey(books.models.Book, null = True)

    def __str__(self):
        return self.item
