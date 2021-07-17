nsfw_file = open("nsfw.txt", "r")
nsfw_words = nsfw_file.readlines()
nsfw_words = [x.strip('\n') for x in nsfw_words]

from PIL import Image, ImageFont, ImageDraw
import requests
from cryptography.fernet import Fernet

decryptKey = os.environ['enc-key']
decryptKey = str.encode(decryptKey[2:-1])
fernet = Fernet(decryptKey)
class warden:

    def __init__(self):
        pass

    def encrypt(self, message):
        return fernet.encrypt(message.encode())

    def decrypt(self, message):
        return fernet.decrypt(message).decode()

    def strToByte(self, message):
        message = message[2:-1]
        return str.encode(message)
    
    def nsfwCheck(self, message):
        for words in nsfw_words:
            new = self.strToByte(words)
            if  self.decrypt(new) in message:
                return True
                                        
    def censorMessage(self, message):
        for words in nsfw_words:
            new = self.strToByte(words)
            ndec = self.decrypt(new)
            if ndec in message:
                message = message.replace(ndec, '\*'*(len(ndec)-1)+'\*')
        return message




class customizer:

    def __init__(self):
        pass

    def welcomeCard(self, pngImage, font, fontSize, pfpURL, memberCount, memberUsername):

        img = Image.open(pngImage)
        
        W, H = (img.width, img.height)
        
        pfp = Image.open(requests.get(pfpURL, stream=True).raw)
        basewidth = 190
        wpercent = (basewidth/float(pfp.size[0]))
        hsize = int((float(pfp.size[1])*float(wpercent)))
        pfp = pfp.resize((basewidth,hsize), Image.ANTIALIAS)
        w1, h1 = pfp.size
        img.paste(pfp, (int((W-w1)/2), int((H-h1)/2 - 90)))
        
        font = ImageFont.truetype(font, fontSize)
        text = "Welcome!, @"+memberUsername
        draw = ImageDraw.Draw(img)
        w, h = draw.textsize(text, font=font)
        draw.text(((W-w)/2, 80+(H-h)/2), text, (255, 255, 255), font=font)
        
        font = ImageFont.truetype("Aileron-ThinItalic.otf", 50)
        text = "Member #"+str(memberCount)
        w, h = draw.textsize(text, font=font)
        draw.text(((W-w)/2, 170+(H-h)/2), text, (255, 255, 255), font=font)
        
        img.save("text.png")
