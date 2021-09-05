import os
import hashlib
import py_avataaars as pa
import secrets

import pixelizer

style_list = [pa.AvatarStyle.CIRCLE]
skin_color_list = [pa.SkinColor.LIGHT,
                   pa.SkinColor.BLACK,
                   pa.SkinColor.BROWN,
                   pa.SkinColor.DARK_BROWN,
                   pa.SkinColor.PALE,
                   pa.SkinColor.TANNED,
                   pa.SkinColor.YELLOW]
hair_color_list = [pa.HairColor.BROWN,
                   pa.HairColor.BLACK,
                   pa.HairColor.BROWN_DARK,
                   pa.HairColor.AUBURN,
                   pa.HairColor.BLONDE,
                   pa.HairColor.BLONDE_GOLDEN,
                   pa.HairColor.PASTEL_PINK,
                   pa.HairColor.PLATINUM,
                   pa.HairColor.RED,
                   pa.HairColor.SILVER_GRAY]
facial_hair_type_list = [pa.FacialHairType.DEFAULT,
                         pa.FacialHairType.BEARD_LIGHT,
                         pa.FacialHairType.BEARD_MAJESTIC,
                         pa.FacialHairType.BEARD_MEDIUM,
                         pa.FacialHairType.MOUSTACHE_FANCY,
                         pa.FacialHairType.MOUSTACHE_MAGNUM]
facial_hair_color_list = [pa.HairColor.BLACK,
                          pa.HairColor.BROWN,
                          pa.HairColor.RED,
                          pa.HairColor.BLONDE,
                          pa.HairColor.AUBURN,
                          pa.HairColor.SILVER_GRAY,
                          pa.HairColor.PLATINUM,
                          pa.HairColor.PASTEL_PINK,
                          pa.HairColor.BLONDE_GOLDEN,
                          pa.HairColor.BROWN_DARK]
top_type_list = [pa.TopType.SHORT_HAIR_SHORT_FLAT,
                 pa.TopType.HAT,
                 pa.TopType.HIJAB,
                 pa.TopType.EYE_PATCH,
                 pa.TopType.LONG_HAIR_BIG_HAIR,
                 pa.TopType.LONG_HAIR_BOB,
                 pa.TopType.LONG_HAIR_BUN,
                 pa.TopType.LONG_HAIR_CURLY,
                 pa.TopType.LONG_HAIR_CURVY,
                 pa.TopType.LONG_HAIR_DREADS,
                 pa.TopType.LONG_HAIR_FRO,
                 pa.TopType.LONG_HAIR_FRIDA,
                 pa.TopType.LONG_HAIR_FRO_BAND,
                 pa.TopType.LONG_HAIR_MIA_WALLACE,
                 pa.TopType.LONG_HAIR_NOT_TOO_LONG,
                 pa.TopType.LONG_HAIR_SHAVED_SIDES,
                 pa.TopType.LONG_HAIR_STRAIGHT,
                 pa.TopType.LONG_HAIR_STRAIGHT2,
                 pa.TopType.LONG_HAIR_STRAIGHT_STRAND,
                 pa.TopType.NO_HAIR,
                 pa.TopType.SHORT_HAIR_DREADS_01,
                 pa.TopType.SHORT_HAIR_DREADS_02,
                 pa.TopType.SHORT_HAIR_FRIZZLE,
                 pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
                 pa.TopType.SHORT_HAIR_SHORT_CURLY,
                 pa.TopType.SHORT_HAIR_SHORT_ROUND,
                 pa.TopType.SHORT_HAIR_SHORT_WAVED,
                 pa.TopType.SHORT_HAIR_SIDES,
                 pa.TopType.SHORT_HAIR_THE_CAESAR,
                 pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART,
                 pa.TopType.TURBAN,
                 pa.TopType.WINTER_HAT1,
                 pa.TopType.WINTER_HAT2,
                 pa.TopType.WINTER_HAT3,
                 pa.TopType.WINTER_HAT4]
hat_color_list = [pa.Color.BLACK,
                  pa.Color.BLUE_01,
                  pa.Color.BLUE_02,
                  pa.Color.BLUE_03,
                  pa.Color.GRAY_01,
                  pa.Color.GRAY_02,
                  pa.Color.HEATHER,
                  pa.Color.PASTEL_BLUE,
                  pa.Color.PASTEL_GREEN,
                  pa.Color.PASTEL_ORANGE,
                  pa.Color.PASTEL_RED,
                  pa.Color.PASTEL_YELLOW,
                  pa.Color.PINK,
                  pa.Color.RED,
                  pa.Color.WHITE]
mouth_type_list = [pa.MouthType.DEFAULT,
                   pa.MouthType.CONCERNED,
                   pa.MouthType.DISBELIEF,
                   pa.MouthType.EATING,
                   pa.MouthType.GRIMACE,
                   pa.MouthType.SAD,
                   pa.MouthType.SCREAM_OPEN,
                   pa.MouthType.SERIOUS,
                   pa.MouthType.SMILE,
                   pa.MouthType.TONGUE,
                   pa.MouthType.TWINKLE,
                   pa.MouthType.VOMIT]
eye_type_list = [pa.EyesType.DEFAULT,
                 pa.EyesType.CLOSE,
                 pa.EyesType.CRY,
                 pa.EyesType.DIZZY,
                 pa.EyesType.EYE_ROLL,
                 pa.EyesType.HAPPY,
                 pa.EyesType.HEARTS,
                 pa.EyesType.SIDE,
                 pa.EyesType.SQUINT,
                 pa.EyesType.SURPRISED,
                 pa.EyesType.WINK,
                 pa.EyesType.WINK_WACKY]
eyebrow_type_list = [pa.EyebrowType.DEFAULT,
                     pa.EyebrowType.DEFAULT_NATURAL,
                     pa.EyebrowType.ANGRY,
                     pa.EyebrowType.ANGRY_NATURAL,
                     pa.EyebrowType.FLAT_NATURAL,
                     pa.EyebrowType.RAISED_EXCITED,
                     pa.EyebrowType.RAISED_EXCITED_NATURAL,
                     pa.EyebrowType.SAD_CONCERNED,
                     pa.EyebrowType.SAD_CONCERNED_NATURAL,
                     pa.EyebrowType.UNI_BROW_NATURAL,
                     pa.EyebrowType.UP_DOWN,
                     pa.EyebrowType.UP_DOWN_NATURAL,
                     pa.EyebrowType.FROWN_NATURAL]
nose_type_list = [pa.NoseType.DEFAULT]
accessories_type_list = [pa.AccessoriesType.DEFAULT,
                         pa.AccessoriesType.KURT,
                         pa.AccessoriesType.PRESCRIPTION_01,
                         pa.AccessoriesType.PRESCRIPTION_02,
                         pa.AccessoriesType.ROUND,
                         pa.AccessoriesType.SUNGLASSES,
                         pa.AccessoriesType.WAYFARERS]
cloth_type_list = [pa.ClotheType.BLAZER_SHIRT,
                   pa.ClotheType.BLAZER_SWEATER,
                   pa.ClotheType.COLLAR_SWEATER,
                   pa.ClotheType.GRAPHIC_SHIRT,
                   pa.ClotheType.HOODIE,
                   pa.ClotheType.OVERALL,
                   pa.ClotheType.SHIRT_CREW_NECK,
                   pa.ClotheType.SHIRT_SCOOP_NECK,
                   pa.ClotheType.SHIRT_V_NECK]
cloth_color_list = [pa.Color.BLACK,
                    pa.Color.BLUE_01,
                    pa.Color.BLUE_02,
                    pa.Color.BLUE_03,
                    pa.Color.GRAY_01,
                    pa.Color.GRAY_02,
                    pa.Color.HEATHER,
                    pa.Color.PASTEL_BLUE,
                    pa.Color.PASTEL_GREEN,
                    pa.Color.PASTEL_ORANGE,
                    pa.Color.PASTEL_RED,
                    pa.Color.PASTEL_YELLOW,
                    pa.Color.PINK,
                    pa.Color.WHITE]
cloth_graphic_type_list = [pa.ClotheGraphicType.BAT,
                           pa.ClotheGraphicType.CUMBIA,
                           pa.ClotheGraphicType.DEER,
                           pa.ClotheGraphicType.DIAMOND,
                           pa.ClotheGraphicType.HOLA,
                           pa.ClotheGraphicType.PIZZA,
                           pa.ClotheGraphicType.RESIST,
                           pa.ClotheGraphicType.SELENA,
                           pa.ClotheGraphicType.BEAR,
                           pa.ClotheGraphicType.SKULL_OUTLINE,
                           pa.ClotheGraphicType.SKULL]


def get_object_info(a: pa.PyAvataaar):
    info = '''{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}''' \
        .format(a.style,
                a.background_color,
                a.skin_color,
                a.hair_color,
                a.facial_hair_type,
                a.facial_hair_color,
                a.top_type,
                a.hat_color,
                a.mouth_type,
                a.eye_type,
                a.nose_type,
                a.eyebrow_type,
                a.accessories_type,
                a.clothe_type,
                a.clothe_color,
                a.clothe_graphic_type)
    return info


def generate_object_md5(info):
    result = hashlib.md5(info.encode()).hexdigest()
    return result


def generate_avatar_png_x(random):
    proc = 0
    unproc = 0
    output = './png'
    if os.path.exists(output):
        print('''Folder './png' exists''')
    else:
        print('''Creating folder './png' ''')
        os.mkdir('./png')

    for i in range(random):
        avatar = pa.PyAvataaar(
            style=secrets.choice(style_list),
            skin_color=secrets.choice(skin_color_list),
            hair_color=secrets.choice(hair_color_list),
            facial_hair_type=secrets.choice(facial_hair_type_list),
            facial_hair_color=secrets.choice(facial_hair_color_list),
            top_type=secrets.choice(top_type_list), hat_color=secrets.choice(hat_color_list),
            mouth_type=secrets.choice(mouth_type_list), eye_type=secrets.choice(eye_type_list),
            eyebrow_type=secrets.choice(eyebrow_type_list), nose_type=secrets.choice(nose_type_list),
            accessories_type=secrets.choice(accessories_type_list),
            clothe_type=secrets.choice(cloth_type_list),
            clothe_color=secrets.choice(cloth_color_list),
            clothe_graphic_type=secrets.choice(cloth_graphic_type_list))
        info = get_object_info(avatar)
        object_txt = open('output.txt', 'a')
        object_txt.write(info)
        object_txt.close()
        print(proc)
        # hash = generate_object_md5(info)
        hash = info
        file_name = './png/{}.png'.format(hash)
        if os.path.isfile(file_name):
            unproc += 1
            print("File already exists, UNPROC: {}".format(
                unproc))
        else:
            proc += 1
            print(
                "File does not exist, creating new avatar, PROC: {}".format(
                    proc))
            avatar.render_png_file(file_name)
            print(
                "File does not exist, creating new pixel avatar")
            # pixelizer.run(file_name, '{}.png'.format(hash))


generate_avatar_png_x(20000)
