from Party_Planner import *
import math
import datetime
import GoogleMapsAPIs
import FuzzySets


def classify(amount):
	return 1/(1+math.exp(-amount))


# gmaps = GoogleMapsAPIs.GoogleMaps()
# print(gmaps.get_places_nearby_keyword('restaurant'))

#
date = datetime.date(2018, 5, 29)
planner = PartyPlanner()
planner.reset()
planner.set_facts(20, PartyPlanner.AGES_EARLY_TWENTIES, True, date, PartyPlanner.PARTY_GET_TOGETHER, True, 50)
planner.run()

print(planner.final_foods_list_fuzzy)
print(planner.final_drinks_list_fuzzy)
print(planner.final_decorations_list_fuzzy)
print(planner.final_checklist)
# print('Food:', planner.suggested_foods)
# print('Drinks:', planner.suggested_drinks)
# print('Music:', planner.suggested_playlist)
# print('Theme:', planner.suggested_themes)
# print('Decorations:', planner.suggested_decorations)

# fuzzy = FuzzyLogic.Fuzzy()
# budget = 2000
# planner = PartyPlanner()
# planner.reset()
# planner.set_facts(10, PartyPlanner.AGES_EARLY_TWENTIES, True, 1, PartyPlanner.PARTY_BIRTHDAY, True, 2000)
# print(planner.budget_class)
# planner.run()
