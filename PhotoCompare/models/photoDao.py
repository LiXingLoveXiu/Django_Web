from models import Photo


def addFavorNum(photoId):
    photo = Photo.objects.get(id=photoId)
    tmp = photo.favorNum
    tmp += 1

    photo.favorNum = tmp
    photo.save()
