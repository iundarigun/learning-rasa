# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk.forms import FormAction

class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email",
            ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        dispatcher.utter_message("Thanks for getting in touch, we'll contact you soon")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {"job_function": self.from_text(intent="inform"),
        "use_case": self.from_text(intent="inform"),
        "budget": self.from_text(intent="inform"),
        "person_name": self.from_text(intent="inform"),
        "company": self.from_text(intent="inform"),
        "business_email": self.from_text(intent="inform")}


class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return [UserUtteranceReverted()]