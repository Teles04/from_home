from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Teg, MainArticleChoice, Article


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            data_dict = form.cleaned_data
            if data_dict.get('main_article') is True:
                i += 1
            if i > 1:
                raise ValidationError('Используйте только один основной тег')
        return super().clean()

class ChoiceInline(admin.TabularInline):
    model = MainArticleChoice
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

@admin.register(Teg)
class TegAdmin(admin.ModelAdmin):
    pass