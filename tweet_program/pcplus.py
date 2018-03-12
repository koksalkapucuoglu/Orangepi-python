
import sys
from twython import Twython

CONSUMER_KEY       = ''
CONSUMER_SECRET    = ''
ACCESS_KEY         = ''
ACCESS_SECRET      = ''

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

TweetMessage = 'http://shop.maxwera.com/orange-pi-pc-plus-pmu8'

TweetPhoto  = '/home/sersa/Sersa/pc-plus-top.png'

TweetMessageName = '#Orangepi PC Plus'


photo = open(TweetPhoto,'rb')
response = twitter.upload_media(media=photo)

twitter.update_status(media_ids=[response['media_id']] ,status= TweetMessage + " " + TweetMessageName)

