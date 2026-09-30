from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import GalleryAlbum, GalleryPhoto, GalleryVideo

def gallery_list_view(request):
    albums = GalleryAlbum.objects.prefetch_related('photos').all()
    videos = GalleryVideo.objects.all()
    all_photos = GalleryPhoto.objects.select_related('album').all()

    tab = request.GET.get('tab', 'albums')

    context = {
        'albums': albums,
        'videos': videos,
        'all_photos': all_photos[:24],
        'tab': tab,
        'page_title': "Galerie Multimédia - Pissy Vibes",
    }
    return render(request, 'gallery/gallery_list.html', context)

def album_detail_view(request, slug):
    album = get_object_or_404(GalleryAlbum, slug=slug)
    photos = album.photos.all()
    context = {
        'album': album,
        'photos': photos,
        'page_title': f"{album.title} - Galerie Pissy Vibes",
    }
    return render(request, 'gallery/album_detail.html', context)
