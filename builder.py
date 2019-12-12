import general_methods as gms
import ArtworkObject as obj

# Converts Collection into list of Artwork Objects
def build_artwork_objects(art_collection):
    try:
        pieces = []
        for piece in art_collection['assets']:
            pieces.append(obj.Artwork(piece))
        return pieces
    except:
        print('This Address has no Art')

def buildIt(owner_addr):
    collection = gms.get_collection(owner_addr)
    return build_artwork_objects(collection)
