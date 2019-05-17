import argparse
from PIL import Image
from pathlib import Path

parser = argparse.ArgumentParser(description='Remove the alpha channel from images in folder.')
parser.add_argument('--folder', dest='folder', default='sim2larvae/testB', help='Folder to be processed')
args = parser.parse_args()

origin_path = Path(args.folder)
all_image_paths = list(origin_path.glob('*'))

for path in all_image_paths:
# path = next(iter(all_image_paths))
    img = Image.open(path).convert('RGB').save('sim2larvae/testB/' + path.name)