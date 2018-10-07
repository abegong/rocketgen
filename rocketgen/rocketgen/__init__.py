import random

from .core import (
	shape_funcs,
)

def render_stack(svg, x, y, stack_obj, poly_kwargs):
    for shape in stack_obj:
        svg.add(
        	shape_funcs[shape["shape"]](
        		x,y,
        		poly_kwargs=poly_kwargs,
        		**shape["kwargs"]
        	)
        )
        y += shape["kwargs"]["h"]

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
	stack = []

	last_w = 10+random.random()*100
	for i in range(random.randint(3,8)):
		segment, last_w = generate_random_stack_segment(
			last_w,
			is_top=i==0,
			is_last=False,
		)
		stack.append(segment)

	return {
	    "stack" : stack,
	    "attachments" : [],
	    "style" : {
	        "stroke" : [64, 64, 64],
	        "stroke_width" : 4,
	        "stroke_linejoin" : 'round',
	        "fill" : [255,0,0],
	    }
	}
