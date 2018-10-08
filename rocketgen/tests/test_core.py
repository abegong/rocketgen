import svgwrite

from rocketgen import (
    render_rocket,
    generate_random_rocket,
)

sub_stack = {
    "segments" : [{
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
        "shape" : "trapezoid",
        "kwargs" : {
            "w" : 40,
            "h" : 15,
            "spread" : .75,
        },
        "style" : {
            "fill" : [128,128,128]
        }
    }],
    "attachments" : [],
    "style" : {},
}


example_rocket = {
    "segments" : [{
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
        "shape" : "trapezoid",
        "kwargs" : {
            "w" : 40,
            "h" : 15,
            "spread" : .75,
        },
        "style" : {
            "fill" : [128,128,128]
        }
    },{
        "shape" : "rectangle",
        "kwargs" : {
            "w" : 30,
            "h" : 10,
        },
        "style" : {
            "fill" : [255, 255, 255]
        }
    },{
        "shape" : "rectangle",
        "kwargs" : {
            "w" : 30,
            "h" : 60,
        }
    },{
        "shape" : "rectangle",
        "kwargs" : {
            "w" : 30,
            "h" : 10,
        },
        "style" : {
            "fill" : [255, 255, 255]
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
            "w" : 30,
            "h" : 15,
            "spread" : .75,
        },
        "style" : {
            "fill" : [128,128,128]
        }
    }],
    "attachments" : [{
        "shape" : "mirrored_poly",
        "kwargs" : {
            "x_offset" : 19,
            "y_offset" : 200,
            "points" : [[0,0], [0,30], [20, 50], [20, 30]]
        },
        "style" : {
            "fill" : [128,128,128]
        }
    },{
        "shape" : "circle",
        "kwargs" : {
            "x_offset" : 0,
            "y_offset" : 60,
            "r" : 10,
        },
        "style" : {
            "fill" : [0,0,255]
        }
    },{
        "shape" : "stack",
        "kwargs" : sub_stack,
    }],
    "style" : {
        "stroke" : [64, 64, 64],
        "stroke_width" : 4,
        "stroke_linejoin" : 'round',
        "fill" : [255,0,0],
    }
}


svg = render_rocket(example_rocket)
file("output/example_rocket_.svg", "w").write(svg.tostring())


for i in range(20):
    random_rocket = generate_random_rocket()
    svg = render_rocket(random_rocket)
    file("output/rocket_"+str(i)+".svg", "w").write(svg.tostring())
