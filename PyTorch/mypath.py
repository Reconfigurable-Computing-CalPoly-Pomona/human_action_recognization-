class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            #root_dir = 'E:\CPP\AI Tutorial\Pytorch\pytorch-video-recognition\UCF-101'
            root_dir = 'UCF-101'

            # Save preprocess data into output_dir
            #output_dir = 'E:\CPP\AI Tutorial\Pytorch\pytorch-video-recognition\UCF101'
            output_dir = 'UCF_101'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/Path/to/hmdb-51'

            output_dir = '/path/to/VAR/hmdb51'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return 'c3d-pretrained.pth'