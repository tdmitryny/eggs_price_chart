from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from chart.models import EggPrice
import random

class Command(BaseCommand):
    help = 'Populates the database with sample egg price data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        EggPrice.objects.all().delete()

        # Generate data for the past year
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=365)
        
        # Initial price
        price = 2.50
        
        # Generate daily prices
        current_date = start_date
        while current_date <= end_date:
            # Add some random variation (-5% to +5%)
            change = price * (random.uniform(-0.05, 0.05))
            price = max(1.50, min(4.50, price + change))  # Keep price between $1.50 and $4.50
            
            EggPrice.objects.create(
                date=current_date,
                price=round(price, 2)
            )
            
            current_date += timedelta(days=1)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated egg price data'))
