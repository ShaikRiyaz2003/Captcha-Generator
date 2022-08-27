font=["D:\\CAPTCHA\Fonts\\Roboto\\Roboto-Black.ttf",
"D:\CAPTCHA\Fonts\Grape_Nuts\GrapeNuts-Regular.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-BoldItalic.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-Italic.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-Light.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-LightItalic.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-Medium.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-MediumItalic.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-Regular.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-Thin.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-ThinItalic.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-Black.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-BlackItalic.ttf",
"D:\CAPTCHA\Fonts\Roboto\Roboto-Bold.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\SourceCodePro-Italic-VariableFont_wght.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\SourceCodePro-VariableFont_wght.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-ExtraLight.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-ExtraLightItalic.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-Italic.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-Light.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-LightItalic.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-Medium.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-MediumItalic.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-Regular.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-SemiBold.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-SemiBoldItalic.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-Black.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-BlackItalic.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-Bold.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-BoldItalic.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-ExtraBold.ttf",
"D:\CAPTCHA\Fonts\Source_Code_Pro\static\SourceCodePro-ExtraBoldItalic.ttf",
"D:\CAPTCHA\Fonts\Shadows_Into_Light\ShadowsIntoLight-Regular.ttf",
"D:\CAPTCHA\Fonts\Rubik_Moonrocks\RubikMoonrocks-Regular.ttf",
"D:\CAPTCHA\Fonts\Rubik_Microbe\RubikMicrobe-Regular.ttf",
"D:\CAPTCHA\Fonts\Rubik_Bubbles\RubikBubbles-Regular.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-BoldItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-ExtraBold.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-ExtraBoldItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-ExtraLight.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-ExtraLightItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-Italic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-Light.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-LightItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-Medium.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-MediumItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-Regular.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-SemiBold.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-SemiBoldItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-Thin.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-ThinItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-Black.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-BlackItalic.ttf",
"D:\CAPTCHA\Fonts\Poppins\Poppins-Bold.ttf",
"D:\CAPTCHA\Fonts\Lobster\Lobster-Regular.ttf",
"D:\CAPTCHA\Fonts\Indie_Flower\IndieFlower-Regular.ttf",
"D:\CAPTCHA\Fonts\Dancing_Script\DancingScript-VariableFont_wght.ttf",
"D:\CAPTCHA\Fonts\Dancing_Script\static\DancingScript-Bold.ttf",
"D:\CAPTCHA\Fonts\Dancing_Script\static\DancingScript-Medium.ttf",
"D:\CAPTCHA\Fonts\Dancing_Script\static\DancingScript-Regular.ttf",
"D:\CAPTCHA\Fonts\Dancing_Script\static\DancingScript-SemiBold.ttf",
"D:\CAPTCHA\Fonts\Bebas_Neue\BebasNeue-Regular.ttf",
"D:\CAPTCHA\Fonts\Beau_Rivage\BeauRivage-Regular.ttf",
"D:\CAPTCHA\Fonts\Babylonica\Babylonica-Regular.ttf",
]

from captcha.image import ImageCaptcha
import string
import random as rand
from PIL import Image
def generateCaptcha(string):
    string=string.replace("**", "^")
    image= ImageCaptcha(width=500,height=90,fonts=font)
    data=image.generate(string)
    image.write(string,'captcha.png')
    #image.show()
    img=Image.open('captcha.png')
    img.show()
    text.replace(" ","")
    print(text)
    return text
def equation(size):
    string="".join(rand.choices("0123456789"))
    for i in range(size//2):
        string=string+''.join(rand.choices(["+","-","/","%","**","*"]))
        if("/" in string or "%" in string):
            string=string+"".join(rand.choice("123456789"))
        else:
            string=string+"".join(rand.choices("0123456789"))
    a=str(eval(string))
    if(a.find('.') < len(a)-2 and ("/" in string or "%" in string )):
        a=a[:a.find('.')+3]
    string=string+"="+a
    string=string.replace("**", "^")
    return string
size=rand.randint(0,2)
img=Image.open('captcha.png')
i=0
#size=int(input("Enter no of digits of captcha"))
while(True):
    text=""
    i=i+1
    if(i%2==0):
        size+=1
        text=equation(size)
    else:
        text=text.join(rand.choices(string.ascii_letters+string.digits,k=size))
    
    if(generateCaptcha(text)==input("Enter the string you see:").replace(" ","")):
        img.close()
        break
    img.close()