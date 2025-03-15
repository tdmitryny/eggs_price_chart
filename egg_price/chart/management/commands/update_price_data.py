from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
from chart.models import EggPrice

class Command(BaseCommand):
    help = 'Updates egg price data from USDA API'

    def handle(self, *args, **kwargs):
        try:
            # USDA API endpoint for egg prices
            url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'
            headers = {'Content-type': 'application/json'}
            data = {
                "seriesid": ["APU0000708111"],  # Grade A Large Eggs
                "startyear": str(timezone.now().year),
                "endyear": str(timezone.now().year)
            }
            
            response = requests.post(url, json=data, headers=headers)
            data = response.json()
            
            if data['status'] == 'REQUEST_SUCCEEDED':
                series = data['Results']['series'][0]
                if series['data']:
                    latest_data = series['data'][0]
                    price = float(latest_data['value'])
                    
                    # Create new price entry
                    EggPrice.objects.create(
                        price=price,
                        date=timezone.now(),
                        source='USDA BLS'
                    )
                    
                    self.stdout.write(
                        self.style.SUCCESS(f'Successfully updated egg price: ${price:.2f}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING('No price data available')
                    )
            else:
                self.stdout.write(
                    self.style.ERROR(f'API request failed: {data.get("message", "Unknown error")}')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating egg price data: {str(e)}')
            )
