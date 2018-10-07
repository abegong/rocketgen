import svgwrite

def get_poly_kwargs_from_style_obj(style_obj):
    return_obj = {}

    for k,v in style_obj.items():
        #FIXME: This is a really hacky way to extract and convert rgb objects
        if type(v)==list:
            return_obj[k] = svgwrite.rgb(v[0], v[1], v[2])
        else:
            return_obj[k] = v

    return return_obj