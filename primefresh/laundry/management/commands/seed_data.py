"""
Management command to populate the database with sample data.
Run: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from laundry.models import Service, Testimonial, SiteStat


class Command(BaseCommand):
    help = 'Seeds the database with initial sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # --- Site Stats ---
        stats = [
            ('Happy Clients', '500+', '😊', 1),
            ('Items Cleaned', '5,000+', '👕', 2),
            ('Satisfaction Rate', '98%', '⭐', 3),
            ('Quick Turnaround', '24hr', '⚡', 4),
        ]
        for label, value, icon, order in stats:
            SiteStat.objects.get_or_create(label=label, defaults={'value': value, 'icon': icon, 'order': order})

        # --- Services ---
        services_data = [
            # (name, category, description, price_from, price_unit, is_featured, order)
            ('Laundry & Ironing', 'laundry', 'Complete washing, drying, and ironing of all garment types. Each item is handled with expert care for a perfectly crisp, fresh finish every time.', 500, 'per item', True, 1),
            ('Dry Cleaning', 'laundry', 'Professional solvent-based cleaning for delicate and special-care fabrics — suits, evening gowns, silk, wool, cashmere, and more.', 2000, 'per item', True, 2),
            ('Garment Alteration & Repairs', 'laundry', 'Expert tailoring and garment repairs including hemming, resizing, zipper replacement, button sewing, and general stitching work.', 1500, 'per item', True, 3),
            ('Home Deep Cleaning', 'cleaning', 'Intensive whole-home cleaning covering every corner and surface — ideal for move-in/move-out situations or thorough seasonal cleaning.', 25000, 'per session', True, 4),
            ('Post Construction Cleaning', 'cleaning', 'Thorough professional cleanup after renovation or construction — removing dust, paint splatter, debris, grout, and building residue.', 30000, 'per session', True, 5),
            ('Industrial Cleaning', 'cleaning', 'Heavy-duty commercial cleaning solutions for offices, warehouses, factories, and large-scale facilities requiring specialist equipment.', 50000, 'per session', False, 6),
            ('Fumigation', 'specialty', 'Safe and effective fumigation services for homes and businesses. Targeting pests at the source for a fully pest-free environment.', 15000, 'per session', False, 7),
            ('Pickup & Delivery', 'laundry', 'Complimentary door-to-door pickup and delivery on every order. We come to you, handle everything with care, and bring your items back fresh.', None, '', False, 8),
        ]
        for name, cat, desc, price, unit, featured, order in services_data:
            Service.objects.get_or_create(name=name, defaults={
                'category': cat, 'description': desc,
                'price_from': price, 'price_unit': unit,
                'is_featured': featured, 'order': order,
            })

        # --- Testimonials ---
        testimonials = [
            ('Amara Okonkwo', 'Wuse II, Abuja', 5, 'PrimeFresh is absolutely incredible! My suits came back perfectly pressed and smelling amazing. The free pickup made it so convenient — I didn\'t have to leave my house at all.', True),
            ('Chidi Nwosu', 'Gwarinpa, Abuja', 5, 'I booked for home deep cleaning before my family visit. The team was thorough, professional, and so polite. Every corner was spotless. Highly recommended!', True),
            ('Fatima Aliyu', 'Garki, Abuja', 5, 'I was a bit skeptical at first but wow — my white shirts have never looked this pristine. They even fixed a missing button without being asked. True professionals!', True),
            ('Emmanuel Bello', 'Maitama, Abuja', 5, 'Super fast service and very affordable pricing. They picked up in the morning and delivered by evening. This is now my go-to laundry service in Abuja!', True),
            ('Ngozi Kalu', 'Life Camp, Abuja', 5, 'The dry cleaning on my wedding outfit was done absolutely beautifully. Delicate fabrics handled with so much care and expertise. Thank you PrimeFresh!', True),
            ('Tunde Makinde', 'Kubwa, Abuja', 5, 'Best laundry service in Abuja by a wide margin. Always professional, always punctual, and the clothes always come back wonderfully fresh and neatly folded.', True),
        ]
        for name, loc, rating, review, featured in testimonials:
            Testimonial.objects.get_or_create(client_name=name, defaults={
                'location': loc, 'rating': rating,
                'review': review, 'is_featured': featured,
            })

        self.stdout.write(self.style.SUCCESS(
            f'✅ Seeded {SiteStat.objects.count()} stats, '
            f'{Service.objects.count()} services, '
            f'{Testimonial.objects.count()} testimonials.'
        ))
        self.stdout.write(self.style.WARNING(
            '\nNext: python manage.py createsuperuser\n'
            'Then visit /admin to manage your content and upload gallery images.'
        ))
