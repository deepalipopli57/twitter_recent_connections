from django.shortcuts import render
from twython import Twython

from recent_connections.local_settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

#API for fetching 10 recently users with twitter credentials as in local_settings.py
def twitter_users(request):
    try:
        user = Twython(app_key=CONSUMER_KEY,
                      app_secret=CONSUMER_SECRET,
                      oauth_token=ACCESS_TOKEN,
                      oauth_token_secret=ACCESS_TOKEN_SECRET
                      )
        search_results = user.get_friends_list(count=10)
        users = search_results['users']
        user_names = [usr['name'] for usr in users]
        return render(request, 'users.html', {'data': user_names})
    except:
        pass


