import led_indicator, time

print("testing 'led_startup()' sequence")
led_indicator.led_startup()
time.sleep(3)

print("testing 'tweet.sent()' sequence")
led_indicator.tweet_sent()
time.sleep(3)
exit()

