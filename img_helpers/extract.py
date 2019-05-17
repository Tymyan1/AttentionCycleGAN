import argparse
from PIL import Image
from pathlib import Path

parser = argparse.ArgumentParser(description='Extract some petri dishes.')
parser.add_argument('--folder', dest='folder', default='imgs1', help='Folder to be processed')
parser.add_argument('--target', dest='target', default='result_imgs', help='Folder to put the results in')
parser.add_argument('--size', dest='size', type=int, default=256, help='Size of the final img (squares only)')
args = parser.parse_args()

target = Path(args.target)
target.mkdir(parents=True,exist_ok=True)

# coordinates
n_dishes = 10
square = 256
xs = [368,625,870,1127,1385,380,623,860,1117,1388]
ys = [350,333,327,303,320,609,620,655,627,619]

origin_path = Path(args.folder)
all_image_paths = list(origin_path.glob('*'))

for path in all_image_paths:
# path = next(iter(all_image_paths))
    img = Image.open(path)
    for d in range(n_dishes):
        dish_img = img.crop((xs[d], ys[d], xs[d]+square, ys[d]+square))
        dish_img = dish_img.resize((args.size, args.size))
        index = path.name.find('.')
        dish_img.save(target.joinpath((path.name[:index] + '_' + str(d) + '.png')), format='PNG')