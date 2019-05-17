import argparse
import datetime
from PIL import Image
import numpy as np
from pathlib import Path

parser = argparse.ArgumentParser(description='Resize imgs')
parser.add_argument('--folder', dest='folder', default='imgs2', help='Folder to be processed')
parser.add_argument('--target', dest='target', default='trainA', help='Folder to put the results in')
parser.add_argument('--size', dest='size', type=int, default=256, help='Size')
args = parser.parse_args()

print('\r')

target = Path(args.target)
target.mkdir(parents=True,exist_ok=True)

origin_path = Path(args.folder)
if not origin_path.exists():
    print('Invalid folder specified')
all_image_paths = list(origin_path.glob('*'))

start_time = datetime.datetime.now()
avg_time = 0
n = len(all_image_paths)
i = 0
for path in all_image_paths:
    epoch_time = datetime.datetime.now()

    img = Image.open(path)
    img = img.resize((args.size, args.size))
    img.save(target.joinpath(path.name))


    epoch_time = datetime.datetime.now() - epoch_time
    avg_time = (avg_time * n + epoch_time.total_seconds()) / (n + 1)
    i += 1
    if i % 10 == 0:
        eta = datetime.datetime.fromtimestamp(start_time.timestamp() + (avg_time * n))
        _avg_time = datetime.datetime.fromtimestamp(avg_time)
        print('Avg time/img: %s, ETA: %s' % (_avg_time , eta), end='\r', flush=True)

print()