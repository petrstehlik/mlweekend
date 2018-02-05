from PIL import Image, ImageOps
import numpy as np

dataset_path='/Users/petrstehlik/Downloads/fgvc-aircraft-2013b/data'

def load_image( infilename ):
    img = Image.open( infilename ).convert('L')
    img.load()
    (width, height) = (img.size)
    img.crop((0, 0, width, height - 20))
    img = ImageOps.fit(img, [150, 100], Image.ANTIALIAS)
    data = np.asarray(img, dtype="uint8")
    return data


def load_dataset(designation, classes):
    class_numbers = []
    print("Loading {}...".format(designation))
    result = []
    file_name = '{}/{}.txt'.format(dataset_path, designation)
    with open(file_name) as f:
        for i, line in enumerate(f):
            file_desig = line.split()[0]
            file_class = line.split(None, maxsplit=1)[1].strip()
            class_numbers.append(classes[file_class])
            img = load_image("{}/images/{}.jpg".format(dataset_path, file_desig))
            result.append(img)
    result = np.array(result)
    class_numbers = np.array(class_numbers)
    print('first result: ',repr(result[0]))
    print('Giving back array of {} images and {} classes'.format(len(result), len(class_numbers)))
    return(result, class_numbers)

def load_classes(designation):
    classes = {}
    with open('{}/{}.txt'.format(dataset_path, designation)) as f:
        for i, line in enumerate(f):
            classes[line.strip()] = i
    return(classes)

def load_data(path='mnist.npz'):
    classes = load_classes('manufacturers')
    (x_train, y_train) = load_dataset('images_manufacturer_train', classes)
    (x_test, y_test) = load_dataset('images_manufacturer_test', classes)

    return (x_train, y_train), (x_test, y_test)
