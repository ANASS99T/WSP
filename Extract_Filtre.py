from Connection_Collection import *

def get_data(soup_div):
    data = {}

    try:
        name = soup_div.find('span', {'class': 'feed-shared-actor__name t-14 t-black t-bold hoverable-link-text'}).text
                             
        if name:
            data["name"] = name.replace("\n", "")
    except:
        a = 1
        #print("can't get the name")

    try:
        work = soup_div.find('span', {'class': 'feed-shared-actor__description t-12 t-black--light t-normal'}).text
                             
        if work:
            data["work"] = work.replace("\n", "")
    except:
        a = 1
        #print("can't get the work infos")

    try:
        image_link = soup_div.find('img', {'class': 'ivm-view-attr__img--centered EntityPhoto-circle-3 feed-shared-actor__avatar-image presence-entity__image EntityPhoto-circle-3 lazy-image loaded ember-view'})['src']

        if image_link:
            data["image"] = image_link
    except:
        a = 1
        #print("can't get the image link")

    try:
        text = soup_div.find('div', {'class': 'feed-shared-text__text-view feed-shared-text-view white-space-pre-wrap break-words ember-view'}).text
                             
        if text:
            data["description"] = text.replace("\n", "")
    except:
        a = 1
        #print("can't get the description")

    try:
        match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        mail = match.group(0)
        if mail:
             data["email"] = mail
    except:
        a = 1
        #print("can't get the email")

    return data




def Extract(name_div):
    Extracted = []

    for item in name_div:
        d = get_data(item)
        if d.keys():
            Extracted.append(d)
    return Extracted


def Filtre(Extracted):

    Dict = {"job": 1,
            "offer": 1,
            "recrutons": 1,
            "CDI": 1,
            "Envoyez votre cv": 1,
            "Envoyez cv": 1,
            "lettre de motivation": 1,
            "WANTED": 1,
            "Contrat": 1,
            "#Emploi": 1,
            "recherche": 1,
            "Développeur": 1,
            "Ingénieur": 1,
            "Engineer": 1,
            "Looking for": 1,
            "recrutement": 1,
            "POSTE PROPOSÉ": 1,
            "PROFIL RECHERCHÉ ": 1,
            "Nous recherchons": 1,
            "Nous offrons": 1,
            "Maitrise": 1,
            "join": 1,
            "offre": 1,
            "carrer" :1,
            "carrière": 1,
            "#carrer" :1,
            "Techniciens": 1,
            "profils": 1,
            "project manager": 1,
            "business development": 1,
            "poste": 1,
            "mission": 1,
            "chargé de mission": 1,
            "chef d'équipe": 1,
            "expérience": 1,
            "stage": 1,
            "Entretien": 1,
            "candidatures": 1,

            }

    Filtered = []

    for Ex in Extracted:
        value = 0
        for key in Dict.keys():
            if key.lower() in str(Ex).lower():
                value = value + Dict[key]
        if value > 0:
            Filtered.append(Ex)
    return Filtered



def email(Filtered):
    NewFiltered = []
    for F in Filtered:
        for f in F.keys():
            if "email" == f:
                NewFiltered.append(F)
    return NewFiltered





