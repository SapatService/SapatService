from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import *


# Форма для модели AboutUs с валидацией
class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'

    def clean(self):
        # Проверка на существование единственной записи
        if not self.instance.pk and AboutUs.objects.exists():
            raise ValidationError("Запись уже существует. Новая запись не будет добавлена.")
        return super().clean()

# Inline для добавления изображений
class AboutUsImageInline(admin.TabularInline):
    model = ImageAboutUs
    extra = 1  # Количество пустых полей для изображений по умолчанию
    fields = ['image']

# Админ-панель для AboutUs с инлайном для изображений и кастомной логикой
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsForm
    inlines = [AboutUsImageInline]  # Добавляем inline для изображений

    def response_add(self, request, obj, post_url_continue=None):
        if AboutUs.objects.count() > 1:
            self.message_user(request, "Запись уже существует. Новая запись не будет добавлена.", level='error')
            return self._get_add_response(request, obj, 'Новая запись не сохранена.')
        return super().response_add(request, obj, post_url_continue)

    def _get_add_response(self, request, obj, message):
        opts = self.model._meta
        post_url_continue = request.path
        self.message_user(request, message, level='error')
        return self.render_change_form(
            request,
            context=self.get_change_form_initial_data(request),
            obj=obj,
            change=False,
            add=True,
            form_url=post_url_continue,
            opts=opts
        )

    def response_change(self, request, obj):
        if AboutUs.objects.count() > 1:
            self.message_user(request, "Запись уже существует. Новая запись не будет добавлена.", level='error')
            return self._get_add_response(request, obj, 'Новая запись не сохранена.')
        return super().response_change(request, obj)

class AboutOurExperienceForm(forms.ModelForm):
    class Meta:
        model = AboutOurExperience
        fields = '__all__'

    def clean(self):
        if not self.instance.pk and AboutOurExperience.objects.exists():
            raise ValidationError("Запись уже существует. Новая запись не будет добавлена.")
        return super().clean()

class AboutOurExperienceAdmin(admin.ModelAdmin):
    form = AboutOurExperienceForm

    def response_add(self, request, obj, post_url_continue=None):
        if AboutOurExperience.objects.count() > 1:
            self.message_user(request, "Запись уже существует. Новая запись не будет добавлена.", level='error')
            return self._get_add_response(request, obj, 'Новая запись не сохранена.')
        return super().response_add(request, obj, post_url_continue)

    def _get_add_response(self, request, obj, message):
        opts = self.model._meta
        post_url_continue = request.path
        self.message_user(request, message, level='error')
        return self.render_change_form(
            request,
            context=self.get_change_form_initial_data(request),
            obj=obj,
            change=False,
            add=True,
            form_url=post_url_continue,
            opts=opts
        )

    def response_change(self, request, obj):
        if AboutOurExperience.objects.count() > 1:
            self.message_user(request, "Запись уже существует. Новая запись не будет добавлена.", level='error')
            return self._get_add_response(request, obj, 'Новая запись не сохранена.')
        return super().response_change(request, obj)


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(AboutOurExperience, AboutOurExperienceAdmin)
