from django import template


register=template.Library()




@register.filter
def types(args):
    if args=="sorry" or args=="empty" or args=="string":
        return False
    
    else:
        return True 