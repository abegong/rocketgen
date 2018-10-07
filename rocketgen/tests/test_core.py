
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
            "w" : 20,
            "h" : 40,
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

svg = svgwrite.Drawing('test.svg')
x,y = 100, 10
for shape in example_rocket["stack"]:
    svg.add(
    	shape_funcs[shape["shape"]](
    		x,y,
    		poly_kwargs=default_poly_kwargs,
    		**shape["kwargs"]
    	)
    )
    y += shape["kwargs"]["h"]

# display(SVG(svg.tostring()))
file("test_svg.svg", "w").write(svg.tostring())
