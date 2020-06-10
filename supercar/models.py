from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.db import models
from django_countries.fields import CountryField

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


"""
db_table = 'slownik_grupy'
"""


class DictGroup(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    name_autopanel = models.CharField(
        db_column='nazwa_autopanel', max_length=50, blank=True, null=True)
    identificator = models.CharField(
        db_column='identyfikator', max_length=9, blank=True, null=True)
    id_worker_1 = models.IntegerField(
        db_column='id_pracownika_1', blank=True, null=True)
    id_worker_2 = models.IntegerField(
        db_column='id_pracownika_2', blank=True, null=True)
    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_system = models.IntegerField(
        db_column='systemowy', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'slownik_grupy'


"""
db_table = 'slownik_rodzaje'
"""


class DictType(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    group = models.ForeignKey(
        DictGroup, on_delete=models.SET_NULL, db_column='id_grupy', blank=True, null=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_system = models.IntegerField(
        db_column='systemowy', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = 'slownik_rodzaje'


"""
db_table = 'slownik_kategorie'
"""


class DictCategory(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    type = models.ForeignKey(DictType, on_delete=models.SET_NULL,
                             db_column='id_rodzaju', blank=True, null=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_system = models.IntegerField(
        db_column='systemowy', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'slownik_kategorie'


"""
db_table = 'slownik_marki'
"""


class DictBrand(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    group = models.ForeignKey(
        DictGroup, on_delete=models.SET_NULL, db_column='id_grupy', blank=True, null=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_system = models.IntegerField(
        db_column='systemowy', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'slownik_marki'


"""
db_table = 'slownik_modele'
"""


class DictModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    brand = models.ForeignKey(
        DictBrand, on_delete=models.SET_NULL, db_column='id_marki', blank=True, null=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_system = models.IntegerField(
        db_column='systemowy', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'slownik_modele'


"""
db_table = 'slownik_rodzaje_paliwa'
"""


class DictTypeOfFuel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_system = models.IntegerField(
        db_column='systemowy', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'slownik_rodzaje_paliwa'


"""
db_table = 'slownik_typy'
"""


class DictTrailerType(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        DictCategory, on_delete=models.SET_NULL, db_column='id_kategorii', blank=True, null=True)
    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_system = models.IntegerField(
        db_column='systemowy', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'slownik_typy'


"""
db_table = 'maszyny'
"""


class Item(models.Model):
    # import_field = models.IntegerField(db_column='vin',db_column='import', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    # import_dostawca = models.CharField(db_column='vin',max_length=20, blank=True, null=True)
    # import_id = models.IntegerField(db_column='vin',blank=True, null=True)

    is_active = models.IntegerField(db_column='aktywny', blank=True, null=True)
    is_auction = models.IntegerField(db_column='aukcja', blank=True, null=True)
    price = models.DecimalField(
        db_column='cena', max_digits=10, decimal_places=2, blank=True, null=True
    )
    identificator = models.CharField(
        db_column='identyfikator', max_length=12, blank=True, null=True)
    group = models.ForeignKey(
        DictGroup, on_delete=models.SET_NULL, db_column='id_grupy', blank=True, null=True)
    category = models.ForeignKey(
        DictCategory, on_delete=models.SET_NULL, db_column='id_kategorii', blank=True, null=True)
    brand = models.ForeignKey(
        DictBrand, on_delete=models.SET_NULL, db_column='id_marki', blank=True, null=True)
    model = models.ForeignKey(
        DictModel, on_delete=models.SET_NULL, db_column='id_modelu', blank=True, null=True)
    type = models.ForeignKey(DictType, on_delete=models.SET_NULL,
                             db_column='id_rodzaju', blank=True, null=True)
    fuel = models.ForeignKey(DictTypeOfFuel, on_delete=models.SET_NULL,
                             db_column='id_rodzaju_paliwa', blank=True, null=True)
    trailer_type = models.ForeignKey(
        DictTrailerType, on_delete=models.SET_NULL, db_column='id_typu', blank=True, null=True)
    name = models.CharField(
        db_column='nazwa', max_length=200, blank=True, null=True)
    description = models.TextField(db_column='opis', blank=True, null=True)
    date_updates = models.DateTimeField(
        db_column='ostatnia_modyfikacja', blank=True, null=True)
    id = models.AutoField(db_column='id', primary_key=True)
    promotion = models.IntegerField(
        db_column='promocja', blank=True, null=True)
    year_production = models.IntegerField(
        db_column='rok_produkcji', blank=True, null=True)
    is_sold = models.IntegerField(db_column='sprzedany', blank=True, null=True)
    slug = models.SlugField(db_column='slug')
    discount_price = models.FloatField(db_column='discount_price')

    def get_absolute_url(self):
        return reverse("supercar:item-detail", kwargs={
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        param = 'Oferta,' + str(self.id) + ',' + self.name
        param = param.replace(' ', '_')
        param = param.replace('-', '_')
        param = param.replace('__', '_')
        param = param.replace('/', '_')
        self.slug = slugify(param, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_add_to_cart_url(self):
        return reverse('supercar:add-to-cart', kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse('supercar:remove-from-cart', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'maszyny'
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def __str__(self):
        return self.item.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(
        db_column='start_date', auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def get_total(self):
        total = 0
        for order_item in self.item.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

    def __str__(self):
        return self.user.username


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

customized_sitetree_models = False

if customized_sitetree_models:

    from sitetree.models import TreeItemBase, TreeBase

    class Tree(TreeBase):

        custom_field = models.CharField(
            'Custom tree field', max_length=50, null=True, blank=True)

    class TreeItem(TreeItemBase):

        custom_field = models.IntegerField('Custom item field', default=42)
