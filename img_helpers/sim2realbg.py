import argparse
import datetime
from PIL import Image
import numpy as np
from pathlib import Path

parser = argparse.ArgumentParser(description='Transform simulation imgs to have real bg')
parser.add_argument('--folder', dest='folder', default='trainA', help='Folder to be processed')
parser.add_argument('--target', dest='target', default='result_imgs', help='Folder to put the results in')
parser.add_argument('--bg', dest='bg', default='background.png', help='Background img')
args = parser.parse_args()

target = Path(args.target)
target.mkdir(parents=True,exist_ok=True)

bg_path = Path(args.bg)
if not bg_path.exists():
    print('Invalid background img specified')
bg = Image.open(bg_path).convert("RGBA")


origin_path = Path(args.folder)
if not origin_path.exists():
    print('Invalid folder specified')
all_image_paths = list(origin_path.glob('*'))

mask_colours = [[0, 0, 0, 255], [141, 141, 141, 255]]

start_time =  datetime.datetime.now()
avg_time = 0
n = len(all_image_paths)
i = 0
for path in all_image_paths:
    epoch_time =  datetime.datetime.now()
    img = np.array(Image.open(path))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.all(np.isin(img[i,j], mask_colours)):
                img[i,j] = [0,0,0,0]

    fg = Image.fromarray(img, 'RGBA')
    img = Image.alpha_composite(bg, fg)
    index = path.name.find('.')
    img.save(target.joinpath((path.name[:index] + '.png')), format='PNG')

    epoch_time = datetime.datetime.now() - epoch_time
    avg_time = (avg_time * n + epoch_time.total_seconds()) / (n + 1)
    i += 1
    if i % 10 == 0:
        eta = datetime.datetime.fromtimestamp(start_time.timestamp() + (avg_time * n))
        _avg_time = datetime.datetime.fromtimestamp(avg_time)
        print('Avg time/img: %s, ETA: %s' % (_avg_time, eta), flush=True)

print()
