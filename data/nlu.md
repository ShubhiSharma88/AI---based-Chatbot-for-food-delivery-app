## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- [morethan700](price)
- [lessthan300](price)

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- [between300to700](price)

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hola
- Hola!
- Hola!!
- hola!!
- Hi there!
- hello!
- Hello!
- Hey
- Hi

## intent:confirm
- yes
- ok
- sure
- please do
- okay
- yes please
- yes ok
- yes. Please

## intent:decline
- no
- no thanks
- nope
- nah
- don't
- please don't
- no. thanks

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Ahmedabad](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- I'm hungry. Looking out for some good restaurants
- [bengaluru](location)
- I'll prefer [thai](cuisine)
- [300-700](price) range
- Can you suggest some good restaurants in [Rishikesh](location)
- Okay. Show me some in [Allahabad](location)
- I'll prefer [chines](cuisine:chinese)
- [>700](price:morethan700)
- yes. Please send it to [xyz@gmail.com](email)
- [italian](cuisine)
- [Jaipur](location)
- [yes](confirm) please. it's [shubhi@gmail.com](email)
- i want to order some [north indian](cuisine) food
- [indore](location)
- [<300](price:lessthan300)
- my budget is [lesser than 300](price:lessthan300)
- [more than 700](price:morethan700)
- [between 300 and 700](price:between300to700)
- I would like to order some [Italian](cuisine) food
- In [Bangalore](location)
- in [between 300 to 700](price:between300to700)
- [shubhi.sharma2788@gmail.com](email)
- Hi, I would like to order from [Italian](cuisine) food
- In [Delhi](location)
- I am looking for [Italian](cuisine) restuarants in [Delhi](location)
- I am looking for [Chinese](cuisine:chinese) restaurants in [Delhi](location)
- I am looking for restaurant with budget [less than 300](price:lessthan300)
- in [Mumbai](location)
- [shubhitest123@gmail.com](email)
- I am looking for some restuarants in [Saharanpur](location)
- I am looking for [Italian](cuisine) restaurant in [Kurla](location)
- Looking for restaurants in [Chittorgarh](location)
- I am looking for a restaurant in [Kurla](location)
- I am looking for restaurants in [Bhatkal](location)
- yes, can you search for restaurants in [Lucknow](location)
- [Mexican](location)
- Are there any restaurants in [Bhatinda](location)
- what about [Lucknow](location)
- [Mexican](cuisine)
- in [mubaim](location)
- [American](cuisine)
- I'm hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- Can you suggesr some good restaurants in [Rishikesh](location)
- yes. Please send it to [shubhitest123@gmail.com](email)
- [bengaluru](location:Bangalore)
- I'll prefer [North Indian](cuisine)
- [300-700](price:between300to700) range
- Can you suggest some good restaurants in [kolkata](location)
- [american](cuisine)
- [<300](price:lessthan300)
- [shubhitest123@gmail.com](email)

## synonym:4
- four

## synonym:Bangalore
- bengaluru
- Bengaluru
- Bangalruru
- BLR

## synonym:Chennai
- chennai
- Madras

## synonym:Delhi
- New Delhi
- Dilli
- Delhi
- centre
- NDLS

## synonym:Italian
- italy
- italiaan
- itaalian
- itly
- pizza
- spaghetti
- spagetti

## synonym:Kolkata
- Calcutta
- Calcuta
- Kolkata

## synonym:Mexican
- mexecan
- mex
- mexico
- meksican
- taco

## synonym:Mumbai
- Bombay
- Mumbai
- Bambai
- MUM
- BOM

## synonym:Pune
- Pune
- Puna
- Poona

## synonym:between300to700
- between 300 and 700
- between 300 to 700
- 300-700
- 300> and <=700
- between 300 & 700
- from 300 to 700
- inbetween 300-700

## synonym:chinese
- chines
- Chinese
- Chines
- noodles
- manchurian

## synonym:lessthan300
- <300
- lesser than 300
- less than 300
- below 300
- cheaper than 300

## synonym:mid
- moderate

## synonym:morethan700
- >700
- more than 700
- above 700

## synonym:north indian
- punjabi

## synonym:vegetarian
- veggie
- vegg

## regex:email
- [\w\.\-\_]+@[\w]+.[a-zA-Z]{2,5}

## regex:greet
- hello[^\s]*
- hey[^\s]*
- hi[^\s]*

## regex:pincode
- [0-9]{6}

## regex:price
- [><=0-9 ]

## lookup:location
  data/city.txt

## lookup:cuisine
- Italian
- Chinese
- American
- North Indian
- South Indian
- Mexican
