consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('new_data2.csv', 'wb')

count = 0
csvWriter = csv.writer(csvFile)
tweets = []
# start = time.time()

my_file = open("dataverse_files/metoo_project_dataset_2019_oct_dec_01.txt", "r")
content = my_file.read()
# print(content)

content_list = content.split("\n")
content_list = content_list[0:500000]
my_file.close()
print(len(content_list))

new_file = open("dataverse_files/metoo_project_dataset_2019_oct_dec_01_new_1.txt", "w")

count = 0
numbers = 0
for id_of_tweet in content_list:
	try:
		tweet = api.get_status(int(id_of_tweet), tweet_mode="extended", len='en')
		numbers += 1
		# print(tweet.full_text)

	except Exception as e:
		count+=1
		# print(e)

	if tweet:
		print("Still counting", numbers)
		new_file.write(id_of_tweet)
		csvFile.write(tweet.full_text.encode('utf-8'))
print(count)
