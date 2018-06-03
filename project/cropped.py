import cv2
import pathlib
from itertools import count


path = pathlib.Path('../db_images')
path = path.resolve()
print(path)

path_imgs_handwritten = path.joinpath('handwritten_digits')
print(path_imgs_handwritten)

is_dir = path_imgs_handwritten.is_dir()
exists_path = path_imgs_handwritten.exists()

print(is_dir)
print(exists_path)

path_imgs = (img for img in path_imgs_handwritten.rglob("*") if img.is_file())

counter = count(1)

for path_img in path_imgs:
    print(path_img.as_posix())

    image = cv2.imread(path_img.as_posix())

    if any(flag in path_img.as_posix() for flag in ['.jpg', '.jpeg']):

        cv2.imshow('original', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#        cropped_up = image[:image.shape[0] // 2, ::]
#        cropped_down = image[image.shape[0] // 2:, ::]

#        cv2.imshow('cropped_up', cropped_up)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()

#        cv2.imshow('cropped_down', cropped_down)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()

        while True: 
            n = next(counter)
            print(n, end="\t")
            print(path_img.with_name(f'sample-{n}.png').exists())
            if not path_img.with_name(f'sample-{n}.png').exists():
                cv2.imwrite(
                    path_img.with_name(f'sample-{n}.png').as_posix(),
                    image
                )
                break


