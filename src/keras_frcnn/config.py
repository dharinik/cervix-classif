import os

import numpy as np
from keras import backend as K
from os.path import isfile, join

from data_provider import MEAN_PIXEL_FILE, FRCNN_MODELS_DIR


class Config:
    def __init__(self, **entries):

        self.model_name = "default"
        # setting for roi augmentation
        self.use_horizontal_flips = True
        self.use_vertical_flips = True
        self.scale_augment = False
        self.scale_percent = 1.15  # max zoom in for 10%
        self.random_rotate = True

        self.validation_percent = 0.15

        # anchor box scales
        self.anchor_box_scales = [25, 50, 75, 100, 150, 200, 299]

        # anchor box ratios
        self.anchor_box_ratios = [[1, 1], [1, 2], [2, 1], [2, 2], [1, 3], [1, 4], [3, 1], [4, 1], [3, 4], [4, 3]]

        # size to resize the smallest side of the image
        # self.im_size = 299
        self.im_size = 299

        # number of ROIs at once
        self.num_rois = 2

        # stride at the RPN (this depends on the network configuration)
        self.rpn_stride = 16

        self.balanced_classes = False

        # scaling the stdev
        self.std_scaling = 4.0

        # overlaps for RPN
        self.rpn_min_overlap = 0.3
        self.rpn_max_overlap = 0.7

        # overlaps for classifier ROIs
        self.classifier_min_overlap = 0.1
        self.classifier_max_overlap = 0.7

        self.img_scaling_factor = 1.0
        if isfile(MEAN_PIXEL_FILE):
            self.mean_pixel = list(np.loadtxt(MEAN_PIXEL_FILE, delimiter=','))

        # location of pretrained weights for the base network
        # weight files can be found at:
        # https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_th_dim_ordering_th_kernels_notop.h5
        # https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
        if K.image_dim_ordering() == 'th':
            self.base_net_weights = join(FRCNN_MODELS_DIR,
                                         'resnet50_weights_th_dim_ordering_th_kernels_notop.h5')
        else:
            self.base_net_weights = join(FRCNN_MODELS_DIR,
                                         'resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5')

        self.__dict__.update(entries)

    def get_model_path(self):
        return join(FRCNN_MODELS_DIR, self.model_name, 'model_frcnn.hdf5')
