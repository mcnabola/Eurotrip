import piexif
import piexif.helper

"""
Returns exif data as a dictionary with the following keys: “0th”, “Exif”, “GPS”, “Interop”, “1st”, and “thumbnail”. All values are dictionaries except for “thumbnail” which has the value of either a JPEG as bytes or None if no thumbnail is stored in the exif data.

Parameters:	filename (str) – JPEG, WebP, or TIFF
Returns:	Exif data({“0th”:dict, “Exif”:dict, “GPS”:dict, “Interop”:dict, “1st”:dict, “thumbnail”:bytes})
"""

exif_dict = piexif.load("lim.jpg")

for ifd_name in exif_dict:
    print("\n{0} IFD:".format(ifd_name))
    for key in exif_dict[ifd_name]:
        print(piexif.TAGS[ifd_name][key]["name"], exif_dict[ifd_name][key])

# modified version of code from readthedocs - prints all data 
#doesnt handle the raw data for thumbnail


""" Hnadling the removal of the thumbnail
thumbnail = exif_dict.pop("thumbnail")
if thumbnail is not None:
    with open("thumbnail.jpg", "wb+") as f:
        f.write(thumbnail)
"""
