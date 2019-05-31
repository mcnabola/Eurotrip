import piexif
import piexif.helper
exif_dict = piexif.load("lim.jpg")
user_comment = piexif.helper.UserComment.load(exif_dict["Exif"][piexif.ExifIFD.UserComment])
print(user_comment)

#keyerror: 37510 - this is the value of userComment tag in the document
