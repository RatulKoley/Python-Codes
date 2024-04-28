name = 'Ratul Koley'
age = 25
has_android_phone = True
name, age, has_android_phone

person = {
    "Name": name,
    "Age" : age,
    "HasAndroidPhone": has_android_phone 
}
print("{} is a good guy, aged {} with {}".format(person["Name"],person["Age"],
         "Android Phone" if person["HasAndroidPhone"]  else "IPhone"))

for item in person:
    print("The key named \"{}\" has the value \"{}\" of the type \"{}\"".format
            (item,person[item],type(person[item])))
    

### QUESTION NUMBER 2 ###

my_list = ['red',3,False]
print('My favourite color is {}'.format(my_list[0]))
print('I have {} pet(s)'.format(my_list[1]))
if my_list[2]:
    print('I have previous programming knowledge')
else:
    print('I dont have previous programming knowledge')

my_list.append(69)
my_list.pop(0)
print('Number of element in the list is {}'.format(len(my_list)))


### Question Number 3 ###
a = 'The sum of '
b = 0
for item in range(18,534):
    if item % 7 == 0:
        b = b + item
        a = a + '{} + '.format(item)
print('{} is = {}'.format(a,b))


### Question Number 4 ###
cost_of_flying_plane = 5000
number_of_passengers = 29
price_of_ticket = 200
profit = (((number_of_passengers*price_of_ticket)*100)/cost_of_flying_plane) - 100
print('Total Profit Will Be {}%'.format(profit))


### Question Number 4 Optional ###
cost_of_flying_plane = 5000
number_of_passengers = 29
number_of_passengers_return = 12
price_of_ticket = 200
profit = ((((number_of_passengers+number_of_passengers_return)*price_of_ticket)
           *100)/(cost_of_flying_plane*2)) - 100
if(profit>0):
    print('Total Profit Will Be {}%'.format(profit))
else:
    print('Total Loss Will Be {}%'.format(-profit))


### Question Number 5 ###

tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

number_of_tweets = len(tweets)
print(number_of_tweets)

happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']
happycounter = 0
sadcounter = 0
neutralcounter = 0
for item in tweets:
    for happyword in happy_words:
        if happyword in item:
            print('Tweet Number {} contains Happy Word \"{}\"'.format(tweets.index(item) + 1,happyword))
            happycounter += 1
    for sadword in sad_words:
        if sadword in item:
            print('Tweet Number {} contains Sad Word \"{}\"'.format(tweets.index(item) + 1,sadword))
            sadcounter += 1
print('Total Tweets Containing happy words are {}'.format(happycounter))
print('Total Tweets Containing happy words in fraction is {}'.format(happycounter/(len(tweets)+1)))
print('Total Tweets Containing sad words are {}'.format(sadcounter))
print('Total Tweets Containing sad words in fraction is {}'.format(sadcounter/(len(tweets)+1)))
Sentiment_Score = (happycounter/(len(tweets)+1))-(sadcounter/(len(tweets)+1))
print('The overall sentiment is happy') if(Sentiment_Score) else print('The overall sentiment is sad')


