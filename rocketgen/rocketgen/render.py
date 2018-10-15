import json
import svgwrite

from .util import (
    get_poly_kwargs_from_style_obj,
)

def gen_isotri(x, y, w, h, poly_kwargs):
    return [svgwrite.shapes.Polygon(
        points=[(x+px,y+py) for px,py in (0,0), (w/-2, h), (w/2, h)],
        **poly_kwargs
    )]

def gen_trapezoid(x, y, w, h, spread, poly_kwargs):
    return [svgwrite.shapes.Polygon(
        points=[(x+px,y+py) for (px,py) in [(w/-2,0), (w*spread/-2, h), (w*spread/2, h), (w/2, 0)]],
        **poly_kwargs
    )]

def gen_rectangle(x, y, w, h, poly_kwargs):
    return [svgwrite.shapes.Polygon(
        points=[(x+px,y+py) for (px,py) in [(w/-2,0), (w/-2, h), (w/2, h), (w/2, 0)]],
        **poly_kwargs
    )]

def gen_circle(x, y, x_offset, y_offset, r, poly_kwargs):
    return [svgwrite.shapes.Circle(
        center=(x+x_offset,y+y_offset),
        r=r,
        **poly_kwargs
    )]

def gen_mirrored_poly(x, y, x_offset, y_offset, points, poly_kwargs):
    return [
        svgwrite.shapes.Polygon(
            points=[(x+px+x_offset,y+py+y_offset) for px,py in points],
            **poly_kwargs
        ),
        svgwrite.shapes.Polygon(
            points=[(x-px-x_offset,y+py+y_offset) for px,py in points],
            **poly_kwargs
        ),
    ]

shape_funcs = {
    "isotri" : gen_isotri,
    "trapezoid" : gen_trapezoid,
    "rectangle" : gen_rectangle,
    "circle" : gen_circle,
    "mirrored_poly" : gen_mirrored_poly,
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


        # print(json.dumps(segment, indent=2))

        new_shapes = shape_funcs[segment["shape"]](
            x,y,
            poly_kwargs=segment_poly_kwargs,
            **segment["kwargs"]
        )

        #FIXME: stack attachments usually need to be rendered first,
        #but other attachments should be rendered later, so they can go on top.
        if "attachments" in segment:
            render_attachments(
                svg, x, y,
                segment["attachments"],
                poly_kwargs,
            )    

        for shape in new_shapes:
            svg.add(shape)

        y += segment["kwargs"]["h"]

def render_attachments(svg, x,y, attachment_obj, poly_kwargs):
    for attachment in attachment_obj:
        #FIXME: Duplicated in render_stack.
        if "style" in attachment:
            attachment_poly_kwargs = get_poly_kwargs_from_style_obj(attachment["style"])
            for k,v in poly_kwargs.items():
                if not k in attachment_poly_kwargs:
                    attachment_poly_kwargs[k] = v
        
        else:
            attachment_poly_kwargs = poly_kwargs


        # print(json.dumps(attachment, indent=2))

        if attachment["shape"] != "stack":
            new_shapes = shape_funcs[attachment["shape"]](
                x,y,
                poly_kwargs=attachment_poly_kwargs,
                **attachment["kwargs"]
            )

            for shape in new_shapes:
                svg.add(shape)

        else:
            for x_offset in attachment["x_offsets"]:
                render_stack(
                    svg,
                    x+x_offset,
                    y+attachment["y_offset"],
                    attachment["segments"],
                    poly_kwargs,
                )
            # assert(False)


def render_rocket(rocket):
    poly_kwargs = get_poly_kwargs_from_style_obj(rocket["style"])

    svg = svgwrite.Drawing('test.svg')
    x,y = 200, 10
    render_stack(
        svg, x, y,
        rocket["segments"],
        poly_kwargs,
    )
    # file("output/rocket_"+str(i)+".svg", "w").write(svg.tostring())
    return svg
