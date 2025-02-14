import argparse
from model import Encoder
import os
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')
parser = argparse.ArgumentParser()

parser.add_argument('--model', nargs='?', default='./out/main.tar', help='Path for model checkpoint file [default: ./out/main.tar]')
parser.add_argument('--image', nargs='?', default='./dataset/', help='Directory which holds the images to be compressed [default: ./dataset/]')
parser.add_argument('--out', nargs='?', default='./out/compressed/', help='Directory which will hold the compressed images [default: ./out/compressed/]')
args = parser.parse_args()

f = os.listdir(args.image)
inputs = []
for i in f:
    #if '.png' in i:
    if '.bmp' in i:
        inputs.append(i)

encoder = Encoder(args.model)

for i in inputs:
    print('converting %s...'%i)
    encoder.encode_and_save(os.path.join(args.image, i), os.path.join(args.out, '%scomp.xfr'%i[:-4]))
