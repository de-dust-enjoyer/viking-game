import re

# Raw HTML content from the webpage
html_content = """
[Ælfheah](/name/ae32lfheah) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ælf](/element/ae32lf) "elf" and
[heah](/element/heah) "high". This was the name of an 11th-century archbishop of Canterbury, a saint and martyr, who is commonly known as Alphege or Elphege.
[Ælfric](/name/ae32lfric) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ælf](/element/ae32lf) "elf" and
[ric](/element/ric) "ruler, king" (making it a cognate of
[Alberich](/name/alberich)). This was the name of a 10th-century archbishop of Canterbury, sometimes considered a saint.
[Ælfwine](/name/ae32lfwine) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ælf](/element/ae32lf) "elf" and
[wine](/element/wine) "friend". This name was not commonly used after the Norman Conquest.
[Æsc](/name/ae32sc) m [Anglo-Saxon](/names/usage/anglo-saxon)Means
"ash tree" in Old English. This was the nickname of a 5th-century king of Kent, whose birth name was Oeric.
[Æþelbeorht](/name/ae32th31elbeorht) m [Anglo-Saxon](/names/usage/anglo-saxon)Old English cognate of
Adalbert (see
[Albert](/name/albert)). This was the name of a Saxon king of England and two kings of Kent, one of whom was a saint. It became unused after the Normans introduced their form of
Adalbert after their invasion.
[Æðelfrið](/name/ae32th30elfrith30) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[æðele](/element/ae32th30ele) "noble" and
[friþ](/element/frith31) "peace". The name was rarely used after the Norman Conquest.
[Æðelmær](/name/ae32th30elmae32r) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[æðele](/element/ae32th30ele) "noble" and
[mære](/element/mae32re) "famous". A famous bearer was the 11th-century English monk Æðelmær of Malmesbury who attempted to fly with a gliding apparatus (breaking his legs in the process).
[Æðelræd](/name/ae32th30elrae32d) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[æðele](/element/ae32th30ele) "noble" and
[ræd](/element/rae32d) "counsel, advice". This was the name of two Saxon kings of England including Æðelræd II "the Unready" whose realm was overrun by the Danes in the early 11th century. The name was rarely used after the Norman Conquest.
[Æðelric](/name/ae32th30elric) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[æðele](/element/ae32th30ele) "noble" and
[ric](/element/ric) "ruler, king". This was the name of several early Anglo-Saxon kings.
[Æðelstan](/name/ae32th30elstan) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[æðele](/element/ae32th30ele) "noble" and
[stan](/element/stan) "stone". This was the name of a 10th-century English king, the first to rule all of England. The name was rarely used after the Norman Conquest, though it enjoyed a modest revival (as
[Athelstan](/name/athelstan)) in the 19th century.
[Æðelwine](/name/ae32th30elwine) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[æðele](/element/ae32th30ele) "noble" and
[wine](/element/wine) "friend". This was the name of a few Anglo-Saxon saints, including a 7th-century bishop of Lindsey. The name became rare after the Norman Conquest.
[Æðelwulf](/name/ae32th30elwulf) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[æðele](/element/ae32th30ele) "noble" and
[wulf](/element/wulf) "wolf" (making it a cognate of
[Adolf](/name/adolf)). This name was borne by a 9th-century king of Wessex.
[Botwulf](/name/botwulf) m [Anglo-Saxon](/names/usage/anglo-saxon)From Old English
[bot](/element/bot-2) meaning "improvement" and
[wulf](/element/wulf) meaning "wolf". Saint Botwulf was a 7th-century English abbot. He may be the person after whom
[Boston](//places.behindthename.com/name/boston) is named.
[Cola](/name/cola) m [Anglo-Saxon](/names/usage/anglo-saxon)Old English byname meaning
"charcoal", originally given to a person with dark features.
[Dunstan](/name/dunstan) m [English (Rare)](/names/usage/english), [Anglo-Saxon](/names/usage/anglo-saxon)From the Old English elements
[dunn](/element/dunn) "dark" and
[stan](/element/stan) "stone". This name was borne by a 10th-century saint, the archbishop of Canterbury. It was occasionally used in the Middle Ages, though it died out after the 16th century. It was revived by the Tractarian movement in the 19th century.
[Eadberht](/name/eadberht) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ead](/element/ead) "wealth, fortune" and
[beorht](/element/beorht) "bright". This was the name of an 8th-century king of Northumbria and three kings of Kent.
[Eadræd](/name/eadrae32d) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ead](/element/ead) "wealth, fortune" and
[ræd](/element/rae32d) "counsel, advice". This was the name of a 10th-century English king.
[Eadwald](/name/eadwald) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ead](/element/ead) "wealth, fortune" and
[weald](/element/weald-1) "powerful, mighty". This was the name of an 8th-century king of East Anglia.
[Eadwig](/name/eadwig) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ead](/element/ead) "wealth, fortune" and
[wig](/element/wig) "war". This was the name of a Saxon king of England in the 10th century. The name fell out of use after the Norman Conquest.
[Eadwulf](/name/eadwulf) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[ead](/element/ead) "wealth, fortune" and
[wulf](/element/wulf) "wolf". This name fell out of use after the Norman Conquest.
[Ealdhelm](/name/ealdhelm) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[eald](/element/eald) "old" and
[helm](/element/helm) "helmet, protection". This was the name of a 7th-century English saint (commonly called
Aldhelm).
[Ealdræd](/name/ealdrae32d) m [Anglo-Saxon](/names/usage/anglo-saxon)From the Old English elements
[eald](/element/eald) "old" and
[ræd](/element/rae32d) "counsel, advice". This name was rarely used after the Norman Conquest.
[Glædwine](/name/glae32dwine) m [Anglo-Saxon](/names/usage/anglo-saxon)Old English name derived from the elements
[glæd](/element/glae32d) "bright, cheerful, glad" and
[wine](/element/wine) "friend". This name was not actually recorded in the Old English era, though it is attested starting in the 11th century.
[Godric](/name/godric) m [Anglo-Saxon](/names/usage/anglo-saxon)Means
"god's ruler", derived from Old English
[god](/element/god-1) combined with
[ric](/element/ric) "ruler, king". This name died out a few centuries after the Norman Conquest.
[Godwine](/name/godwine) m [Anglo-Saxon](/names/usage/anglo-saxon)Means
"friend of god", derived from Old English
[god](/element/god-1) combined with
[wine](/element/wine) "friend". This was the name of the powerful 11th-century Earl of Wessex, the father of King Harold II of England.
[Heard](/name/heard) m [Anglo-Saxon](/names/usage/anglo-saxon)Short form of various Old English names containing the element
[heard](/element/heard) meaning
"hard, firm, brave, hardy".
[Hereward](/name/hereward) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[here](/element/here-1) "army" and
[weard](/element/weard) "guard". This was the name of an 11th-century Anglo-Saxon leader who rebelled against Norman rule.
[Hroðgar](/name/hroth30gar) m [Anglo-Saxon](/names/usage/anglo-saxon)From Old English
[hroð](/element/hroth30) "fame, glory" and
[gar](/element/gar) "spear", making it a cognate of
Hrodger (see
[Roger](/name/roger)). The name became unused after the Normans introduced the continental form. In the Old English poem
Beowulf this is the name of the Danish king. The same character is named in Scandinavian sources as
[Hróarr](/name/hro10arr).
[Leofwine](/name/leofwine) m [Anglo-Saxon](/names/usage/anglo-saxon)Means
"dear friend", derived from the Old English elements
[leof](/element/leof) "dear, beloved" and
[wine](/element/wine) "friend". This was the name of an 8th-century English saint, also known as
Lebuin, who did missionary work in Frisia.
[Sigeberht](/name/sigeberht) m [Anglo-Saxon](/names/usage/anglo-saxon)Means
"bright victory", derived from Old English
[sige](/element/sige) "victory" and
[beorht](/element/beorht) "bright" (a cognate of
[Siegbert](/name/siegbert)). This was the name of a king of Wessex. The name fell out of use after the Norman Conquest.
[Wærmund](/name/wae32rmund) m [Anglo-Saxon](/names/usage/anglo-saxon)From Old English
[wær](/element/wae32r) "aware, cautious" and
[mund](/element/mund) "protection", making it a (partial) cognate of
[Veremund](/name/veremund). This was the name of a legendary ancestor of the Mercians according to the
Anglo-Saxon Chronicle.
[Waltheof](/name/waltheof) m [Anglo-Saxon](/names/usage/anglo-saxon)Old English name derived from the Old Norse
[Valþjófr](/name/valth31jo10fr). This was the name of a 12th-century English saint, an abbot of Melrose.
[Wigberht](/name/wigberht) m [Anglo-Saxon](/names/usage/anglo-saxon), [Germanic](/names/usage/germanic)Derived from the Old English elements
[wig](/element/wig) "battle" and
[beorht](/element/beorht) "bright". This is also a continental Germanic equivalent, derived from the Old German elements
[wig](/element/wig) and
[beraht](/element/beraht). The name was borne by an 8th-century English saint who did missionary work in Frisia and Germany.
[Wulfnoð](/name/wulfnoth30) m [Anglo-Saxon](/names/usage/anglo-saxon)Derived from the Old English elements
[wulf](/element/wulf) "wolf" and
[noð](/element/noth30) "boldness, daring". This name became rare after the Norman Conquest.
"""

# Extract names using regex pattern
# Look for names in square brackets at the start of lines
name_pattern = r'\[([^\]]+)\]\(/name/[^\)]+\) m \[Anglo-Saxon\]'
matches = re.findall(name_pattern, html_content)

# Clean up the names by removing HTML entities and converting special characters
anglo_saxon_names = []
for name in matches:
    # Replace common HTML entities with their Unicode equivalents
    clean_name = (name
                  .replace('æ', 'æ')  # This should already be correct
                  .replace('þ', 'þ')   # Thorn
                  .replace('ð', 'ð')   # Eth
                  .replace('ae32', 'æ') # HTML entity for æ
                  .replace('th30', 'ð') # HTML entity for ð
                  .replace('th31', 'þ') # HTML entity for þ
                  .replace('32', '')    # Remove remaining numbers
                  .replace('30', '')    # Remove remaining numbers
                  .replace('31', '')    # Remove remaining numbers
                  .replace('10', ''))   # Remove remaining numbers
    
    anglo_saxon_names.append(clean_name)

# Remove duplicates and sort
anglo_saxon_names = sorted(list(set(anglo_saxon_names)))

# Print the Python list
print("# Anglo-Saxon Masculine Names")
print("anglo_saxon_masculine_names = [")
for name in anglo_saxon_names:
    print(f'    "{name}",')
print("]")

print(f"\n# Total count: {len(anglo_saxon_names)} names")

# Also create a simple list without formatting for easy copying
print("\n# Simple list format:")
print(anglo_saxon_names)