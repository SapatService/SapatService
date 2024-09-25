from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    first_name = models.CharField(max_length=18, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=18, blank=True, null=True, verbose_name=_("Фамилия"))
    stars = models.CharField(
        max_length=1, 
        choices=[(str(star), str(star)) for star in range(6)], 
        default='0', 
        verbose_name=_("Оценка")
    )
    text = models.TextField(verbose_name=_("Отзыв"))
    image = models.ImageField(upload_to="ImageReviewer/", verbose_name=_("Фото пользователя"))

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - оценка: {self.stars}'


class OurTeam(models.Model):
    first_name = models.CharField(max_length=18, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=18, blank=True, null=True, verbose_name=_("Фамилия"))
    role = models.CharField(max_length=16, verbose_name=_("Роль"))
    image = models.ImageField(upload_to='OurTeamImage/', verbose_name=_("Фото"))

    class Meta:
        verbose_name = _("Член команды")
        verbose_name_plural = _("Наша команда")

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name} - {self.role}'


class GeoLocate(models.Model):
    map_image = models.ImageField(upload_to='MapImage/', verbose_name=_("Карта"))
    locate = models.TextField(verbose_name=_("Локация"))
    working_hours = models.TextField(verbose_name=_("Часы работы"))
    map_url = models.TextField(verbose_name=("Ссылка на местоположения"))

    class Meta:
        verbose_name = _("Геолокация")
        verbose_name_plural = _("Геолокации")

    def __str__(self) -> str:
        return 'Геолокация'


class WhatsApp(models.Model):
    url = models.TextField(verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("WhatsApp")
        verbose_name_plural = _("WhatsApp")

    def __str__(self) -> str:
        return self.url


class Instagram(models.Model):
    url = models.TextField(verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Instagram")
        verbose_name_plural = _("Instagram")

    def __str__(self) -> str:
        return self.url


class Telegram(models.Model):
    url = models.TextField(verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Telegram")
        verbose_name_plural = _("Telegram")

    def __str__(self) -> str:
        return self.url


class TikTok(models.Model):
    url = models.TextField(verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("TikTok")
        verbose_name_plural = _("TikTok")

    def __str__(self) -> str:
        return self.url
