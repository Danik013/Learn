from PIL import Image

monro = Image.open("monro.jpg")
red_monro, blue_monro, green_monro = monro.split()

red_coord_left = (50, 0, red_monro.width, red_monro.height)
red_cropped_left = red_monro.crop(red_coord_left)
red_coord_mid = (25, 0, 671, red_monro.height)
red_cropped_mid = red_monro.crop(red_coord_mid)
red_monro_blend = Image.blend(red_cropped_mid, red_cropped_left, 0.2)

blue_coord_right = (0, 0, 646, blue_monro.height)
blue_cropped_right = blue_monro.crop(blue_coord_right)
blue_coord_mid = (25, 0, 671, blue_monro.height)
blue_cropped_mid = blue_monro.crop(blue_coord_mid)
blue_monro_blend = Image.blend(blue_cropped_mid, blue_cropped_right, 0.2)

green_coord_mid = (25, 0, 671, green_monro.height)
green_cropped_mid = green_monro.crop(green_coord_mid)

new_monro = Image.merge("RGB", (red_monro_blend, blue_monro_blend, green_cropped_mid))
new_monro.save("new_monro.jpg")
avatar = Image.merge("RGB", (red_monro_blend, blue_monro_blend, green_cropped_mid))
avatar.thumbnail((80, 80))
avatar.save("avatar.jpg")