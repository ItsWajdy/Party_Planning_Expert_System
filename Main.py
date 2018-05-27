from Party_Planner import *
import datetime


def classify(amount):
	if amount <= 2:
		return 'Low'
	if 2 < amount <= 6:
		return "Medium"
	if amount > 6:
		return "High"


date = datetime.date(2018, 5, 29)
planner = PartyPlanner()
planner.reset()
planner.set_facts(20, PartyPlanner.AGES_EARLY_TWENTIES, True, date, PartyPlanner.PARTY_GET_TOGETHER, True, 20)
planner.run()

print('Food:', planner.suggested_foods)
print('Drinks:', planner.suggested_drinks)
print('Music:', planner.suggested_playlist)
print('Theme:', planner.suggested_themes)
print('Decorations:', planner.suggested_decorations)