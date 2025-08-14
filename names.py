from random import choice

def generate_name(names_list:list, surname_list:list=[]) -> tuple:
	forname:str = choice(names_list)
	if not surname_list:
		surname:str = choice(names_list) + "son"
	else:
		surname:str = choice(surname_list)
	return forname, surname


viking_names = ["Aghi", "Agmundr", "Agnarr", "Agni", "Áki", 
		"Áleifr", "Alfarr", "Alfríkr", "Alfvin", 
		"Algautr", "Anundr", "Ari", "Arnfinnr", 
		"Árni", "Árni", "Arnórr", "Arnsteinn", 
		"Arnþórr", "Arnviðr", "Ásbjǫrn", "Ásgeirr",
		"Ásketill", "Áskeladd", "Ásmundr", "Ásvaldr", "Aðalsteinn",
		"Auðr", "Auðun", "Baggi", "Bárðr", "Birgir", 
		"Bjarni", "Bjartr", "Bjǫrn", "Brandr", "Bróðir",
		"Brynjarr", "Búi", "Dagfinnr", "Dagr", "Danr", 
		"Egill", "Eileifr", "Einarr", "Eindriði", "Eiríkr",
		"Erlendr", "Erlingr", "Eysteinn", "Eyvindr", "Fastúlfr",
		"Félagi", "Finnr", "Flæmingr", "Fólki", "Friðþjófr", 
		"Fróði", "Gauti", "Gautstafr", "Geirmundr", "Geirr", 
		"Gulbrandr", "Gunnarr", "Gunni", "Gunnvaldr", "Guðbrandr", 
		"Guðfrøðr", "Guðini", "Guðleifr", "Guðmundr", "Guðormr", 
		"Guðrøðr", "Hákon", "Hálfdan", "Hallbjǫrn", "Halli", "Hallr", 
		"Hallsteinn", "Hallþórr", "Hallvarðr", "Hámundr", "Haraldr", 
		"Harðaknútr", "Hávarðr", "Helgi", "Heming", "Herleifr", 
		"Hilddingr", "Hjálmarr", "Hólmgeirr", "Hrafn", "Hreiðarr", 
		"Hróaldr", "Hróarr", "Hrœrekr", "Hrólfr", "Hrǿríkr", 
		"Hróðgeirr", "Hróðulfr", "Hugleikr", "Ingi", "Ingimárr",
		"Ingólfr", "Ívarr", "Jarl", "Jóarr", "Jósteinn", "Kálfr", 
		"Kári", "Karl", "Ketill", "Knútr", "Kolr", "Kóri", "Leifr", 
		"Magni", "Mundi", "Njáll", "Oddbjǫrn", "Oddgeirr", 
		"Oddr", "Oddvarr", "Ǫlvir", "Óttarr", "Ragnarr", "Ragnvaldr",
		"Randúlfr", "Ráðúlfr", "Rúni", "Sigfrøðr", "Sigmundr", 
		"Sigsteinn", "Sigurðr", "Sindri", "Snorri", "Sǫlvi", 
		"Somerled", "Stáli", "Steinarr", "Steingrímr", "Steinn", 
		"Stígandr", "Stigr", "Sumarliði", "Sundri", "Suni", "Sveinn",
		"Sverrir", "Tórarinn", "Tórbjǫrn", "Tórfastr", "Torfinn", 
		"Tórfreðr", "Tórgeirr", "Tórgísl", "Tórgnýr", "Tórgrímr", 
		"Tórir", "Tórketill", "Tórleifr", "Tórleikr", "Tórmóðr", 
		"Tórsteinn", "Tórðr", "Tórvaldr", "Tróndr", "Tófi", "Tóki", 
		"Tryggvi", "Úlfr", "Uni", "Vagn", "Valdimárr", "Valþjófr", 
		"Vébjǫrn", "Végarðr", "Vetrliði", "Vígi", "Víkingr", "Vragi",
		"Yngvarr", "Simøn", "Lúis"]

english_forenames = ['Botwulf', 'Cola', 'Eadberht', 'Eadræd', 'Eadwald', 
				'Eadwig', 'Eadwulf', 'Ealdhelm', 'Ealdræd', 'Glædwine', 
				'Godric', 'Godwine', 'Heard', 'Hereward', 'Hroðgar', 
				'Leofwine', 'Sigeberht', 'Waltheof', 'Wigberht', 'Wulfnoð', 
				'Waermund', 'Aelfheah', 'Aelfric', 'Aelfwine', 'Aesc', 'Aeðelfrið', 
				'Aeðelmær', 'Aeðelric', 'Aeðelræd', 'Aeðelstan', 'Aeðelwine', 'Aeðelwulf', 
				'Aethelbeorht']

english_surnames = medieval_epithets = [
    "the Tall","the Short", "the Great","the Small","the Mighty","the Strong","the Stout",
    "the Lean","the Broad","the Giant","the Slender","the Stocky","the Burly","the Gaunt",
    "the Massive","the Thin","the Heavy","the Swift","the Large","the Frail","the Fair",
    "the Ruddy","the Pale","the Scarred","the One-eyed","the Cross-eyed","the Blue-eyed","the Green-eyed","the Hook-nosed",
    "the Lame", "the Blind", "the Crooked", "the Hunchbacked", "the Limping", "the Stuttering",
     "the Marked", "the Branded", "the Wounded", "the Maimed", "the Twisted", "the Wise", "the Just", 
     "the Noble", "the Brave", "the Bold", "the Loyal", "the Honest", "the Kind", "the Gentle", 
    "the Patient", "the Merciful", "the Generous", "the Faithful", "the Righteous", "the Good", 
    "the Pure", "the Humble", "the Pious","the Devout","the Sacred","the Holy","the Blessed",
    "the Peaceful","the Calm","the Steadfast","the True","the Honorable","the Virtuous",
    "the Cruel","the Mad","the Wicked","the Evil","the Treacherous","the Coward","the False",
    "the Greedy","the Selfish","the Jealous","the Angry","the Bitter","the Harsh","the Cold","the Ruthless","the Merciless",
    "the Bloodthirsty","the Vengeful","the Spiteful","the Cunning","the Sly","the Deceitful",
    "the Dishonest","the Corrupt","the Vain","the Arrogant","the Proud",
    "the Stubborn","the Loud","the Quick","the Slow","the Lazy","the Restless","the Alert","the Cautious","the Reckless","the Careful",
    "the Careless","the Clever","the Simple","the Witty","the Dull","the Sharp","the Keen","the Observant","the Forgetful",
    "the Brooding","the Cheerful","the Gloomy","the Merry","the Serious","the Playful","the Fierce","the Warrior","the Conqueror","the Victorious",
    "the Defeated","the Battle-scarred","the Iron","the Steel","the Sharp","the Terrible","the Fearsome","the Dreadful","the Invincible",
    "the Undefeated","the Slayer","the Hunter","the Defender","the Guardian","the Protector","the Hammer","the Blade","the Shield",
    "the Unknown","the Forgotten","the Beloved","the Hated","the Feared","the Scorned","the Exiled","the Banished",
    "the Outcast","the Wanderer","the Lost","the Found","the Chosen","the Cursed","the Blessed","the Young",
    "the Old","the Ancient","the Elder","the Younger","the First","the Last","the Late","the Early","the Timeless","the Wild",
    "the Tame","the Free","the Bound","the Rock"]