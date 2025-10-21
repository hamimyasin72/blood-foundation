from .models import NewsTicker

def news_ticker(request):
    return {
        'tickers': NewsTicker.objects.all()
    }
