from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from decimal import Decimal
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        # Create sample users
        self.stdout.write('Creating users...')
        users = []
        user_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
            {'username': 'bob_wilson', 'email': 'bob@example.com', 'first_name': 'Bob', 'last_name': 'Wilson'},
            {'username': 'alice_brown', 'email': 'alice@example.com', 'first_name': 'Alice', 'last_name': 'Brown'},
            {'username': 'charlie_davis', 'email': 'charlie@example.com', 'first_name': 'Charlie', 'last_name': 'Davis'},
        ]

        for data in user_data:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password='password123'
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'  Created user: {user.username}'))

        # Create sample listings
        self.stdout.write('Creating listings...')
        listings = []
        listing_data = [
            {
                'title': 'Cozy Beach House',
                'description': 'Beautiful beach house with stunning ocean views.',
                'location': 'Malibu, California',
                'price_per_night': Decimal('250.00')
            },
            {
                'title': 'Modern Downtown Apartment',
                'description': 'Stylish apartment in the heart of the city.',
                'location': 'New York, NY',
                'price_per_night': Decimal('180.00')
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Secluded cabin in the mountains.',
                'location': 'Aspen, Colorado',
                'price_per_night': Decimal('300.00')
            },
            {
                'title': 'Luxury Villa with Pool',
                'description': 'Spacious villa with private pool.',
                'location': 'Miami, Florida',
                'price_per_night': Decimal('450.00')
            },
            {
                'title': 'Charming Country Cottage',
                'description': 'Quaint cottage in the countryside.',
                'location': 'Vermont',
                'price_per_night': Decimal('150.00')
            },
        ]

        for data in listing_data:
            listing = Listing.objects.create(
                host=random.choice(users),
                title=data['title'],
                description=data['description'],
                location=data['location'],
                price_per_night=data['price_per_night']
            )
            listings.append(listing)
            self.stdout.write(self.style.SUCCESS(f'  Created listing: {listing.title}'))

        # Create sample bookings
        self.stdout.write('Creating bookings...')
        booking_count = 0
        for _ in range(10):
            listing = random.choice(listings)
            user = random.choice([u for u in users if u != listing.host])
            
            days_ahead = random.randint(1, 60)
            check_in = datetime.now().date() + timedelta(days=days_ahead)
            nights = random.randint(2, 7)
            check_out = check_in + timedelta(days=nights)
            
            total_price = listing.price_per_night * nights
            
            Booking.objects.create(
                listing=listing,
                user=user,
                check_in_date=check_in,
                check_out_date=check_out,
                total_price=total_price,
                status=random.choice(['pending', 'confirmed', 'confirmed'])
            )
            booking_count += 1

        self.stdout.write(self.style.SUCCESS(f'  Created {booking_count} bookings'))

        # Create sample reviews
        self.stdout.write('Creating reviews...')
        review_comments = [
            'Amazing place! Highly recommend.',
            'Great location and very clean.',
            'Perfect for our vacation.',
            'Excellent host and communication.',
            'Beautiful views and comfortable.',
        ]

        review_count = 0
        for listing in listings:
            num_reviews = random.randint(2, 4)
            reviewers = random.sample([u for u in users if u != listing.host], 
                                     min(num_reviews, len(users) - 1))
            
            for reviewer in reviewers:
                Review.objects.create(
                    listing=listing,
                    user=reviewer,
                    rating=random.randint(3, 5),
                    comment=random.choice(review_comments)
                )
                review_count += 1

        self.stdout.write(self.style.SUCCESS(f'  Created {review_count} reviews'))

        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))
        self.stdout.write(self.style.SUCCESS(f'Created: {len(users)} users, {len(listings)} listings, {booking_count} bookings, {review_count} reviews'))
        self.stdout.write(self.style.SUCCESS('='*50))