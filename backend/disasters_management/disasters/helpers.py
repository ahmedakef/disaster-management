from disasters.models import GeoJSON


def create_point(lang, lat):
    center_point = {
        "type"          :   "Point",
        "coordinates"   :   [lang, lat]  
    }
    center_point = GeoJSON(**center_point)
    return center_point