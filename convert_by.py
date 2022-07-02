from PIL import Image

num_key_frames = 16

with Image.open('by18.gif') as im:
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save('f'+'{}.png'.format(i))