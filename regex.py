# import re 

# xyz=r'[a-z]'
# text="the trustees have Hello approved the following updated policy document"

# match=re.findall(xyz,text)

# print(match)

#####################################################################

# ai=r'[A-Z]'


# ai=r'v*' #to find how many v's are there 
# ai=r'v+' 
# ai=r't{3}'
# ai=r'\s' #to identify how many spaces are there 
# ai=r'\S' #it will print everything except space
# ai=r'\W' #except alphabetical numbers or numericals it will print everythin ex: _?.
# ai=r'\w' #it will print everything with _?>!


# ai=r''
# text="if you tttrouble the tttttrouble the trouble will trouble you "

# match=re.findall(ai,text)

# print(match)

# xyz= r"Divakar"

# x="My name is Divakar"

# match= re.match(xyz,x)

# if match:
#     print("Match found ",match.group())
# else:
#     print("Match not found")

#############################################################

# # Input string
# text = "123 4567 89 01234"

# # Regex pattern to match 2 to 4 digit numbers
# pattern = r'\b\d{2,4}\b'

# # Find all matches
# matches = re.findall(pattern, text)

# print(matches)

###############################################################

# Input string
# text = "This is a test of the regex function."

# Regex pattern to match words with exactly 4 characters
# pattern = r'\b\w{4}\b'

# Find all matches
# matches = re.findall(pattern, text)

# print(matches)

##############################################################

# import re

# xyz=r'name'

# x='My name is Divakar'

# match=re.match(xyz,x)

# if match:
#     print('match :', match.group())
# else:
#     print('No match ')


#VALIDATION USING REGEX

# import re 

# mob="+91-6281253955"
# xyz=r'^\+?\d{1,3}[-\s]?\d{10}$'

# if re.match(xyz,mob):
#     print("valid no.")
# else:
#     print("Invalid ")

########################################################

#email validation

# import re 

# x="Bojugu2524_%#@gmail.com"

# # xyz=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+@[a-z]+\.[a-z]{2,3}$'
# xyz=r'^[A-Za-z0-9_%#]+@[a-z]+\.[a-z]{2,3}$'

# if re.match(xyz,x):
#     print("valid email ")
# else:
#     print("Invalid")

####################################################
#password validation
# import re 

# password="Divakar@22"

# # xyz=r'^[A-Za-z](?=.\d)(?=.*[@$!%&])[A-Za-z\d@$!%]{10,}'

# xyz=r'(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!%&])[A-Za-z\d@4!%]{10,}'


# if re.match(xyz,password):
#     print("divakar nedhi gattigundhirooo..  ")
# else:
#     print("varun nedhi methagundhirooo...")

########################################################

# import re

# xyz=r'^[a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]*@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'


# x=["bojugu2524@gmail.com","Divakar$%@gmail.com","Kevinmathew1217@gmail.com"]

# for email in x:
#     if re.match(xyz,x):
#         print(f"{x}" "Valid E-mail")
#     else:
#         print(f"{x}" "Invalid E-mail")

import re

xyz="""Amazon.in Bestsellers: The most popular items on Amazon





























Skip to



Main content





      Keyboard shortcuts






Search

alt
+
/







Cart

shift
+
alt
+
c







Home

shift
+
alt
+
h







Orders

shift
+
alt
+
o





Show/hide shortcuts, shift, alt, z

Show/Hide shortcuts

shift
+
alt
+
z

















.in









                   Delivering to Mumbai 400001


                   Update location





















All


Select the department you want to search in

All Categories
Alexa Skills
Amazon Devices
Amazon Fashion
Amazon Fresh
Amazon Fresh Meat
Amazon Pharmacy
Appliances
Apps & Games
Audible Audiobooks
Baby
Beauty
Books
Car & Motorbike
Clothing & Accessories
Collectibles
Computers & Accessories
Deals
Electronics
Furniture
Garden & Outdoors
Gift Cards
Grocery & Gourmet Foods
Health & Personal Care
Home & Kitchen
Industrial & Scientific
Jewellery
Kindle Store
Luggage & Bags
Luxury Beauty
Movies & TV Shows
MP3 Music
Music
Musical Instruments
Office Products
Pet Supplies
Prime Video
Shoes & Handbags
Software
Sports, Fitness & Outdoors
Subscribe & Save
Tools & Home Improvement
Toys & Games
Under ₹500
Video Games
Watches













Search Amazon.in

























EN





Hello, sign in
Account & Lists



Returns
& Orders










        Cart













All










Fresh
MX Player
Sell
Best Sellers
Mobiles
Today's Deals
Prime
Customer Service
 Electronics
Home & Kitchen
Amazon Pay
New Releases
Fashion
Computers
Car & Motorbike
Books
Toys & Games
Sports, Fitness & Outdoors
Beauty & Personal Care
Gift Cards
Home Improvement
Custom Products
Health, Household & Personal Care
Grocery & Gourmet Foods
Video Games
Baby
Pet Supplies
Audible
Gift Ideas
AmazonBasics
Subscribe & Save
Kindle eBooks






































BestsellersHot New ReleasesMovers and ShakersMost Wished ForMost Gifted













Amazon BestsellersOur most popular products based on sales.  Updated frequently.Bestsellers










Any DepartmentAmazon LaunchpadAmazon RenewedApps for AndroidBaby ProductsBags, Wallets and LuggageBeautyBooksCar & MotorbikeClothing & AccessoriesComputers & AccessoriesElectronicsGarden & OutdoorsGift CardsGrocery & Gourmet FoodsHealth & Personal CareHome & KitchenHome ImprovementIndustrial & ScientificJewelleryKindle StoreMovies & TV ShowsMusicMusical InstrumentsOffice ProductsPet SuppliesShoes & HandbagsSoftwareSports, Fitness & OutdoorsToys & GamesVideo GamesWatches










 Bestsellers in Industrial & ScientificSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Konvio Neer Imported Tds Meter, Total Dissolved Solids Meter, Water Quality Tester, Ppm Tester For Water Testing - White4.3 out of 5 stars 45,027#2Daluci Anti Pollution N95 Reusable Unisex Non Woven fabric Face Mask, Ear Loop Style (Pack of 10) Protective Fold Flat Mask With 5 Layered Filtration, Without Valve3.9 out of 5 stars 10,512#3Dr Trust USA Compressor Nebulizer Machine Complete Kit for Adults and Kids with Mask (White)4.2 out of 5 stars 26,800#4Dr. Fixit Kwik N Ezee Wall Gap & Crack Filler, 150gm (White), DIY Waterproofing for Home Repairs, Kitchen Sink & Wall Cracks, Bathroom Tile Gaps Sealant, Metal, Wood, PVC, Best for Wet & Damp areas3.7 out of 5 stars 7,695#5REDCOP® Isopropyl Alcohol 99.9% Pure [(CH3)2-CH-OH] CAS: 67-63-0] 300ml Rubbing Alcohol4.3 out of 5 stars 2,428#6UB Unity Brand Super Strong Adhesive Waterproof tape Permanent Repair Roof Water Leakage Solution Rubber Foil Suitable for Roof Leak, surface Crack, Window Sill Gap, Boat Sealing, Tank Leak (5CM*5M)4.5 out of 5 stars 561Next page






 Bestsellers in Grocery & Gourmet FoodsSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Tata Salt 1 Kg, Free Flowing and Iodised Namak, Vacuum Evaporated, Salt in Fresh4.5 out of 5 stars 67,548#2Tata Sampann Unpolished Toor Dal/Arhar Dal, 1kg4.5 out of 5 stars 32,112#3Fortune Sunlite Refined Sunflower Oil, 1L4.4 out of 5 stars 37,205#4Fortune Premium Kachi Ghani Pure Mustard Oil, 1Litre PET Bottle4.4 out of 5 stars 45,943#5Amazon Brand - Vedaka Cumin (Safed Zeera) whole, 100 g4.4 out of 5 stars 28,157#6Fortune Premium Kachi Ghani Pure Mustard Oil, 1 ltr pouch4.4 out of 5 stars 32,164Next page






 Bestsellers in Car & MotorbikeSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1SOFTSPUN Microfiber Cloth - 4 pcs - 40x40 cms - 340 GSM Grey! Thick Lint & Streak-Free Multipurpose Cloths - Automotive Microfibre Towels for Car Bike Cleaning Polishing Washing & Detailing.4.3 out of 5 stars 93,454#2Jopasu Car Duster4.4 out of 5 stars 40,111#3Godrej aer O – Hanging Car Air Freshener – Assorted Pack of 3 (22.5g) | Gel Lasts up to 30 days | Car Accessories4.2 out of 5 stars 1,926#4ShineXPro Microfiber Car Cleaning Cloth - OG Soft 500 GSM Extra Large (35x75 CM) Microfiber Cloth for Car and Bike - Suede Edging for Scratchless Drying and Detailing (Pack of 2, Grey)4.3 out of 5 stars 13,907#5Boldfit Full Face Helmet Mask for Bikers in Riding UV Protected, Balaclava, Black Mask for Bike Riding and Cycling Accessories Mask for Men & Women4.1 out of 5 stars 5,701#6Involve Your Senses One Musk Organic Car Perfume, Involve Your Senses Strong Fiber Air Freshener to Freshen'up Your Car - IONE01-40 g,Car Accessories interior car perfumes and fresheners3.8 out of 5 stars 26,768Next page






 Bestsellers in Gift CardsSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Google Play recharge code - Digital Voucher4.3 out of 5 stars 279,677#2Amazon Pay eGift Card4.5 out of 5 stars 205,723#3Amazon Pay eGift Card4.5 out of 5 stars 205,723#4Reliance Retail | Flat 3% off | E-Gift Card | Instant Delivery | Valid for in-store purchases |1 year Validity5.0 out of 5 stars 5#5Google Play Gift Card| 2% Flat Cashback | Instant Delivery | Valid for online purchase | Redeemable on Play Store4.1 out of 5 stars 143#6App Store Codes4.1 out of 5 stars 260Next page






 Bestsellers in ElectronicsSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1realme NARZO 70x 5G (Ice Blue, 6GB RAM,128GB Storage)|120Hz Ultra Smooth Display|Dimensity 6100+ 6nm 5G|50MP AI Camera|45W Charger in The Box4.1 out of 5 stars 4,365#2boAt Rockerz 255 Pro+, 60HRS Battery, Fast Charge, IPX7, Dual Pairing, Low Latency, Magnetic Earbuds, Bluetooth Neckband, Wireless with Mic Earphones (Active Black)4.0 out of 5 stars 206,013#3realme NARZO N61 (Voyage Blue,4GB RAM+64GB Storage) 90Hz Eye Comfort Display | IP54 Dust & Water Resistance | 48-Month Fluency | Charger in The Box4.0 out of 5 stars 1,456#4Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)4.3 out of 5 stars 2,562#5Redmi A4 5G (Sparkle Purple, 4GB RAM, 128GB Storage) | Global Debut SD 4s Gen 2 | Segment Largest 6.88in 120Hz | 50MP Dual Camera | 18W Fast Charging4.0 out of 5 stars 581#6boAt Bassheads 100 in Ear Wired Earphones with Mic(Black)4.1 out of 5 stars 412,589Next page






 Bestsellers in JewellerySee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Elina Dark Multi Color Elastic Hair Ponytail Holder Soft Non Slip Tight Stretchable Rubber Bands for School Girls/Women, Hair tie (Pack of 30)(Dark English Multicolor)4.4 out of 5 stars 692#2Shining Diva Fashion 26 Pcs Colorful Hair Accessories Hair Clips for Girls Kids Baby Girl Toddlers Women Hairband Hair Band Ties4.3 out of 5 stars 875#3Gold Plated Invisible Transparent Stretchable and Adjustable Lightweighted Elastic Heavy Earrings Support Ear Chains (2 Pair) And Invisible Ear Lobe Support for Earrings Earlobe Tapes and Stickers Earring Supporter for Heavy Earrings Support Patches Girls & Women (Pack 20)3.5 out of 5 stars 27#4JEWILLEY Floral Kundan Studded Matha Patti Sheesh Patti Wedding Hairband Traditional Golden Celebrity Headband Hair accessory Jewellery for Women and Girls4.3 out of 5 stars 101#5Zeneme Traditional Brass 18 K Gold Plated Wedding Jewellery Bahubali Inspired Long Chain Jhumki Earrings for Women and Girl4.1 out of 5 stars 300#6Shining Diva Fashion Latest Stylish Multilayer Gold Plated Bangle Bracelet for Women and Girls (rr14669b) Set of 63.5 out of 5 stars 540Next page







About BestsellersThese frequently updated lists contain bestselling items.





























                    Your recently viewed items and featured recommendations      ›    View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.         Your recently viewed items and featured recommendations      ›    View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.   





    Back to top






Get to Know Us


About Amazon


Careers


Press Releases


Amazon Science





Connect with Us


Facebook


Twitter


Instagram





Make Money with Us


Sell on Amazon


Sell under Amazon Accelerator


Protect and Build Your Brand


Amazon Global Selling


Supply to Amazon


Become an Affiliate


Fulfilment by Amazon


Advertise Your Products


Amazon Pay on Merchants





Let Us Help You


Your Account


Returns Centre


Recalls and Product Safety Alerts


100% Purchase Protection


Amazon App Download


Help

















English



India






AbeBooksBooks, art& collectibles
Amazon Web ServicesScalable CloudComputing Services
AudibleDownloadAudio Books
IMDbMovies, TV& Celebrities
 

ShopbopDesignerFashion Brands

Amazon BusinessEverything ForYour Business
Prime Now 2-Hour Deliveryon Everyday Items
Amazon Prime Music100 million songs, ad-freeOver 15 million podcast episodes



Conditions of Use & Sale Privacy Notice Interest-Based Ads © 1996-2025, Amazon.com, Inc. or its affiliates


















PS C:\divakar>































"""
x=r'\b.\b'

match=re.findall(x,xyz)
print(match)

