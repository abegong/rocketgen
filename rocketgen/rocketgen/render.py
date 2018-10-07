import svgwrite

from .util import (
    get_poly_kwargs_from_style_obj,
)

def gen_isotri(x, y, w, h, poly_kwargs):
    return svgwrite.shapes.Polygon(
        points=[(x+px,y+py) for px,py in (0,0), (w/-2, h), (w/2, h)],
        **poly_kwargs
    )

def gen_trapezoid(x, y, w, h, spread, poly_kwargs):
    return svgwrite.shapes.Polygon(
        points=[(x+px,y+py) for (px,py) in [(w/-2,0), (w*spread/-2, h), (w*spread/2, h), (w/2, 0)]],
        **poly_kwargs
    )

def gen_rectangle(x, y, w, h, poly_kwargs):
    return svgwrite.shapes.Polygon(
        points=[(x+px,y+py) for (px,py) in [(w/-2,0), (w/-2, h), (w/2, h), (w/2, 0)]],
        **poly_kwargs
    )

def gen_circle(x, y, r, poly_kwargs):
    return svgwrite.shapes.Circle(
        center=(x,y),
        r=r,
        **poly_kwargs
    )

shape_funcs = {
    "isotri" : gen_isotri,
    "trapezoid" : gen_trapezoid,
    "rectangle" : gen_rectangle,
#     "circle" : gen_circle,
}


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
