from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from flask_mail import Mail, Message
from flask import Flask, current_app

import zomatopy
import json
import operator

# code
#for setting email server details
app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'shubhitest123@gmail.com',
    "MAIL_PASSWORD": 'Hello*123'
}

app.config.update(mail_settings)
mail = Mail(app)

class ActionSearchRestaurants(Action):
    def name(self):
      return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {
            "user_key": "f4924dc9ad672ee8c4f8c84743301af5"
        }
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        email = tracker.get_slot('person')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        city_id = d1["location_suggestions"][0]["city_id"]
        cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}

        list1 = [80]
        d = []
        for i in list1:
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine.lower())), limit=i)
            d1 = json.loads(results)
            d.extend(d1['restaurants'])

        response = []
        if len(d) == 0:
            response = "no results"
        else :
            for restaurant in d:
                if str(price) == 'lessthan300':
                    if restaurant['restaurant']['average_cost_for_two'] < 300:
                        response.append([restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],float(restaurant['restaurant']['user_rating']['aggregate_rating'])])
                    else:
                        response
                elif str(price) == 'between300to700':
                    if 300 <= restaurant['restaurant']['average_cost_for_two'] <700:
                        response.append([restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],float(restaurant['restaurant']['user_rating']['aggregate_rating'])])
                    else:
                        response
                else:
                    if restaurant['restaurant']['average_cost_for_two'] >=700:
                        response.append([restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],float(restaurant['restaurant']['user_rating']['aggregate_rating'] )])
                    else:
                        response

        response = sorted(response, key=operator.itemgetter(3), reverse=True)
        top5 = response[:5]
        response_display = 'Showing you top results:' +"\n"
        if len(top5) == 0:
            dispatcher.utter_message("Sorry, we couldn't find any results!")
        else:
            for i in top5:
                response_display = response_display + i[0] + ' (rated ' + str(i[3]) + ') in ' + i[1] + ' and the average price for two people is Rs.' + str(i[2]) +"\n"
            dispatcher.utter_message("-----"+str(response_display))

        response_email = 'Here are the top results for your query- ' + cuisine + ' restaurants in '+ loc + ' with budget for two '+ price + ': \n'
        count = 0
        for i in response[:10]:
            count+=1
            response_email = response_email + str(count) +') - ' +i[0] + ' (rated ' + str(i[3]) + ') in ' + i[1] + ' and the average price for two people is Rs.' + str(i[2]) +"\n"

        return [SlotSet('search_results',response_email)]

class ActionEmailRestaurantsDetails(Action):
    def name(self):
        return 'action_email_restaurants_details'

    @app.route('/send-mail/')
    def run(self, dispatcher, tracker, domain):
        config = {
            "user_key": "f4924dc9ad672ee8c4f8c84743301af5"
        }
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        email = tracker.get_slot('email')
        search_results = tracker.get_slot('search_results')
        with app.app_context():
            msg = Message("Top 10 restaurant search", sender = "shubhitest123@gmail.com", recipients = [email])
            msg.body = search_results
            mail.send(msg)
            dispatcher.utter_message("Email sent! Hope I can be of any assistance soon! Goodbye.")

        return 0

class Location_Check(Action):
    def name(self):
        return 'action_check_location'

    def run(self, dispatcher, tracker, domain):
        config={"user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        city_dict  = ['Gunter',    'Raipur',    'Dharamshala',    'Jhansi',    'Ludhiana',    'Vijayawada',
        'Meerut',    'Surat',    'Varanasi',    'Salem',    'Agra',    'Ranchi',    'Kolkata',    'Dehradun',
        'Kanpur',    'Pune',    'Jammu',    'Palakkad',    'Cuttack',    'Bhubaneswar',    'Aurangabad',    'Jaipur',
        'Madurai',    'Visakhapatnam',    'Kochi',    'Gwalior',    'Mangalore',    'Indore',    'Chandigarh',
        'Delhi NCR',    'Patna',    'Jamshedpur',    'Sheboygan',    'Bhopal',    'Ahmedabad',    'Kota',    'Vadodara',
        'Mumbai',    'Chennai',    'Gorakhpur',    'Coimbatore',    'Hyderabad',    'Nashik',    'Lucknow',    'Goa',    'Jodhpur',
        'Nagpur',    'Amritsar',    'Abu Dhabi',    'Ajmer',    'Mysore',    'Allahabad',    'Jalandhar',    'Bengaluru',
        'Vellore',    'Srinagar',    'Thrissur',    'Siliguri',    'Trivandrum']

        city_dict = [x.lower() for x in city_dict]
        if len(d1["location_suggestions"]) ==0:
            dispatcher.utter_message("Sorry, we are unable to find your location, can you please mention it again?")
            location_f = 'notfound'
            location_new = None
        elif (d1["location_suggestions"][0]["city_name"]).lower() not in city_dict:
            dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some othe location")
            location_f = 'tier3'
            location_new = None
        else:
            location_f = 'found'
            location_new = loc

        return [SlotSet('location',location_new), SlotSet('location_found',location_f)]
