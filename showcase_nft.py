import random, time
import cv2
from imageio import imread, mimread
from urllib.request import Request, urlopen

import general_methods as gms

def showcase(wallet):
    rando_art = []
    for i in range(5):
        rando = random_art(wallet)
        if rando.Name != 'Cube Life':
            rando_art.append(rando)
        else:
            rando = random_art(wallet)
            if rando.Name != 'Cube Life':
                rando_art.append(rando)

            else:
                rando = random_art(wallet)
                if rando.Name != 'Cube Life':
                    rando_art.append(rando)


    for rando in rando_art:
        print('Downloading %s' % (rando.Name))
        show_art(rando)

    cv2.waitKey(1)
    for i in range (1,5):
        cv2.destroyAllWindows()
        cv2.waitKey(1)

def random_art(wallet):
    rando = random.choice(wallet)
    return rando

def show_random_art(wallet):
    rando = random.choice(wallet)
    rando.show_art()
    return ''

def print_wallet(wallet):
    if(art_wallet != None):
        print('\nThis collection has {} pieces of Artwork\n\n'.format(len(art_wallet)))
        for piece in art_wallet:
            piece.to_string()

    else:
        print('This address has no Art')

def show_art(art):
    try:
        image = gms.url_to_image(art.ImageURL)
        print('Original Dimensions : ',image.shape)

        h = image.shape[0]
        w = image.shape[1]

        if(h >= 4500 or w >= 4500):
            height = int(0.2 * h)
            width = int(0.2 * w)

            if(height >= 1300 or width >= 1300):
                height = int(height * 0.5)
                width  = int(width * 0.5)

            dim = (height,width)

            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        elif(h >= 4001 or w >= 4001):
            height = int(0.25 * h)
            width = int(0.25 * w)

            dim = (height,width)
            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        elif(h >= 3500 or w >= 3500):
            height = int(0.3 * h)
            width = int(0.3 * w)

            dim = (height,width)
            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)


        elif(h >= 3001 or w >= 3001):
            height = int(0.35 * h)
            width = int(0.35 * w)

            dim = (height,width)
            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        elif(h >= 2500 or w >= 2500):
            height = int(0.4 * h)
            width = int(0.4 * w)

            dim = (width,height)
            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        elif(h >= 1900 or w >= 1900):
            height = int(0.5 * h)
            width = int(0.5 * w)

            dim = (width,height)
            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        elif(h >= 1500 or w >= 1500):
            height = int(0.6 * h)
            width = int(0.6 * w)

            dim = (width,height)
            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        elif(h >= 900 or w >= 900):
            height = int(0.8 * h)
            width = int(0.8 * w)

            dim = (width,height)
            resized = cv2.resize(image, dim,
                                 interpolation = cv2.INTER_AREA)

            print('Resized Dimensions : ',resized.shape)

            cv2.imshow(art.Name, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        else:
            cv2.imshow(art.Name, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        '''
        cv2.imshow(art.Name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        '''

    except:
        fname = 'tmp.gif'
        resp = urlopen(Request(art.ImageURL,
                               headers={'User-Agent': \
                                        'Mozilla/5.0'})).read()
        open(fname,"wb+").write(resp)

        gif = mimread(fname, memtest = False)
        nums = len(gif)
        print("Total {} frames in the gif!".format(nums))

        max_height = 0
        max_width = 0

        for frame in gif:
            h = frame.shape[0]
            w = frame.shape[1]

            if h > max_height:
                max_height = h
            if w > max_width:
                max_width = w

        if(max_height >= 900 or max_width >= 1500):
            if(max_height >= 900):
                scale = 800 / max_height
                dim = (int(scale * max_height), max_width)
            elif(max_width >= 1500):
                scale = 1500 / max_width
                dim = (max_height, int(scale * max_width))

        else:
            dim = (900,900)

        imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]
        resized = [cv2.resize(img, dim,
        interpolation = cv2.INTER_AREA) for img in imgs]

        i = 0
        if(art.Name == 'WASHINGTON VIDEO GAME'):
            while True:
                cv2.imshow('{} gif'.format(art.Name), imgs[i])
                if cv2.waitKey(100)&0xFF == 27:
                    break
                time.sleep(0.1)
                i = (i+1)%nums

        else:
            while True:
                cv2.imshow('{} gif'.format(art.Name), imgs[i])
                if cv2.waitKey(100)&0xFF == 27:
                    break
                i = (i+1)%nums

            cv2.destroyAllWindows()
            cv2.waitKey(1)

    finally:
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    return ''
