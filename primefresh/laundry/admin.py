from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Testimonial, GalleryItem, Booking, ContactMessage, SiteStat


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_from', 'price_unit', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'description')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'location', 'date', 'is_featured')
    list_editable = ('is_featured',)
    list_filter = ('rating', 'is_featured')
    search_fields = ('client_name', 'review')


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'order', 'thumbnail')
    list_editable = ('is_active', 'order')
    list_filter = ('category', 'is_active')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover;border-radius:4px;" />', obj.image.url)
        return '—'
    thumbnail.short_description = 'Preview'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'service_type', 'preferred_date',
                    'preferred_slot', 'status', 'quoted_price', 'created_at')
    list_filter = ('status', 'service_type', 'preferred_slot', 'needs_pickup', 'needs_delivery')
    search_fields = ('full_name', 'email', 'phone', 'address')
    list_editable = ('status', 'quoted_price')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Customer Information', {
            'fields': ('full_name', 'email', 'phone', 'address')
        }),
        ('Booking Details', {
            'fields': ('service_type', 'preferred_date', 'preferred_slot',
                       'estimated_items', 'needs_pickup', 'needs_delivery', 'special_instructions')
        }),
        ('Admin', {
            'fields': ('status', 'quoted_price', 'admin_notes', 'created_at', 'updated_at')
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read',)
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)


@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'icon', 'order')
    list_editable = ('value', 'order')


# Customize admin site
admin.site.site_header = 'PrimeFresh Admin'
admin.site.site_title = 'PrimeFresh Management'
admin.site.index_title = 'Dashboard'
