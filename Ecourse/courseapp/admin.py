from django.contrib import admin
from .models import Category, Course, Lesson
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active', 'course']
    search_fields = ['name', 'id', 'active']
    list_filter = ['name', 'created_date']
    forms = LessonForm


class CourseAdmin(admin.ModelAdmin):
    # list_display = ['id', 'subject', 'active', 'avatar']
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/course/{obj.image.name}" width="120" />'
            )

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)