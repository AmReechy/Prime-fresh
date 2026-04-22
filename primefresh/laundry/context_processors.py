def global_context(request):
    """Inject global context into all templates."""
    return {
        'nav_links': [
            ('Home', 'home'),
            ('Services', 'services'),
            ('Gallery', 'gallery'),
            ('Booking', 'booking'),
            ('Contact', 'contact'),
        ],
        'footer_services': [
            'Laundry & Ironing',
            'Dry Cleaning',
            'Garment Alteration & Repairs',
            'Industrial Cleaning',
            'Post Construction Cleaning',
            'Fumigation',
            'Home Deep Cleaning',
            'Pickup & Delivery',
        ],
        'site_phone': '090 7380 8333',
        'site_whatsapp': '2349073808333',
        'site_email': 'info@primefreshlaundry.com',
        'site_instagram': 'primefreshlaundry',
        'site_website': 'www.primefreshlaundry.com',
        'site_address': 'NAF Officers Quarters Hajia Estate, After Mint and Print, Adjacent Abattoir, Garki II, FCT, Nigeria.',
    }
