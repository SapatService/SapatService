from django.core.exceptions import ValidationError
from django.db import models


class AboutUs(models.Model):
    description = models.TextField(verbose_name="Описание")
#    first_image = models.ImageField(upload_to='ImageAboutUs/', verbose_name="Изображение")
    # second_image = models.ImageField(upload_to='ImageAboutUs/', verbose_name="Изображение", blank=True, null=True)
    # third_image = models.ImageField(upload_to='ImageAboutUs/', verbose_name="Изображение", blank=True, null=True)
    # fourth_image = models.ImageField(upload_to='ImageAboutUs/', verbose_name="Изображение", blank=True, null=True)
    # fifth_image = models.ImageField(upload_to='ImageAboutUs/', verbose_name="Изображение", blank=True, null=True)
    # sixth_image = models.ImageField(upload_to='ImageAboutUs/', verbose_name="Изображение", blank=True, null=True)

    def clean(self):
        if AboutUs.objects.exists() and not self.pk:
            raise ValidationError("Можно добавить только одну запись в модель 'О нас'")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self) -> str:
        return 'О нас'

class ImageAboutUs(models.Model):
    about_us = models.ForeignKey(AboutUs, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='AbouUsImages/')

    def __str__(self) -> str:
        return "Поле для Изображения 'О нас'"


class AboutOurExperience(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
#    image_about = models.ImageField(upload_to='AboutOurExperience/', verbose_name="фото фона")
    main_description = models.TextField(verbose_name="Описание")

    first_cart_title = models.CharField(max_length=15, verbose_name="Заголовок первой карточки")
    first_cart_description = models.TextField(verbose_name="Описание первой карточки")

    second_cart_title = models.CharField(max_length=15, verbose_name="Заголовок второй карточки")
    second_cart_description = models.TextField(verbose_name="Описание второй карточки")

    third_cart_title = models.CharField(max_length=15, verbose_name="Заголовок третьей карточки")
    third_cart_description = models.TextField(verbose_name="Описание третьей карточки")

    def clean(self):
        if AboutOurExperience.objects.exists() and not self.pk:
            raise ValidationError("Можно добавить только одну запись в модель 'О нас и о нашем опыте'")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "О нас и о нашем опыте"
        verbose_name_plural = "О нас и о нашем опыте"

    def __str__(self) -> str:
        return 'О нас и о нашем опыте'

