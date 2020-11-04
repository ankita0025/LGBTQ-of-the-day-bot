'''
generate_stripey_backgrounds.py: create 16:9 background for posting to twitter
3 November 2020
Vicki Langer (@vicki_langer)
'''

from PIL import Image, ImageDraw, ImageFont


def create_background(stripe_colors):
    # create 16:9 image for twitter post
    box = Image.new("RGB", size=(1600, 900), color="#ffffff")  # test color
    draw = ImageDraw.Draw(box)

    # define stripes
    stripe_height = 90
    # left_img_middle = 700  # px from top
    # right_img_middle = 200  # px from top

    total_stripe_height = stripe_height * len(stripe_colors)
    left_hand_top = 200 - (total_stripe_height / 2)
    right_hand_top = 700 - (total_stripe_height / 2)

    # draw the stripes
    for label, color in enumerate(stripe_colors):
        draw.polygon(
            [
                (0,    left_hand_top  + stripe_height * label),
                (1600, right_hand_top + stripe_height * label),
                (1600, right_hand_top + stripe_height * (label + 1)),
                (0,    left_hand_top  + stripe_height * (label + 1)),
            ],
            fill=color
        )

    # write in the twitter handle watermark thingy
    chosen_font = ImageFont.truetype('assets/Nunito-SemiBold.ttf', 60)
    twitter_handle = "@LGBTQotd"

    draw = ImageDraw.Draw(box)
    draw.text((28, 800), text=twitter_handle, fill=("#444"), font=chosen_font)

    # give the box
    return box

    # add transparent mask thingy to lighten image to help with a11y
    # transparent_front_layer =
    # TODO: add mask

# TODO: add function call to get_img_for_tweet.py
# TODO: add function to get_img_for_tweet.py to check contrast w/ WCAG standards


if __name__ == '__main__':
    for label, stripe_colors in [
        # colors from schemecolor.com/tag/gender-flags
        ("genderfluid", ["#F996B9", "#FFFFFF", "#CA28E3", "#333333", "#5861CD"]),
        ("aromantic", ["#5BBD60", "#BAD897", "#ffffff", "#BABABA", "#333333"]),
        ("asexual", ["#000000", "#a4a4a4", "#ffffff", "#810081"]),
        ("pansexual", ["#ff1b8d", "#ffda00", "#1bb3ff"]),
        ("trans", ["#55cdfc", "#f7a8b8", "#ffffff", "#f7a8b8", "#55cdfc"]),
        ("intersex", ["#ffda00", "#7a00ac"]),
        ("non-binary", ["#fff430", "#ffffff", "#9c59d1", "#000000"]),
        ("bear", ["#633800", "#d76300", "#ffde58", "#ffe7b5", "#555555", "#000000"]),
        ("genderqueer", ["#b77fdd", "#ffffff", "#48821e"]),
        ("polysexual", ["#f714ba", "#01d66a", "#1594f6"]),
    ]:
        box = create_background(stripe_colors=stripe_colors)
        box.save(f"img_bg/bg_{label}.jpg")