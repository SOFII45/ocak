from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Project(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Planlama'),
        ('active', 'Aktif'),
        ('completed', 'Tamamlandı'),
        ('on-hold', 'Beklemede'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    description = models.TextField(verbose_name="Açıklama")
    short_description = models.CharField(max_length=500, blank=True, null=True, verbose_name="Kısa Açıklama")
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'gif'])],
        verbose_name="Proje Görseli"
    )
    # Yeni eklenen link alanı
    project_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Proje Linki (İncele)")
    
    start_date = models.DateField(blank=True, null=True, verbose_name="Başlangıç Tarihi")
    end_date = models.DateField(blank=True, null=True, verbose_name="Bitiş Tarihi")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='planning', verbose_name="Durum")
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Bütçe")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Konum")
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projects', verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_active', 'status']),
            models.Index(fields=['start_date']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title