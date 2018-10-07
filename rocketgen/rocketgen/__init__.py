import random
import svgwrite

from .core import (
    shape_funcs,
)

def render_stack(svg, x, y, stack_obj, poly_kwargs):
    for segment in stack_obj:
        if "style" in segment:
            segment_poly_kwargs = get_poly_kwargs_from_style_obj(segment["style"])
            for k,v in poly_kwargs.items():
                if not k in segment_poly_kwargs:
                    segment_poly_kwargs[k] = v
        
        else:
            segment_poly_kwargs = poly_kwargs


        svg.add(
            shape_funcs[segment["shape"]](
                x,y,
                poly_kwargs=segment_poly_kwargs,
                **segment["kwargs"]
            )
        )
        y += segment["kwargs"]["h"]

    # display(SVG(svg.tostring()))

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

def get_poly_kwargs_from_style_obj(style_obj):
    return_obj = {}

    for k,v in style_obj.items():
        #FIXME: This is a really hacky way to extract and convert rgb objects
        if type(v)==list:
            return_obj[k] = svgwrite.rgb(v[0], v[1], v[2])
        else:
            return_obj[k] = v

    return return_obj


def render_rocket(rocket):
    poly_kwargs = get_poly_kwargs_from_style_obj(rocket["style"])

    svg = svgwrite.Drawing('test.svg')
    x,y = 100, 10
    render_stack(
        svg, x, y,
        rocket["segments"],
        poly_kwargs,
    )
    # file("output/rocket_"+str(i)+".svg", "w").write(svg.tostring())
    return svg
