from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

#choose an image to work with
im = Image.open("DonaldTrump.jpg")
#print(im.size)

data = im.getdata()
data_list = list(data)
length = len(data_list)

#this is the new list that your new tuples will appear in
picture_list = []

#this for loop adds up the intensity and sorts the tuples into the corresponding color
for tuple in data_list:
	total = tuple[0] + tuple[1] + tuple[2]
	if total <=182:
		picture_list.append(darkBlue)
		#color it dark blue (low intensity)
	elif total >182 and total <=364:
		picture_list.append(red)
		#color it red (med/low intensity)
	elif total >364 and total <=546:
		picture_list.append(lightBlue)
		#color it light blue (med/high intensity)
	else:
		picture_list.append(yellow)
		#color it yellow (high intensity)

#new_image = Image.new("RGB", (620, 412))
new_image = Image.new(im.mode, im.size)

im.putdata(data, 1.0, 0.0)
new_image.putdata(picture_list)
new_image.show()
new_image.save("NewDonaldTrump.jpg", "jpeg")
