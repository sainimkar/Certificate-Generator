import os
import sys

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from func.shorten import shorten 


# Add name, institute and title to certificate
def maker( ID, name, completed_on, score ):
    abspath = os.path.abspath("")
    templates_dir = os.path.join(abspath, "templates")
    img = Image.open(f'{templates_dir}/certi_final.png')
    draw = ImageDraw.Draw(img)

    # Load font
    fonts_dir = os.path.join(abspath, "fonts")
    font = ImageFont.truetype(f"{fonts_dir}/RobotoCondensed-Regular.ttf", 25)
    font2 = ImageFont.truetype(f"{fonts_dir}/RobotoCondensed-Regular.ttf", 25)
    font1 = ImageFont.truetype(f"{fonts_dir}/RobotoCondensed-Regular.ttf", 50)

    # Check sizes and if it is possible to abbreviate
    if ( len( name ) > 20 ):
        name = shorten( name, 20 )

    if name == -1 or completed_on == -1 or score == -1 :
        return -1
    else:
        # Insert text into image template
        print(score)
        draw.text( (460, 380), name, (64,64,64), font=font1 )
        draw.text( (320, 530), str(completed_on), (64,64,64), font=font2 )
        draw.text( (850, 530), str(int(score)) + '%', (64,64,64), font=font )

        main_dir = os.path.join(abspath, "certificates")
        if not os.path.isdir(main_dir) :
            os.makedirs(main_dir)

        # Save as a PDF
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        img.save( f'{main_dir}/certificate\\'+str(ID)+'.pdf', "PDF", resolution=100.0)
        return  f'{main_dir}/certificate\\' + str(ID)+ '.pdf' , 'certificate\\' + str(ID) + '.pdf'