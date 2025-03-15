from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import EggPrice

def chart_view(request):
    # Get the last 30 days of data
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    
    prices = EggPrice.objects.filter(
        date__range=(start_date, end_date)
    ).order_by('date')
    
    # Prepare data for the chart
    dates = [price.date.strftime('%Y-%m-%d') for price in prices]
    price_values = [float(price.price) for price in prices]
    
    context = {
        'dates': dates,
        'prices': price_values,
        'latest_price': price_values[-1] if price_values else None,
        'latest_date': dates[-1] if dates else None,
    }
    
    return render(request, 'chart/chart.html', context)
