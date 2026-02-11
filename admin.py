from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Listede project_link de görünsün
    list_display = ['title', 'status', 'start_date', 'project_link', 'is_active', 'image_preview']
    list_filter = ['is_active', 'status', 'start_date', 'location']
    search_fields = ['title', 'description', 'short_description', 'location']
    list_editable = ['status', 'is_active']
    readonly_fields = ['image_preview', 'created_by', 'created_at', 'updated_at']
    date_hierarchy = 'start_date'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Proje Bilgileri', {
            'fields': ('title', 'short_description', 'description')
        }),
        ('Medya', {
            'fields': ('image', 'image_preview')
        }),
        ('Proje Detayları', {
            'fields': ('project_link', 'start_date', 'end_date', 'status', 'budget', 'location')
        }),
        ('Ayarlar', {
            'fields': ('is_active',)
        }),
        ('Sistem Bilgileri', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['activate_items', 'deactivate_items']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />', obj.image.url)
        return "Görsel Yok"
    image_preview.short_description = 'Görsel Önizleme'

    def activate_items(self, request, queryset):
        queryset.update(is_active=True)
    activate_items.short_description = 'Seçili projeleri aktif et'

    def deactivate_items(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_items.short_description = 'Seçili projeleri pasif et'