## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}




## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"price": "300-700"}
    - action_search_restaurants
    - utter_should_send_email
* restaurant_search{"affirm": "yes", "email": "ahbcdj@dkj.com"}
    -action_email_restaurants_details
    - utter_confirm_yes_email_bye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - utter_dont_serve_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"search_results":""}
    - utter_should_send_email
* restaurant_search{"email": "xyz@gmail.com"}
    - action_email_restaurants_details

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"search_results":""}
    - slot{"location": "Jaipur"}
    - utter_should_send_email
* restaurant_search{"confirm": "yes", "email": "shubhi@gmail.com"}
    - action_email_restaurants_details

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"search_results":""}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_budget
* restaurant_search{"price": "between300to700"}
    - slot{"price": "between300to700"}
    - action_search_restaurants
    - slot{"search_results": "Byg Brewski Brewing Company (rated 4.9) in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore and the average price for two people is Rs.1600\nByg Brewski Brewing Company (rated 4.9) in Behind MK Retail, Sarjapur Road, Bangalore and the average price for two people is Rs.1600\nBrahma Brews (rated 4.9) in 24th Main, 7th Phase, Opposite Brigade Palm Springs, JP Nagar, Bangalore and the average price for two people is Rs.1850\nTBC- Sky Lounge (rated 4.9) in 36/1, 5th Floor, Berry's Hotel, Kadubeesanahalli, Opposite JP Morgan, Ring Road, Marathahalli, Bangalore and the average price for two people is Rs.1600\nByg Brewski Brewing Company (rated 4.9) in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore and the average price for two people is Rs.1600\nByg Brewski Brewing Company (rated 4.9) in Behind MK Retail, Sarjapur Road, Bangalore and the average price for two people is Rs.1600\nBrahma Brews (rated 4.9) in 24th Main, 7th Phase, Opposite Brigade Palm Springs, JP Nagar, Bangalore and the average price for two people is Rs.1850\nTBC- Sky Lounge (rated 4.9) in 36/1, 5th Floor, Berry's Hotel, Kadubeesanahalli, Opposite JP Morgan, Ring Road, Marathahalli, Bangalore and the average price for two people is Rs.1600\nByg Brewski Brewing Company (rated 4.9) in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore and the average price for two people is Rs.1600\nByg Brewski Brewing Company (rated 4.9) in Behind MK Retail, Sarjapur Road, Bangalore and the average price for two people is Rs.1600\n"}
    - utter_should_send_email
* confirm
    - utter_ask_email
* restaurant_search{"email": "shubhi.sharma2788@gmail.com"}
    - slot{"email": "shubhi.sharma2788@gmail.com"}
    - action_email_restaurants_details
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - slot{"location_found": ""}
    - utter_ask_budget
* goodbye{"price": "between300to700"}
    - slot{"price": "between300to700"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top 10 results for your query- Italian restaurants in Delhiwith budget for two between300to700: \n1) - Hauz Khas Social (rated 4.8) in 9-A & 12, Hauz Khas Village, New Delhi and the average price for two people is Rs.1300\n2) - Hauz Khas Social (rated 4.8) in 9-A & 12, Hauz Khas Village, New Delhi and the average price for two people is Rs.1300\n3) - Hauz Khas Social (rated 4.8) in 9-A & 12, Hauz Khas Village, New Delhi and the average price for two people is Rs.1300\n4) - Hauz Khas Social (rated 4.8) in 9-A & 12, Hauz Khas Village, New Delhi and the average price for two people is Rs.1300\n5) - C.I.A. Call it Asiian (rated 4.7) in 13/14/15/16, Narmada Shopping Complex, Opposite Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi and the average price for two people is Rs.700\n6) - Masia - Indian. Asian. Cultures (rated 4.7) in Plot 102A, Opposite Gardens Galleria, Sector 38, Noida and the average price for two people is Rs.1800\n7) - C.I.A. Call it Asiian (rated 4.7) in 13/14/15/16, Narmada Shopping Complex, Opposite Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi and the average price for two people is Rs.700\n8) - Masia - Indian. Asian. Cultures (rated 4.7) in Plot 102A, Opposite Gardens Galleria, Sector 38, Noida and the average price for two people is Rs.1800\n9) - C.I.A. Call it Asiian (rated 4.7) in 13/14/15/16, Narmada Shopping Complex, Opposite Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi and the average price for two people is Rs.700\n10) - Masia - Indian. Asian. Cultures (rated 4.7) in Plot 102A, Opposite Gardens Galleria, Sector 38, Noida and the average price for two people is Rs.1800\n"}
    - utter_should_send_email
* confirm
    - utter_ask_email
* restaurant_search{"email": "shubhi.sharma2788@gmail.com"}
    - slot{"email": "shubhi.sharma2788@gmail.com"}
    - action_email_restaurants_details
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - utter_ask_budget
* goodbye{"price": "between300to700"}
    - slot{"price": "between300to700"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top 10 results for your query- chinese restaurants in Delhiwith budget for two between300to700: \n1) - China Box (rated 4.5) in 2nd Floor, Ashoka Complex, Near Ocus Quantum Mall, Sector 51, Near Sector 50, Gurgaon and the average price for two people is Rs.600\n2) - Momo Hut (rated 4.2) in 141, 1st Floor, City Plaza, Gaur City 1, Greater Noida and the average price for two people is Rs.500\n3) - Mom Hand Momos (rated 4.1) in Opposite Venkateshwara College, Satyaniketan, New Delhi and the average price for two people is Rs.300\n4) - Drifters Wok (rated 4.0) in A212, Super Mart 1, DLF Phase 4, Gurgaon and the average price for two people is Rs.550\n5) - KC Restaurant (rated 4.0) in Ramphal Chowk, Opposite Relaxo Showroom, Sector 7, Dwarka, New Delhi and the average price for two people is Rs.450\n6) - Prem Chinese Fast Food (rated 3.9) in 23, C4E Market, Janakpuri, New Delhi and the average price for two people is Rs.350\n7) - Sunil Momos.com (rated 3.8) in 14, Block GH, Paschim Vihar, New Delhi and the average price for two people is Rs.300\n"}
    - utter_should_send_email
* confirm
    - utter_ask_email
* restaurant_search{"email": "shubhi.sharma2788@gmail.com"}
    - slot{"email": "shubhi.sharma2788@gmail.com"}
    - action_email_restaurants_details
* stop

## interactive_story_2
    - utter_greet
* restaurant_search{"price": "lessthan300"}
    - slot{"price": "lessthan300"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top 10 results for your query- South Indian restaurants in Mumbaiwith budget for two lessthan300: \n1) - Cafe Madras (rated 4.3) in 38 B, Circle House, King's Circle Near Maheshwari Udyan, Matunga East, Mumbai and the average price for two people is Rs.250\n2) - Hotel Ram Ashraya (rated 4.3) in Bhandarkar Road, Matunga East, Mumbai and the average price for two people is Rs.200\n3) - Mani's Lunch Home (rated 4.0) in 153 C, Mahskar Building, Near Ruia College, Matunga East, Mumbai and the average price for two people is Rs.200\n4) - Swamy - South Indian Food Express (rated 4.0) in Lok Upvan Circle, Barrister Nath Pai Marg, Pokhran Road 2, Upvan, Thane West, Thane and the average price for two people is Rs.200\n5) - Udipi Idli House (rated 4.0) in 462, Ram Bhavan, Opposite Jain Temple, Dr. B R Ambedkar Road, King Circle, Matunga East, Mumbai and the average price for two people is Rs.150\n6) - Anand Bhavan (rated 3.9) in 461/A, Ram Niwas, Maheshwari Udyan, Ambedkar Road, Matunga East, Mumbai and the average price for two people is Rs.200\n"}
    - utter_should_send_email
* confirm
    - utter_ask_email
* restaurant_search{"email": "shubhitest123@gmail.com"}
    - slot{"email": "shubhitest123@gmail.com"}
    - action_email_restaurants_details
* stop


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Bhatinda"}
    - slot{"location": "Bhatinda"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* affirm{"price": "morethan700"}
    - slot{"price": "morethan700"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top results for your query- Mexican restaurants in Lucknow with budget for two morethan700: \n1) - Be The Beer (rated 4.4) in A110, First Floor, Cyber Heights, Above Nexa Showroom, Vibhuti Khand, Gomti Nagar, Lucknow and the average price for two people is Rs.1200\n2) - Garden Bakery (rated 4.3) in Plot 297, Bara Birwa, Kanpur Road, Alambagh, Lucknow and the average price for two people is Rs.800\n3) - Garden Bakery (rated 4.3) in B 1031, Behind Bhootnath Market, Indira Nagar, Lucknow and the average price for two people is Rs.800\n4) - Be The Beer Season 2 (rated 4.3) in 19, 20, Rohtas Presidential Arcade, Vibhuti Khand, Gomti Nagar, Lucknow and the average price for two people is Rs.1200\n5) - Coffee Culture (rated 4.1) in 1st Floor, B 939/A, Mandir Marg, Gole Market, Mahanagar, Lucknow and the average price for two people is Rs.800\n6) - Coal Jar Bistro (rated 4.1) in CP 101, Upper Ground Floor, Viraj Khand, Gomti Nagar, Lucknow and the average price for two people is Rs.800\n7) - JW Club (rated 3.8) in 5th Floor , Shalimar Elldee Plaza ,Bhoothnath, Indira Nagar, Lucknow and the average price for two people is Rs.1000\n8) - Bombay Blue (rated 3.6) in 3rd Floor, Phoenix United Mall, Alambagh, Lucknow and the average price for two people is Rs.1200\n9) - Heimweh Cafe (rated 3.2) in LDA Colony, Sector K, Near Aashiana Power House Chowraha, Aashiana, Lucknow and the average price for two people is Rs.800\n10) - Downtown \"The Cafe Lounge\" (rated 3.0) in 5/18, Manoj Pandey Chauraha, Vishal Khand, Gomti Nagar Lucknow, Uttar Pradesh and the average price for two people is Rs.850\n"}
    - utter_should_send_email
* confirm
    - utter_ask_email
* restaurant_search{"email": "shubhitest123@gmail.com"}
    - slot{"email": "shubhitest123@gmail.com"}
    - action_email_restaurants_details
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* affirm{"price": "lessthan300"}
    - slot{"price": "lessthan300"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top results for your query- American restaurants in Mumbai with budget for two lessthan300: \n"}
    - utter_should_send_email
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* affirm{"price": "lessthan300"}
    - slot{"price": "lessthan300"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top results for your query- chinese restaurants in chandigarh with budget for two lessthan300: \n1) - Sandhya (rated 3.9) in Booth 37 & 40, Rehri Market, Sector 7, Panchkula and the average price for two people is Rs.250\n"}
    - utter_should_send_email
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "morethan700"}
    - slot{"price": "morethan700"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top results for your query- chinese restaurants in Allahabad with budget for two morethan700: \n1) - EDEN by Connoisseur (rated 4.9) in Hotel Samrat, Civil Lines, Allahabad and the average price for two people is Rs.1000\n2) - Sagar Ratna (rated 4.5) in 3/3, Hashimpur Road, Balson Crossing, Near Anand Bhawan, Tagore Town, Allahabad and the average price for two people is Rs.800\n3) - Old School Cafe (rated 4.4) in 2nd Floor, 9-10 Tulsiani Grace, Civil Lines, Allahabad and the average price for two people is Rs.1000\n4) - El Chico Restaurant (rated 4.3) in 142A, 32, Mahatma Gandhi, Civil Lines, Allahabad and the average price for two people is Rs.800\n5) - Pind Balluchi (rated 4.3) in 48/8, Stratchy Road, Civil Lines, Allahabad and the average price for two people is Rs.1000\n6) - Berco's (rated 4.2) in 17C, 0-1, Stretchy Road, Civil Lines, Allahabad and the average price for two people is Rs.1600\n"}
    - utter_should_send_email
* confirm
    - utter_ask_email
* restaurant_search{"email": "shubhitest123@gmail.com"}
    - slot{"email": "shubhitest123@gmail.com"}
    - action_email_restaurants_details
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* affirm{"price": "morethan700"}
    - slot{"price": "morethan700"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top results for your query- Mexican restaurants in Allahabad with budget for two morethan700: \n"}
    - utter_should_send_email
* restaurant_search{"email": "shubhitest123@gmail.com"}
    - slot{"email": "shubhitest123@gmail.com"}
    - action_email_restaurants_details
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"price": "between300to700"}
    - slot{"price": "between300to700"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top results for your query- North Indian restaurants in Bangalore with budget for two between300to700: \n1) - Dilli to Dakshin (rated 4.4) in 2735, Kousthubham, 16th Cross, 27th Main, Opposite NIFT College, Sector 1, HSR, Bangalore and the average price for two people is Rs.600\n2) - Aligarh House (rated 4.3) in 34/154 & 155, 1st Floor, 11th Cross Somasundrapalya, Sector 2, HSR, Bangalore and the average price for two people is Rs.400\n3) - Al-Bek (rated 4.2) in 349, 350, 1A/87, Dr Rajkumar Road, 6th Block, Rajaji Nagar Industrial Town, Rajajinagar, Bangalore and the average price for two people is Rs.400\n4) - Grill Biryanis (rated 4.1) in 9, Jalahalli Cross Circle, Jalahalli, Bangalore and the average price for two people is Rs.500\n5) - Al-Bek (rated 4.1) in 48/6, MKK Road, Near Sri Rampura Metro Station, Nagappa Block, Rajajinagar, Bangalore and the average price for two people is Rs.400\n6) - Al-Bek (rated 4.1) in 527, 1st Cross, Sampige Road, Malleshwaram, Bangalore and the average price for two people is Rs.400\n7) - Al-Bek (rated 4.0) in 1, 80 Feet Road, Besides Florence School, RT Nagar, Bangalore and the average price for two people is Rs.400\n8) - Al-Bek (rated 4.0) in 9th Block, Opposite Jayadeva Hospital, Off Bannerghatta Road, Jayanagar, Bangalore and the average price for two people is Rs.650\n9) - Zero Mile Punjab (rated 3.9) in 79/8, 1st Main, Muneshwara Nagar, Sector 6, HSR, Bangalore and the average price for two people is Rs.400\n"}
    - utter_should_send_email
* restaurant_search{"email": "shubhitest123@gmail.com"}
    - slot{"email": "shubhitest123@gmail.com"}
    - action_email_restaurants_details
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "lessthan300"}
    - slot{"price": "lessthan300"}
    - action_search_restaurants
    - slot{"search_results": "Here are the top results for your query- american restaurants in kolkata with budget for two lessthan300: \n1) - The Chicken House (rated 4.0) in 29/1, Hare Krishna Kunal Road, Entally, Kolkata and the average price for two people is Rs.250\n2) - Goofys Chicken Shack (rated 3.5) in 156, GT Road, Near Little Start High School, Bally, Howrah and the average price for two people is Rs.200\n"}
    - utter_should_send_email
* confirm
    - utter_ask_email
* restaurant_search{"email": "shubhitest123@gmail.com"}
    - slot{"email": "shubhitest123@gmail.com"}
    - action_email_restaurants_details
    - action_restart
