from pyknow import *
import datetime
from Backing_Classes import *


class PartyPlanner(KnowledgeEngine):

	PARTY_NONE = 'NONE'
	PARTY_BIRTHDAY = 'Birthday'
	PARTY_ANNIVERSARY = 'Anniversary'
	PARTY_GRADUATION = 'Graduation'
	PARTY_GET_TOGETHER = 'Get Together'

	AGES_NONE = 0
	AGES_KIDS = 1
	AGES_EARLY_TENS = 2
	AGES_LATE_TENS = 3
	AGES_EARLY_TWENTIES = 4

	# TODO fill prices
	prices = {}

	def __init__(self):
		super().__init__()
		self.num_guests = 0
		self.ages = PartyPlanner.AGES_NONE
		self.alcoholic_drinks = False
		self.date = datetime.date(2000, 1, 1)
		self.party_type = PartyPlanner.PARTY_NONE
		self.house_party = False
		self.budget = 0

		self.suggested_foods = []
		self.suggested_menus = []
		self.suggested_drinks = []
		self.suggested_playlist = []
		self.suggested_themes = []
		self.suggested_decorations = []

	@DefFacts()
	def init(self):
		yield Food('House Party', List(['Popcorn', 'Chips And Dip', 'Cheese Fingers', 'Finger Sandwiches', 'Potato Wedges',
								   'Spring Rolls', 'Fondue', 'Chocolate Fountain']))
		yield Food('Kids Party', List(['Popcorn', 'Chips And Dip', 'Cupcakes', 'Finger Sandwiches', 'Mini Pizzas',
								  'Mini Burgers']))
		yield Food('Birthday', List(['Birthday Cake']))

		yield Drinks('House Party', List(['Water', 'Soda']))
		yield Drinks('Kids Party', List(['Water', 'Soda', 'Juice Boxes']))
		yield Drinks('Alcohol', List(['Beer', 'Absintheِ', 'Vodka', 'Whiskey']))

		# TODO implement Menu
		yield Menu('Menu_1', List([]))
		yield Menu('Menu_2', List([]))
		yield Menu('Menu_3', List([]))

		# TODO implement Music Playlists
		# yield MusicPlaylist('Kids Party', List(['The 1975-Chocolate', 'McFLY-Do Ya', 'PSY-Gangnam Style',
		# 										'One Direction-Best Song Ever', 'Years & Years-King',
		# 										'Coldplay-A Sky Full Of Stars', 'Sliento-Watch Me',
		# 										'Royal Blood-Figure It Out', 'LunchMoney Lewis-Bills',
		# 										'Buddy Holly & His Crickets-That\'ll Be The Day',
		# 										'Deep Purple-Smoke On The Water', 'Katy Perry-Roar',
		# 										'Toni Basil-Hey Mickey', 'The Muppets-Life\' a Happy Song',
		# 										'Taylor Swift-Blank Space', 'One Direction-What Makes You Beautiful',
		# 										'OMI-CHEERLEADER', 'Pharrel Williams-Happy', 'Taylor Swift-Wonderland']))
		# yield MusicPlaylist('Birthday Kids', List(['Selena Gomez-Birthday', 'Weird Al Yankovic-Happy Birthday']))
		# yield MusicPlaylist('Birthday Early Twenties', List(['Selena Gomez-Birthday', 'Sufjan Stevens-Happy Birthday',
		# 													 'Mya-It\'s My Birthday',
		# 						  							 '50 Cent-In Da Club', '2Chainz-Birthday Song',
		# 													 'Rihanna-Birthday Cake',
		# 						                             'Weird Al Yankovic-Happy Birthday', 'The Beatles-Birthday',
		# 						                             'David Joel and Eric Sage-Birthday Drinking Song',
		# 													 'Madonna-B\'day Song']))
		# yield MusicPlaylist('Graduation', List(['Halesy-Castle', 'Kygo & Selena Gomez-It Ain\'t Me',
		# 										'Ed Sheeran-Castle On The Hill',
		# 										'Wiz Khalifa & Charlie Puth-See You Again', 'Lady Gaga-Marry The Night',
		# 										'Rihanna-Never Ending', 'John Legend-Love Me Now', 'Ruth B-Lost Boy',
		# 										'Alessia Cara-Wild Things', 'MO-Final Sonng',
		# 										'Bruno Mars-Too Good To Say Goodbye', 'Beyonce-Run The World',
		# 										'Hayley Kiyoko-Given It All', 'Troye Sivan-YOUTH', ]))

		yield MusicPlaylist('Anniversary', List(['https://open.spotify.com/user/1264690619/playlist/79NydVPZodhn3bG2LyKdrZ']))
		yield MusicPlaylist('Kids Party',
							List(['https://open.spotify.com/user/bbc_playlister/playlist/6uRN7aisZdhMyJ18irmLkT']))
		yield MusicPlaylist('Graduation', List(['https://open.spotify.com/user/mmmmpai/playlist/7GEDv08p82OGmUP9g0ITYO']))
		yield MusicPlaylist('Birthday', List(['https://open.spotify.com/user/meghantoumey/playlist/62KLyvQEueGcHYXf6HgAlu']))
		yield MusicPlaylist('Birthday Kids', List(['https://open.spotify.com/album/3p9s4eTLHI1VMAgYWEKc3v']))
		yield MusicPlaylist('House Party', List(['https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXaXB8fQg7xif',
												 'https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0IlCGIUGBsA']))
		yield MusicPlaylist('Party Late Tens',
							List(['https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX1N5uK98ms5p']))

		yield Themes('Kids Party', List(['Princess/Prince Theme', 'Disney Theme', 'Easter Egg Hunt', 'Pirate']))
		yield Themes('House Party', List(['Black and White', 'Formal Tea Party', 'Karaoke', 'Harry Potter',
										  'Lord Of The Rings', 'Mad Scientist', 'Under The Stars', 'Under The Sea',
										  'Fire and Ice']))

		yield Decorations('Birthday', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers', 'Gift Corner/Table']))
		yield Decorations('Birthday_Under 15', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
													 'Gift Corner/Table', 'Pinata', 'Bunting']))
		yield Decorations('Anniversary', List(['Center Pieces', 'Confetti', 'Candles and Votives']))
		yield Decorations('Generic', List(['Confetti', 'Balloons', 'Hanging Decorations']))

	def set_facts(self, num_guests, ages, alcoholic_drinks, date, party_type, house_party, budget):
		self.num_guests = num_guests
		self.ages = ages
		self.alcoholic_drinks = alcoholic_drinks
		self.date = date
		self.party_type = party_type
		self.house_party = house_party
		self.budget = budget

		self.declare(GuestsNumber(num_guests))
		self.declare(Ages(ages))
		self.declare(Alcoholic(alcoholic_drinks))
		self.declare(Date(date))
		self.declare(PartyType(party_type))
		self.declare(HouseParty(house_party))
		self.declare(Budget(budget))

	@Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
		  Food('House Party', 'foods' << W()))
	def suggest_foods_late_tens_get_together(self, foods):
		for item in foods.get_list():
			self.suggested_foods.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
		  Food('House Party', 'foods' << W()))
	def suggest_foods_early_twenties_get_together(self, foods):
		for item in foods.get_list():
			self.suggested_foods.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS),
		  Food('Kids Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
	def suggest_foods_kids_birthday(self, foods, birthday_foods):
		for item in foods.get_list():
			self.suggested_foods.append(item)
		for item in birthday_foods.get_list():
			self.suggested_foods.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
		  Food('Kids Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
	def suggest_foods_early_tens_birthday(self, foods, birthday_foods):
		for item in foods.get_list():
			self.suggested_foods.append(item)
		for item in birthday_foods.get_list():
			self.suggested_foods.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_LATE_TENS),
		  Food('House Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
	def suggest_foods_late_tens_birthday(self, foods, birthday_foods):
		for item in foods.get_list():
			self.suggested_foods.append(item)
		for item in birthday_foods.get_list():
			self.suggested_foods.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TWENTIES),
		  Food('House Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
	def suggest_foods_early_twenties_birthday(self, foods, birthday_foods):
		for item in foods.get_list():
			self.suggested_foods.append(item)
		for item in birthday_foods.get_list():
			self.suggested_foods.append(item)

	@Rule(HouseParty(False),
		  Menu('Menu_1', 'menu1' << W()), Menu('Menu_2', 'menu2' << W()), Menu('Menu_3', 'menu3' << W()))
	def suggest_menus(self, menu1, menu2, menu3):
		self.suggested_menus.append(menu1.get_list())
		self.suggested_menus.append(menu2.get_list())
		self.suggested_menus.append(menu3.get_list())

	@Rule(Ages(AGES_KIDS),
		  Drinks('Kids Party', 'drinks' << W()))
	def suggest_drinks_kids(self, drinks):
		for item in drinks.get_list():
			self.suggested_drinks.append(item)

	@Rule(Ages(AGES_EARLY_TENS),
		  Drinks('Kids Party', 'drinks' << W()))
	def suggest_drinks_early_tens(self, drinks):
		for item in drinks.get_list():
			self.suggested_drinks.append(item)

	@Rule(Ages(AGES_LATE_TENS),
		  Drinks('House Party', 'drinks' << W()))
	def suggest_drinks_late_tens(self, drinks):
		for item in drinks.get_list():
			self.suggested_drinks.append(item)

	@Rule(Ages(AGES_EARLY_TWENTIES), Alcoholic(False),
		  Drinks('House Party', 'drinks' << W()))
	def suggest_drinks_early_twenties(self, drinks):
		for item in drinks.get_list():
			self.suggested_drinks.append(item)

	@Rule(Ages(AGES_EARLY_TWENTIES), Alcoholic(True),
		  Drinks('House Party', 'drinks' << W()), Drinks('Alcohol', 'alcohol' << W()))
	def suggest_drinks_early_twenties_alcohol(self, drinks, alcohol):
		for item in drinks.get_list():
			self.suggested_drinks.append(item)
		for item in alcohol.get_list():
			self.suggested_drinks.append(item)

	@Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS),
		  MusicPlaylist('Birthday Kids', 'playlist' << W()))
	def suggest_music_birthday_kids(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
		  MusicPlaylist('Birthday Kids', 'playlist' << W()))
	def suggest_music_birthday_early_tens(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_LATE_TENS),
		  MusicPlaylist('Birthday', 'playlist' << W()))
	def suggest_music_birthday_late_tens(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TWENTIES),
		  MusicPlaylist('Birthday', 'playlist' << W()))
	def suggest_music_birthday_early_twenties(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
		  MusicPlaylist('Party Late Tens', 'playlist' << W()))
	def suggest_music_house_party_late_tens(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
		  MusicPlaylist('House Party', 'playlist' << W()))
	def suggest_music_house_party_early_twenties(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(PartyType(PARTY_ANNIVERSARY),
		  MusicPlaylist('Anniversary', 'playlist' << W()))
	def suggest_music_anniversary_party(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(PartyType(PARTY_GRADUATION),
		  MusicPlaylist('Graduation', 'playlist' << W()))
	def suggest_music_graduation_party(self, playlist):
		for item in playlist.get_list():
			self.suggested_playlist.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
		  Themes('House Party', 'themes' << W()))
	def suggest_themes_house_party_late_tens(self, themes):
		for item in themes.get_list():
			self.suggested_themes.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
		  Themes('House Party', 'themes' << W()))
	def suggest_themes_house_party_early_twenties(self, themes):
		for item in themes.get_list():
			self.suggested_themes.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS),
		  Themes('Kids Party', 'themes' << W()))
	def suggest_themes_birthday_kids(self, themes):
		for item in themes.get_list():
			self.suggested_themes.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
		  Themes('Kids Party', 'themes' << W()))
	def suggest_themes_birthday_early_tens(self, themes):
		for item in themes.get_list():
			self.suggested_themes.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
		  Decorations('Generic', 'decorations' << W()))
	def suggest_decorations_house_party_late_tens(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)
		self.suggested_decorations.append('Theme Specific Decorations')

	@Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
		  Decorations('Generic', 'decorations' << W()))
	def suggest_decorations_house_party_early_twenties(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)
		self.suggested_decorations.append('Theme Specific Decorations')

	@Rule(HouseParty(True), PartyType(PARTY_GRADUATION),
		  Decorations('Graduation', 'decorations' << W()))
	def suggest_decorations_graduation_party(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_ANNIVERSARY),
		  Decorations('Anniversary', 'decorations' << W()))
	def suggest_decorations_anniversary_party(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS),
		  Decorations('Birthday_Under 15', 'decorations' << W()))
	def suggest_decorations_birthday_kids(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)
		self.suggested_decorations.append('Theme Specific Decorations')

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
		  Decorations('Birthday_Under 15', 'decorations' << W()))
	def suggest_decorations_birthday_early_tens(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)
		self.suggested_decorations.append('Theme Specific Decorations')

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_LATE_TENS),
		  Decorations('Birthday', 'decorations' << W()))
	def suggest_decorations_birthday_late_tens(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)
		self.suggested_decorations.append('Theme Specific Decorations')

	@Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TWENTIES),
		  Decorations('Birthday', 'decorations' << W()))
	def suggest_decorations_birthday_early_twenties(self, decorations):
		for item in decorations.get_list():
			self.suggested_decorations.append(item)
		self.suggested_decorations.append('Theme Specific Decorations')

