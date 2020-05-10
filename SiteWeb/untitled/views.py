from django.shortcuts import render
import sys


def home(request):
    return render(request, 'index.html')


def animation(request):
    res = request._post
    taille = res['taille']
    ecart = res['ecart']
    embranchement = res['embarnchement']
    apex = res['nbapex']
    angle1 = res['angle1']
    angle2 = res['angle2']
    angle3 = res['angle3']
    ecart1 = res['ecart1']
    ecart2 = res['ecart2']
    ecart3 = res['ecart3']

    para = {"taille": taille, "ecart": ecart, "embranchement": embranchement, "apex":  apex, "angle1": angle1, "angle2": angle2, "angle3": angle3,
            "ecart1": ecart1,  "ecart2": ecart2,  "ecart3": ecart3
            }
    print(para, file=sys.stderr)
    return render(request, 'animation.html', {'para': para})


