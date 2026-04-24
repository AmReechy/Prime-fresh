from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Testimonial, GalleryItem, SiteStat
from .forms import BookingForm, ContactForm

 
HOW_IT_WORKS = [
    ('Book Online', 'Fill out our simple booking form with your service needs and preferred pickup time — takes under 2 minutes.'),
    ('We Pickup', 'Our friendly team comes to your doorstep to collect your laundry — free of charge, on your schedule.'),
    ('Expert Care', 'Your clothes are treated with professional care using quality detergents and well-maintained equipment.'),
    ('Fresh Delivery', 'Clean, fresh, and neatly folded — delivered right back to your door, right on time.'),
]

WHY_US = [
    {'icon': 'M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4', 'title': 'Free Pickup & Delivery', 'desc': 'We come to you — anywhere in Abuja. No transportation hassle, no extra cost, just pure convenience.'},
    {'icon': 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z', 'title': 'Expert Fabric Care', 'desc': 'Each garment type is treated differently. We know exactly what your fabrics need for the best results.'},
    {'icon': 'M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z', 'title': 'Fast 24–48hr Turnaround', 'desc': 'Most orders are ready within 24–48 hours. Express same-day service is available for urgent needs.'},
    {'icon': 'M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z', 'title': 'Affordable Rates', 'desc': "Quality laundry care shouldn't break the bank. Our pricing is transparent, fair, and competitive."},
]

PLACEHOLDER_TESTIMONIALS = [
    ('Amara O.', 'Wuse II, Abuja', 'PrimeFresh is absolutely incredible! My suits came back perfectly pressed and smelling amazing. The free pickup made it so convenient.'),
    ('Chidi N.', 'Gwarinpa, Abuja', 'I booked for home deep cleaning before my family visit. The team was thorough, professional, and so polite. Highly recommended!'),
    ('Fatima A.', 'Garki, Abuja', 'I was skeptical at first but wow — my white shirts have never looked this clean. They even fixed a missing button without being asked!'),
    ('Emmanuel B.', 'Maitama, Abuja', 'Super fast service and very affordable. They picked up in the morning and delivered by evening. Will definitely use again!'),
    ('Ngozi K.', 'Life Camp, Abuja', 'The dry cleaning on my wedding outfit was done beautifully. Delicate fabrics handled with so much care. Thank you PrimeFresh!'),
    ('Tunde M.', 'Kubwa, Abuja', 'Best laundry service in Abuja by far. Professional, punctual, and the clothes always smell wonderfully fresh.'),
]

PLACEHOLDER_SERVICES = [
    {'emoji': '👕', 'bg': 'bg-blue-50', 'name': 'Laundry & Ironing', 'desc': 'Complete washing, drying, and ironing of all garment types. Each item handled with care for a crisp, fresh finish.'},
    {'emoji': '🧴', 'bg': 'bg-purple-50', 'name': 'Dry Cleaning', 'desc': 'Professional solvent-based cleaning for delicate fabrics — suits, evening gowns, silk, wool, and more.'},
    {'emoji': '✂️', 'bg': 'bg-red-50', 'name': 'Garment Alteration & Repairs', 'desc': 'Expert tailoring and repairs including hemming, resizing, zipper replacement, and stitching.'},
    {'emoji': '🏭', 'bg': 'bg-orange-50', 'name': 'Industrial Cleaning', 'desc': 'Heavy-duty cleaning solutions for commercial spaces, warehouses, offices, and large-scale facilities.'},
    {'emoji': '🏗️', 'bg': 'bg-yellow-50', 'name': 'Post Construction Cleaning', 'desc': 'Thorough cleanup after renovation or construction — removing dust, paint splatter, debris, and grout.'},
    {'emoji': '🌿', 'bg': 'bg-green-50', 'name': 'Fumigation', 'desc': 'Safe and effective fumigation services for homes and businesses to ensure a pest-free environment.'},
    {'emoji': '🏠', 'bg': 'bg-teal-50', 'name': 'Home Deep Cleaning', 'desc': 'Intensive whole-home cleaning covering every corner — ideal for move-in/move-out or seasonal cleaning.'},
    {'emoji': '🚚', 'bg': 'bg-sky-50', 'name': 'Pickup & Delivery', 'desc': 'Complimentary door-to-door pickup and delivery. We come to you, handle everything, and bring it back fresh.'},
]


def home(request):
    featured_services = Service.objects.filter(is_featured=True, is_active=True)#[:6]
    testimonials = list(Testimonial.objects.filter(is_featured=True)[:6])
    stats = SiteStat.objects.all()
    gallery_highlights = GalleryItem.objects.filter(is_active=True)[:6]
    context = {
        'featured_services': featured_services,
        'testimonials': testimonials,
        'stats': stats,
        'gallery_highlights': gallery_highlights,
        'page': 'home',
        'why_us': WHY_US,
        'placeholder_testimonials': PLACEHOLDER_TESTIMONIALS,
        'how_it_works': HOW_IT_WORKS,
    }
    print(featured_services)
    return render(request, 'laundry/home.html', context)


def services(request):
    all_services = Service.objects.filter(is_active=True)
    laundry_services = all_services.filter(category='laundry')
    cleaning_services = all_services.filter(category='cleaning')
    specialty_services = all_services.filter(category='specialty')
    context = {
        'laundry_services': laundry_services,
        'cleaning_services': cleaning_services,
        'specialty_services': specialty_services,
        'all_services': all_services,
        'page': 'services',
        'placeholder_services': PLACEHOLDER_SERVICES,
    }
    return render(request, 'laundry/services.html', context)


def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_obj = form.save()
            messages.success(request, f"Booking confirmed! We'll call you shortly to confirm pickup. Reference: #PF{booking_obj.pk:04d}")
            return redirect('booking_success', pk=booking_obj.pk)
        else:
            messages.error(request, 'Please correct the errors below and try again.')
    return render(request, 'laundry/booking.html', {'form': form, 'page': 'booking'})


def booking_success(request, pk):
    return render(request, 'laundry/booking_success.html', {'booking_id': f'PF{pk:04d}', 'page': 'booking'})


def gallery(request):
    category_filter = request.GET.get('category', 'all')
    items = GalleryItem.objects.filter(is_active=True)
    if category_filter != 'all':
        items = items.filter(category=category_filter)
    return render(request, 'laundry/gallery.html', {
        'items': items,
        'categories': GalleryItem.CATEGORY_CHOICES,
        'active_category': category_filter,
        'page': 'gallery',
    })


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for reaching out! We'll get back to you within 24 hours.")
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields correctly.')
    return render(request, 'laundry/contact.html', {'form': form, 'page': 'contact'})
