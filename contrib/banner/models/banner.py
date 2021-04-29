from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from .category import Category


class Banner(models.Model):
    image = models.ImageField(_("Image"), upload_to='banners/images/%Y/%m/%d/')
    url = models.URLField(_("URL"))
    name = models.CharField(_("Name"), max_length=150)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    published = models.DateTimeField(_("Published"), default=now)
    expired = models.DateTimeField(_("Expired"), null=True, blank=True)

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")
        ordering = ("-published", "-expired")

    def __str__(self):
        return self.name