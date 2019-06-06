import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # récupère le fichier
        # défini le nom du fichier avec une chaine de caractère aléatoire
        filename = '{}.{}'.format(uuid4().hex, ext)
        # renvoie tout le chemin jusqu'au fichier.
        return os.path.join(self.sub_path, filename)    

