from django.contrib import admin
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class RelationshipInline(admin.TabularInline):
    model = Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_is_main = {}
        for form in self.forms:
            
            if form.cleaned_data['is_main']:
                if count_is_main:
                    raise ValidationError('Выберете только 1 главную тематику')
                count_is_main['is_main'] = True
            if not form.cleaned_data['is_main']:
                raise ValidationError('Укажите главную тематику')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass