from django.db import models
from django.utils.translation import gettext_lazy as _


class OurService(models.Model):
    title = models.CharField(max_length=34, verbose_name=_("Название"))
    ImageOurService = models.ImageField(upload_to='ImageOurService/', verbose_name=_("Изображение услуги"))

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")

    def __str__(self) -> str:
        return self.title


class OurServiceDetail(models.Model):
    our_service = models.ForeignKey(OurService, on_delete=models.CASCADE, verbose_name=_("Услуга"))
    title = models.CharField(max_length=34, verbose_name=_("Название детали"))
    ImageDetailOurService = models.ImageField(upload_to='ImageOurService/', verbose_name=_("Изображение детали услуги"))

    class Meta:
        verbose_name = _("Деталь услуги")
        verbose_name_plural = _("Детали услуг")

    def __str__(self) -> str:
        return self.title


class OurServicePrice(models.Model):
    our_service = models.ForeignKey(OurServiceDetail, on_delete=models.CASCADE, verbose_name=_("Деталь услуги"))
    price = models.PositiveBigIntegerField(verbose_name=_("Цена"))
    contact = models.TextField(verbose_name=_("Контактная информация"))

    class Meta:
        verbose_name = _("Цена услуги")
        verbose_name_plural = _("Цены услуг")

    def __str__(self) -> str:
        return f'{self.our_service.our_service.title} - {self.price}'
