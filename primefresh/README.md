# PrimeFresh – Laundry & General Cleaning Services Website

A full-featured Django website for PrimeFresh Laundry & General Cleaning Services, built with Django templates, vanilla JavaScript, and Tailwind CSS (CDN).

---

## 🗂 Project Structure

```
primefresh/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3                    ← created after migrations
├── media/                        ← uploaded images (created automatically)
├── primefresh_site/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── laundry/                      ← main app
    ├── __init__.py
    ├── admin.py                  ← fully configured admin panel
    ├── context_processors.py     ← global nav/footer data
    ├── forms.py                  ← BookingForm, ContactForm
    ├── models.py                 ← Service, Testimonial, GalleryItem, Booking, ContactMessage, SiteStat
    ├── urls.py
    ├── views.py
    ├── migrations/
    ├── management/
    │   └── commands/
    │       └── seed_data.py      ← python manage.py seed_data
    └── templates/laundry/
        ├── base.html             ← navbar, footer, WhatsApp button, global styles
        ├── home.html             ← hero, stats, how-it-works, services, why-us, testimonials, CTA
        ├── services.html         ← full services listing by category
        ├── booking.html          ← 3-step multi-step booking form
        ├── booking_success.html  ← confirmation page
        ├── gallery.html          ← filterable masonry gallery + lightbox
        └── contact.html          ← contact form + social links + map placeholder
```

---

## 🚀 Quick Setup

### 1. Create a virtual environment

```bash
cd primefresh
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed sample data (services, stats, testimonials)

```bash
python manage.py seed_data
```

### 5. Create an admin superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## 🔑 Admin Panel

Visit **http://127.0.0.1:8000/admin/** and log in with your superuser credentials.

You can manage:

| Section | What you can do |
|---|---|
| **Services** | Add/edit services, set prices, mark as featured, reorder |
| **Testimonials** | Add client reviews, upload photos, set ratings |
| **Gallery Items** | Upload before/after photos, workspace images, categorize |
| **Bookings** | View all bookings, update status, add notes, set quoted price |
| **Contact Messages** | Read messages from the contact form, mark as read |
| **Site Stats** | Edit homepage stats (satisfaction rate, items cleaned, etc.) |

---

## 📄 Pages

| URL | Page |
|---|---|
| `/` | Home – animated hero, stats, services, testimonials, CTA |
| `/services/` | Full services listing, categorised |
| `/booking/` | 3-step booking form with free pickup & delivery |
| `/gallery/` | Filterable masonry photo gallery with lightbox |
| `/contact/` | Contact form + social links + working hours + map |
| `/admin/` | Django admin panel (superuser only) |

---

## 🎨 Design Features

- **Fonts**: Syne (display/headings) + DM Sans (body) — loaded from Google Fonts
- **Colors**: Brand blue (`#1463d9`) + gold accents (`#f59e0b`) on light blue backgrounds
- **Animations**: Scroll-reveal, hero fade-in, auto-scrolling testimonial carousel, floating WhatsApp button
- **Components**: Sticky navbar with scroll effect, mobile hamburger menu, multi-step booking form, gallery lightbox, toast notifications
- **Extras**: WhatsApp floating chat button, booking reference numbers, admin-editable content

---

## 🛠 Customisation Guide

### Replace placeholder images

Images are currently placeholder boxes. To replace them:

1. Go to `/admin/` → **Gallery Items** → upload your photos
2. For the hero and "why us" images: edit `home.html` and replace the placeholder `<div>` blocks with `<img>` tags pointing to your uploaded media

### Update contact details

All contact details (phone, email, address, social links) appear in multiple places. Search and replace across templates, or better — update `laundry/context_processors.py` which injects global values.

### Add a real Google Map

In `contact.html`, find the comment `<!-- Embed Google Maps here -->` and replace the placeholder div with your Google Maps `<iframe>` embed code.

### Email notifications for bookings

In `primefresh_site/settings.py`, update the email settings section:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

Then add email sending logic to `views.py` in the `booking()` function after `form.save()`.

### Production deployment

For production, also:

1. Change `SECRET_KEY` to a secure random string
2. Set `DEBUG = False`
3. Add your domain to `ALLOWED_HOSTS`
4. Run `python manage.py collectstatic`
5. Serve static files with WhiteNoise (already in `requirements.txt`) or Nginx
6. Use PostgreSQL instead of SQLite

---

## 📦 Tech Stack

- **Backend**: Django 4.2+
- **Templates**: Django Template Language (DTL)
- **Styling**: Tailwind CSS (CDN) + custom CSS
- **JavaScript**: Vanilla JS (no framework)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Images**: Pillow + Django Media Files
- **Fonts**: Google Fonts (Syne + DM Sans)
- **Icons**: Inline SVG (Heroicons style)
