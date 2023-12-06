from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    name = models.CharField(_("product"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    image = models.URLField(_("image"), max_length=200)
    desc = models.TextField(_("desc"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
