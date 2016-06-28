{\rtf1\ansi\ansicpg1252\cocoartf1038\cocoasubrtf360
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red249\green249\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww17880\viewh10340\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\ql\qnatural\pardirnatural

\f0\fs24 \cf0 '''\
Local Settings for a quorn_bot account. #fill in the name of the account you're tweeting from here.\
'''\
\
#configuration\
MY_CONSUMER_KEY = '
\f1\fs28 \cf2 \cb3 DRyHJnaEuSSjKdCn44A1s4fHb'
\f0\fs24 \cf0 \cb1 \
MY_CONSUMER_SECRET = '
\f1\fs28 \cf2 \cb3 0IpVRuiFCCgj7ziIx7AtbatVgnzKycjAFkR84EfmJMfAFaBxm0'
\f0\fs24 \cf0 \cb1 \
MY_ACCESS_TOKEN_KEY = '
\f1\fs28 \cf2 \cb3 747842110368407552-tQOUH4UKoS9fQlOXoVxts42gv2fSheZ'
\f0\fs24 \cf0 \cb1 \
MY_ACCESS_TOKEN_SECRET = '
\f1\fs28 \cf2 \cb3 jsDPeSwGr2pnvJ8Tp0YQnXfFwf8FUe5l61BbDgUmdittQ'\

\f0\fs24 \cf0 \cb1 \
\
SOURCE_ACCOUNTS = ["qu0rn_d0g"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.\
ODDS = 8 #How often do you want this to run? 1/8 times?\
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.\
DEBUG = False #Set this to False to start Tweeting live\
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.\
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.\
TWEET_ACCOUNT = "quorn_bot" #The name of the account you're tweeting to.\
}