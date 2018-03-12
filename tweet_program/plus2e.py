import sys
from twython import Twython

CONSUMER_KEY       = ''
CONSUMER_SECRET    = ''
ACCESS_KEY         = ''
ACCESS_SECRET      = ''

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

TweetMessage = 'http://shop.maxwera.com/orange-pi-plus-2e-pmu9'

TweetPhoto  = '/home/sersa/Sersa/plus-2e-top.png'

TweetMessageName = '#Orangepi Plus 2e'


photo = open(TweetPhoto,'rb')
response = twitter.upload_media(media=photo)

twitter.update_status(media_ids=[response['media_id']] ,status= TweetMessage + " " + TweetMessageName)

