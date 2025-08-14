from random import choice

def generate_name(names_list:list) -> tuple:
	forname:str = choice(names_list)
	surname:str = choice(names_list) + "son"
	return forname, surname


names = ["Aghi", "Agmundr", "Agnarr", "Agni", "Áki", 
		"Áleifr", "Alfarr", "Alfríkr", "Alfvin", 
		"Algautr", "Anundr", "Ari", "Arnfinnr", 
		"Árni", "Árni", "Arnórr", "Arnsteinn", 
		"Arnþórr", "Arnviðr", "Ásbjǫrn", "Ásgeirr",
		"Ásketill", "Ásmundr", "Ásvaldr", "Aðalsteinn",
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