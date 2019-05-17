import argparse
from PIL import Image
from pathlib import Path

parser = argparse.ArgumentParser(description='Extract samples from sample image')
parser.add_argument('--folder', dest='folder', default='samples', help='Folder to be processed')
parser.add_argument('--target', dest='target', default='sub-samples', help='Folder to put the results in')
args = parser.parse_args()

origin_path = Path(args.folder)
all_image_paths = list(origin_path.glob('*'))

x_offset = 511
imgs = 9
res = (471, 471)
origin1 = (37, 1222)
origin2 = (37, 2915)

target = origin1

for path in all_image_paths:
    img = Image.open(path).convert('RGB').crop((548, 1222, 1019, 1688)).save(args.target + '/' + path.name)