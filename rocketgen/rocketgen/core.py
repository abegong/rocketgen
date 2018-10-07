import svgwrite


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
