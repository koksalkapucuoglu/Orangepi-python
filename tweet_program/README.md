What you need for Tweet program?
* sudo apt-get update (check update)
* sudo apt-get install -y python-setuptools (install python tool)
* sudo easy_install pip (install pip , pip is a package manager)
* sudo apt-get install python-pip  (other way)
* sudo pip  install  twython requests requests_oauthlib (install twython , twython is python twitter package)

--------------------------------------------------------------------------------------------------------------------------
* Making app settings via Twitter
  https://apps.twitter.com/
** click 'Create your Twitter application
** You can substitute 'http://localhost.dev' for the website.
** I'll go to "Keys and Access Tokens" 
** Click “Create my access token” 
** Save  “Consumer Key (API Key)” ,  “Consumer Secret (API Secret)” ,“Access Token” and “Access Token Secret” values anywhere.   

* git clone https://github.com/koksalkapucuoglu/Tweet-Program.git
* cd tweet_program
* nano twit_zero.py 
* Fill in your information for vacancies.
* finally python twit_zero.py
