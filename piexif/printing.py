import piexif
exif_dict = piexif.load("lim.jpg") # will have to error handle if file doesnt exist or not found

for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])
