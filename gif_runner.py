from urllib.request import Request, urlopen
import os, time
import pir_communication as comm

def grab_wallet():
    erc721_address = 'Enter Ethereum Address'
    art_wallet = b.buildIt(c.owner_addr)
    return art_wallet

def do():
    wallet = grab_wallet()
    token = [i for i in wallet if i.TokenID == '5864']
    run(token)

def run(art):
    try:
        store_gif(art)
        gif = get_gif()
        comm.setup()
        
        while True:
            show_first_image(art, gif[0])
            check = 0
            while check != 1:
                check = comm.current_state
                time.sleep(0.1)
                comm.check_motion()
                
            if check:
                run_gif(art, gif[0])
                
     except:
        print('Something is broken')
        
     finally:
        cleanup()
        

def store_gif(art):
    fname = 'tmp.gif'
    resp = urlopen(Request(art.ImageURL,headers={'User-Agent': 'Mozilla/5.0'})).read()
    open(fname,"wb+").write(resp)
    
def cleanup():
    exists = os.path.isfile('tmp.gif')
    if exists:
        os.remove('tmp.gif')
        print('Files cleaned up!')

def get_gif():
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
      return [imgs, resized]
      
def show_first_image(art, gif):
    try:
        cv2.imshow('{} gif'.format(art.Name), gif[0])
        if cv2.waitKey(100)&0xFF == 27:
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
    except:
        print('Problem showing Gif')
        
    finally:
        return ''
      
def run_gif(art, gif):
    i = 0
    try:
        while True:
            cv2.imshow('{} gif'.format(art.Name), gif[i])
            if cv2.waitKey(100)&0xFF == 27:
                break
            time.sleep(0.1)
            i = (i+1)%nums

        cv2.destroyAllWindows()
        cv2.waitKey(1)
        
    except:
        print('Problem running Gif!')

    finally:
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        return ''
