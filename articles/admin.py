from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from articles.models import Article, PositionTag, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count != 1:
            raise ValidationError(f'У Вас количество основных тегов равно {count}, а должно Один ')
        else:
            return super().clean()


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ['id', 'tag', ]


class InlinePositionTag(admin.TabularInline):
    model = PositionTag
    fields = ['is_main', 'tag']
    formset = RelationshipInlineFormset


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    inlines = [InlinePositionTag, ]
    list_display = ['id', 'title', 'published_at']
