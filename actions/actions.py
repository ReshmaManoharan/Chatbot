# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
import json
from datetime import datetime
from random import randint
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionMenu(Action):

    def name(self) -> Text:
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        menu_list = []
        menu_details = json.loads(open("actions/menu.json", "r").read())
        for food in menu_details:
            menu_list.append([f"In {food_name} ---> {' | '.join(food_value)}\n" for food_name, food_value in food.items()][0])
        menu_message = f"Below is our menu for the day : \n{''.join(menu_list)}"
        dispatcher.utter_message(text=menu_message)

        return []
    
class ActionOrderSummary(Action):

    def name(self) -> Text:
        return "action_order_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        size_dict = {"S" : "small", "M" : "medium", "L" : "large", "XL" : "grand"}
        order_name = tracker.get_slot("buyer_name")
        item = tracker.get_slot("drink_name")
        item_size = tracker.get_slot("size_name")
        item_size = item_size if size_dict.get(item_size.upper(), "null") == "null" else size_dict[item_size]
        summary = f"** Order for {order_name} **\nOrder number: {randint(100, 400)}\nOrder Summary: One {item_size} {item}\n{str(datetime.now()).split('.')[0]}"
        #summary = f"Order number: {randint(100, 400)}\n{str(datetime.now()).split('.')[0]}"
        dispatcher.utter_message(text=summary)

        return []
    
class ActionDefaultFallback(Action):
     
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_fallback")

        return [] 

