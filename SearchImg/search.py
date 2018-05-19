# -*- coding: utf-8 -*-

from django.shortcuts import render
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from search_image import engine
import shutil
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


classes = {'people': 0, 'sea': 1, 'building': 2, 'bus': 3, 'dinosaur': 4, 'elephant': 5,
           'flower': 6, 'horse': 7, 'mountain': 8, 'food': 9}


@csrf_exempt
def search(request):
    data = request.FILES['img']
    try:
        img_class = classes[request.POST['class']]
    except:
        img_class = -1
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'target.jpg')):
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'target.jpg'))
    default_storage.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'target.jpg'),
                         ContentFile(data.read()))
    engine.store_imgs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image.orig'))
    img_paths = engine.query_img(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'target.jpg'))
    count = 0
    for idx, img_path in enumerate(img_paths):
        if int(os.path.basename(img_path).replace('.jpg', '')) // 100 == img_class:
            count = count + 1
        shutil.copy(img_path, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/rs/{}.jpg').format(idx))
    imgs = map(lambda x: '/static/rs/{}.jpg'.format(x), range(0, 50))
    acc = count / 50 if img_class != -1 else -1
    return render(request, 'show_img.html', {'imgs': imgs, 'acc': acc})
