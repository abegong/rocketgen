import random
import json

def generate_random_stack_segment(last_w, is_top, is_last):
    if is_top and random.random() > .3:
        segment = {
            "shape" : "isotri",
            "kwargs" : {
                "w" : last_w,
                "h" : 10+random.random()*60,
            }
        }

    else:

        segment_type = random.choice(["rectangle", "rectangle", "trapezoid"])

        if segment_type== "rectangle":
            adjustment = random.choice(["same", "same", "same", "same", "shrink", "grow"])

            if adjustment == "shrink":
                last_w = last_w*random.uniform(.5, .9)
            elif adjustment == "grow":
                last_w = last_w*random.uniform(1.1, 1/.5)

            segment = {
                "shape" : "rectangle",
                "kwargs" : {
                    "w" : last_w,
                    "h" : 10+random.random()*90,
                }
            }

        elif segment_type=="trapezoid":
            spread = random.uniform(.3, 1.7)
            segment = {
                "shape" : "trapezoid",
                "kwargs" : {
                    "w" : last_w,
                    "h" : 10+random.random()*40,
                    "spread" : spread,
                }
            }
            last_w = last_w*spread

        else:
            raise ValueError

    if random.random() > .8:
        segment["style"] = {
            "fill" : random.choice([
                [32, 32, 32],
                [128, 128, 128],
                [255, 255, 255],
            ])
        }

    return segment, last_w

def generate_random_rocket():
    segments = []

    last_w = 10+random.random()*100
    for i in range(random.randint(3,8)):
        segment, last_w = generate_random_stack_segment(
            last_w,
            is_top=i==0,
            is_last=False,
        )
        segments.append(segment)

    return {
        "segments" : segments,
        "attachments" : [],
        "style" : {
            "stroke" : [64, 64, 64],
            "stroke_width" : 4,
            "stroke_linejoin" : 'round',
            "fill" : [
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255),
            ],
        }
    }