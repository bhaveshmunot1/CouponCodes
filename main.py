import re
from ClassWebScrapping import WebScrapping 
from ClassLogging import Logging
from ClassFileOperations import FileOperations
from ClassJSON import *
from Categorizer import *

LINKS = [[" PromoCodeClub ", " Freecharge ", "http://promocodeclub.com/freecharge-promo-code-and-coupons/"],
         [" PromoCodeClub ", " Mobikwik ", "http://promocodeclub.com/mobikwik-promo-code-and-coupons/"],
         [" PromoCodeClub ", " Paytm ", "http://promocodeclub.com/paytm-promo-code-and-coupons/"]]
ListOfOffers = []

objLogging = Logging(3)
objFileOp = FileOperations()

def Tag(text, dictionary, tags_list):
    bIsAttached = False
    text = text.lower()
    for key in dictionary:
        if key in text:
            bIsAttached = True
            tags_list.append(dictionary[key])
    return bIsAttached


def FindDiscount(text):

	num = re.search('(\d)+', text)
	if num != None :
		return num.group(0)

	return '0'


def AddSimpleTags(text):

    tags_list = []
    if not Tag(text, users_categorizer, tags_list) :
        tags_list.append('All Users')
    if not Tag(text, type_categorizer, tags_list) :
        objLogging.log(1, "Didn't attach type tag...")
    if not Tag(text, airtel_categorizer, tags_list) :
        tags_list.append('Airtel and Others')
    if not Tag(text, offerdeal_categorizer, tags_list) :
        tags_list.append('Deal')

    return tags_list

def GetOffersDealsList(CompleteList) :
	Offers = []
	Deals = []

	for item in CompleteList:
		if 'Offer' in item['Tags'] :
			Offers.append(item)
		else :
			Deals.append(item)

	return [Offers, Deals]

def PromoCodeClubDotCom(link, name, tag_name):

    # Initialize and get source code
    ObjPromocodeclub = WebScrapping(link, name)
    objLogging.log(0, ObjPromocodeclub)
    
    # Get List of offers
    CompleteList = ObjPromocodeclub.GetListByDivAndClass("jcorgcr-hover-container")
    objLogging.log(0, len(CompleteList))

    # Display each offers    
    for eachItem in CompleteList:
        offer_object = {}
        offer_object['Site'] = tag_name
        
        # Get full info
        details = ObjPromocodeclub.GetChildren(eachItem.div)
        
        # Get Title
        objLogging.log(2, ObjPromocodeclub.TagText(details[1]))
        offer_object['Title'] = ObjPromocodeclub.TagText(details[1])                
        
        # Get Body
        couponCode = ObjPromocodeclub.GetParsed(str(details[5]))              
        temp = ObjPromocodeclub.GetChildren(couponCode.body.ul)
        
        # Get Description
        description = temp[1]
        objLogging.log(2, description.get_text())
        offer_object['Description'] = description.get_text()
                
        # Get Promo Code
        promocode = ObjPromocodeclub.GetChildren(temp[3])[1]        
        objLogging.log(2, promocode.get_text())
        offer_object['Promocode'] = promocode.get_text()
                
        tags_list = AddSimpleTags(ObjPromocodeclub.TagText(details[1]) + " " + description.get_text())                
        offer_object['Tags'] = tags_list

        discount = FindDiscount(description.get_text())
        offer_object['Discount'] = int(discount)

        ListOfOffers.append(offer_object)
        # Print splitter line
        objLogging.PrintLine(2)                
        
if __name__ == "__main__":       
    
    for link in LINKS:  
        objLogging.log(2, " \n ************* " + link[0] + " " + link[1] + " *************\n")
        PromoCodeClubDotCom(link[2], link[0] + "-" + link[1]+".html", link[1])

    Offers, Deals = GetOffersDealsList(ListOfOffers)

    Offers = sorted(Offers, key = lambda k : k['Discount'], reverse = True)
    Deals = sorted(Deals, key = lambda k : k['Discount'], reverse = True)

    offersJSONObj = JSONify(Offers)
    dealsJSONObj = JSONify(Deals)
    
    JSONtoCSV(offersJSONObj)