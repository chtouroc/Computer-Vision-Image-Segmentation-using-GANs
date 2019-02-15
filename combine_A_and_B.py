import os
import numpy as np
import cv2
import argparse
from PIL import Image
from random import shuffle
'''in this file, we changed the way the original file works'''
parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--fold_A', dest='fold_A', help='input directory for image A', type=str, default='../dataset/50kshoes_edges')
parser.add_argument('--fold_B', dest='fold_B', help='input directory for image B', type=str, default='../dataset/50kshoes_jpg')
parser.add_argument('--fold_AB', dest='fold_AB', help='output directory', type=str, default='../dataset/test_AB')
parser.add_argument('--num_imgs', dest='num_imgs', help='number of images',type=int, default=1000000)
parser.add_argument('--use_AB', dest='use_AB', help='if true: (0001_A, 0001_B) to (0001_AB)',action='store_true')
args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg,  getattr(args, arg))
#small fix for python 3
cv2.CV_LOAD_IMAGE_COLOR = 1
splits = os.listdir(args.fold_A)
print(splits)
for sp in splits:
    if sp!='.DS_Store': 
        '''we used this because this kind of file gets created in mac'''
        img_fold_A = os.path.join(args.fold_A, sp)
        print(img_fold_A,"wazgha")
        img_fold_B = os.path.join(args.fold_B, sp)
        img_list =os.listdir(img_fold_A)
        shuffle(img_list)
        print(img_list)
        if args.use_AB:
            img_list=[img_path for img_path in img_list if '_A.' in img_path]
            '''We shuffle the list to make sure we have a random validation set and train set everytime'''
            shuffle(img_list) 
        num_imgs = min(args.num_imgs, len(img_list))
        '''Training set has proportion 70%'''
        tr=int(num_imgs*0.7)
        '''Validation set has proportion 30%'''
        te=num_imgs-tr
        print(' train split of %s, use %d/%d images' % (sp, tr, len(img_list)))
        for n in range(tr):
            img_fold_AB = os.path.join(args.fold_AB, sp)
            img_fold_AB=os.path.join(img_fold_AB, 'train')
            if not os.path.isdir(img_fold_AB):
                os.makedirs(img_fold_AB)
            #print(' train split = %s, number of images = %d' % (sp, tr))
            name_A = img_list[n]
            path_A = os.path.join(img_fold_A, name_A)
            if args.use_AB:
                name_B = name_A.replace('_A.', '_B.')
            else:
                name_B = name_A
            path_B = os.path.join(img_fold_B, name_B)
            if os.path.isfile(path_A) and os.path.isfile(path_B):
                name_AB = name_A
                if args.use_AB:
                    name_AB = name_AB.replace('_A.', '.') # remove _A
                path_AB = os.path.join(img_fold_AB, name_AB)
                im_A = cv2.imread(path_A, cv2.CV_LOAD_IMAGE_COLOR)
                im_B = cv2.imread(path_B, cv2.CV_LOAD_IMAGE_COLOR)
                im_AB = np.concatenate([im_A, im_B], 1)
                '''convert images to jpg'''
                cv2.imwrite(path_AB[:-3]+"jpg", im_AB)
        
        print(' test split of %s, use %d/%d images' % (sp, te, len(img_list)))
        for n in range(tr,num_imgs):
            img_fold_AB = os.path.join(args.fold_AB, sp)
            img_fold_AB=os.path.join(img_fold_AB, 'test')
            if not os.path.isdir(img_fold_AB):
                os.makedirs(img_fold_AB)
            #print(' test split = %s, number of images = %d' % (sp, te))
            name_A = img_list[n]
            path_A = os.path.join(img_fold_A, name_A)
            if args.use_AB:
                name_B = name_A.replace('_A.', '_B.')
            else:
                name_B = name_A
            path_B = os.path.join(img_fold_B, name_B)
            if os.path.isfile(path_A) and os.path.isfile(path_B):
                name_AB = name_A
                if args.use_AB:
                    name_AB = name_AB.replace('_A.', '.') # remove _A
                path_AB = os.path.join(img_fold_AB, name_AB)
                im_A = cv2.imread(path_A, cv2.CV_LOAD_IMAGE_COLOR)
                im_B = cv2.imread(path_B, cv2.CV_LOAD_IMAGE_COLOR)
                im_AB = np.concatenate([im_A, im_B], 1)
                cv2.imwrite(path_AB[:-3]+"jpg", im_AB)
                #im_AB = Image.open(path_AB[:-3]+"jpg")
                #im_AB = im_AB.convert("RGB").resize((512, 256), Image.ANTIALIAS) 
                #path_AB=path_AB[:-3]+"jpg"
                #im_AB.save(path_AB)