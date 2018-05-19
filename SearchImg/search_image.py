import os
import numpy as np
from vgg import vgg16
import glob
import sys
import shutil


class ImgSearchEngine(object):
    def __init__(self):
        self.vgg = vgg16(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vgg16_weights.npz'))

    def store_imgs(self, img_dir):
        img_paths = glob.glob(os.path.join(img_dir, '*'))

        for idx, img_path in enumerate(img_paths):
            if os.path.exists(img_path.replace('.jpg', '.npy')):
                continue
            np.save(img_path.replace('.jpg', '.npy'), self.vgg.get_feat(img_path))

    def query_img(self, img_path):
        feat = self.vgg.get_feat(img_path)
        feat_paths = np.array(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image.orig/*.npy')))
        feats = np.array([np.load(f) for f in feat_paths])
        dis = np.linalg.norm(feat - feats, axis=-1)
        return map(lambda x: x.replace('.npy', '.jpg'), feat_paths[np.argsort(dis)[:50]])


engine = ImgSearchEngine()
if __name__ == '__main__':
    engine = ImgSearchEngine()
    engine.store_imgs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image.orig'))
    img_paths = engine.query_img(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image.orig'),
                                              sys.argv[1]))
    for idx, img_path in enumerate(img_paths):
        shutil.copy(img_path, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/rs/{}.jpg').format(idx))
