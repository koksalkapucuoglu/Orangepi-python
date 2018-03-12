import sys
from twython import Twython

CONSUMER_KEY       = ''
CONSUMER_SECRET    = ''
ACCESS_KEY         = ''
ACCESS_SECRET      = ''

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

TweetMessage = 'http://shop.maxwera.com/orange-pi-prime-pmu68'

TweetPhoto  = '/home/sersa/Sersa/prime-top.png'

TweetMessageName = '#Orangepi Prime'


photo = open(TweetPhoto,'rb')
response = twitter.upload_media(media=photo)

twitter.update_status(media_ids=[response['media_id']] ,status= TweetMessage + " " + TweetMessageName)
