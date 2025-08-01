
from django import template

register=template.Library()

def change_edition(value):
    if value==1:
        return 'First'
    if value==2:
        return 'Second'
    if value==3:
        return 'Third'
    if value==4:
        return 'Fourth'
    if value==5:
        return 'Fifth'
    if value==6:
        return 'Sixth'
    if value==7:
        return 'Seventh'
    return value


register.filter('change_edition',change_edition)