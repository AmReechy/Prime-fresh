from django.db import models
from django.utils import timezone


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('laundry', 'Laundry'),
        ('cleaning', 'Cleaning'),
        ('specialty', 'Specialty'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='laundry')
    description = models.TextField()
    price_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_unit = models.CharField(max_length=50, default='per item', blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text='Heroicon or emoji name')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_photo = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=5)
    review = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    date = models.DateField(default=timezone.now)
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']

    def __str__(self):
        return f"{self.client_name} - {self.rating}★"


class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('before_after', 'Before & After'),
        ('workspace', 'Our Workspace'),
        ('team', 'Our Team'),
        ('equipment', 'Equipment'),
    ]
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='workspace')
    image = models.ImageField(upload_to='gallery/')
    before_image = models.ImageField(upload_to='gallery/before/', null=True, blank=True,
                                     help_text='For before/after items')
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('ready', 'Ready for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    SERVICE_TYPE_CHOICES = [
        ('laundry_ironing', 'Laundry & Ironing'),
        ('dry_cleaning', 'Dry Cleaning'),
        ('garment_alteration', 'Garment Alteration & Repairs'),
        ('industrial_cleaning', 'Industrial Cleaning'),
        ('post_construction', 'Post Construction Cleaning'),
        ('fumigation', 'Fumigation'),
        ('home_deep_cleaning', 'Home Deep Cleaning'),
        ('pickup_delivery', 'Pickup & Delivery Only'),
    ]
    PICKUP_SLOT_CHOICES = [
        ('morning', 'Morning (8AM – 12PM)'),
        ('afternoon', 'Afternoon (12PM – 4PM)'),
        ('evening', 'Evening (4PM – 7PM)'),
    ]

    # Customer info
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(help_text='Pickup address')

    # Booking details
    service_type = models.CharField(max_length=30, choices=SERVICE_TYPE_CHOICES)
    preferred_date = models.DateField()
    preferred_slot = models.CharField(max_length=20, choices=PICKUP_SLOT_CHOICES)
    special_instructions = models.TextField(blank=True)
    needs_pickup = models.BooleanField(default=True, verbose_name='Free Pickup Required')
    needs_delivery = models.BooleanField(default=True, verbose_name='Free Delivery Required')
    estimated_items = models.PositiveIntegerField(null=True, blank=True,
                                                   help_text='Approximate number of items/bags')

    # Admin fields
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    quoted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"#{self.pk} - {self.full_name} ({self.get_service_type_display()}) - {self.status}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} – {self.subject}"


class SiteStat(models.Model):
    """Editable homepage stats like satisfaction rate, items cleaned, etc."""
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50, help_text='e.g. 98%, 5000+, 3 Years')
    icon = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.label}: {self.value}"
