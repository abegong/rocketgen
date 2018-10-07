import svgwrite

from rocketgen import (
    shape_funcs,
    render_stack,
    generate_random_rocket,
)

default_poly_kwargs = {
    "stroke" : svgwrite.rgb(64, 64, 64),
    "stroke_width" : 4,
    "stroke_linejoin" : 'round',
    "fill" : svgwrite.rgb(255,0,0),
}

example_rocket = {
    "stack" : [{
        "shape" : "isotri",
        "kwargs" : {
            "w" : 40,
            "h" : 40,
        }
    },{
        "shape" : "rectangle",
        "kwargs" : {
            "w" : 40,
            "h" : 40,
        }
    },{
        "shape" : "rectangle",
        "kwargs" : {
            "w" : 30,
            "h" : 60,
        }
    },{
        "shape" : "trapezoid",
        "kwargs" : {
            "w" : 20,
            "h" : 40,
            "spread" : 1.5
        }
    }],
    "attachments" : [],
    "style" : {
        "stroke" : [64, 64, 64],
        "stroke_width" : 4,
        "stroke_linejoin" : 'round',
        "fill" : [255,0,0],
    }
}


for i in range(20):
    random_rocket = generate_random_rocket()
    svg = svgwrite.Drawing('test.svg')
    x,y = 100, 10
    render_stack(
        svg, x, y,
        random_rocket["stack"],
        # example_rocket["stack"],
        default_poly_kwargs,
    )
    file("output/rocket_"+str(i)+".svg", "w").write(svg.tostring())


