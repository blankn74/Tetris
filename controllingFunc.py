from variables import *
import winsound
from random import randint
from finaltexture import *
import time
import threading

# convert from windows cordinates to secreen cordenate so that we can use mouse cordinate in the code
def W_2_s (x,y):
    global width,hight
    xa=-1-x
    y*=-1
    ya=1-y
    xa=ceil(abs(xa/2)*width)
    ya=ceil(abs(ya/2)*hight)
    alist=[xa,ya]
    return alist


def collision():
    xvar = []
    yvar = []
    x=0
    y=0
    global name,randx,sright,sleft,sbottom,redgep,ledgep,bedgep
    right = redgep
    left = ledgep
    bottom = bedgep
    ## o shape
    if name == 'O':
        ##bottom
        xvar = (GLubyte * 1)(0)
        x,y = W_2_s(right-.05, bottom+.01)
        glReadPixels(x,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
        if xvar[0]!=51:
            sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x, y = W_2_s(left + .05, bottom+.01)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                sbottom = False
        ##right
        yvar = (GLubyte * 1)(0)
        x, y = W_2_s(right+.01, bottom+.1)
        glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
        if yvar[0] != 51:
            sright = True
        else:
            sright = False

        ## left
        yvar = (GLubyte * 1)(0)
        x,y = W_2_s(left-.01, bottom + .1)
        glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
        if yvar[0] != 51:
            sleft = True
        else:
            sleft = False

            ##shapes##
    ## i shape
    if name =='I':
        ##bottom
        if randx == 0 or randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right - .05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0]!=51:
                sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right - 0.15, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - 0.05, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y= W_2_s(left + 0.05, bottom)
                    glReadPixels(x,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
                    else:
                        xvar = (GLubyte * 1)(0)
                        x,y = W_2_s(left + 0.15, bottom)
                        glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                        if xvar[0] != 51:
                            sbottom = True
        ##right
        if randx == 0 or randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0]!=51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right, bottom + 0.15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right, bottom + 0.25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True
                    else:
                        yvar = (GLubyte * 1)(0)
                        x,y = W_2_s(right, bottom + 0.35)
                        glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                        if yvar[0] != 51:
                            sright = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
        ##left
        if randx == 0 or randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left, bottom + 0.15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    left = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left, bottom + 0.25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
                    else:
                        yvar = (GLubyte * 1)(0)
                        x,y = W_2_s(left, bottom + 0.35)
                        glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                        if yvar[0] != 51:
                            sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
    ## T shape
    if name =='T':
        ##bottom
        if randx == 0:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right -.15,bottom)
            glReadPixels(x,y+2 , 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0]!=51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .05, bottom+.1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left + .05, bottom + .1)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        elif randx == 1:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + .05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y =W_2_s(right - .05, bottom + .1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
        elif randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + .05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .15, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left + .25, bottom)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        elif randx == 3:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + .05, bottom + .1)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .05, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
        ##right and left
        if randx == 0:
            yvar = (GLubyte * 1)(0)
            x,y =W_2_s(right, bottom+0.15)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .1, bottom + 0.05)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .1, bottom + 0.05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        elif randx == 1:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.15)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .1, bottom + 0.05)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right - .1, bottom + 0.25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left, bottom + 0.05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left, bottom + 0.25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
        elif randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .1, bottom + 0.15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .1, bottom + 0.15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right, bottom + 0.15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right, bottom + 0.25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left+.1, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left, bottom + 0.15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y =W_2_s(left+.1, bottom + 0.25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
    ## z shape
    if name =='Z':
        ##bottom
        if randx == 0 or randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right -.15, bottom)
                glReadPixels(x,y+2 , 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left +.05,bottom+.1)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + 0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .05, bottom + 0.1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True

        ## right and left
        if randx == 0 or randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom+ .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(x+2,y)
                glReadPixels(right -.1, bottom+ .15, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left , bottom +.15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .1, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .15)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right , bottom + .25)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right - .1, bottom + .05)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left , bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left + .1, bottom + .25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True

    ## L shape
    if name =='L':
        ##bottom
        if randx == 0:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x, y = W_2_s(right - 0.15, bottom + .1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right - 0.25, bottom+.1)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        elif randx == 1:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.15, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - 0.05, bottom + .2)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
        elif randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x, y = W_2_s(right - 0.15, bottom)
                glReadPixels(x,y+2 , 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right - 0.25, bottom)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x, y = W_2_s(right - 0.15, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True

        ## right and left
        if randx == 0:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right, bottom + .15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left -.2, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        elif randx == 1:
            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(right, bottom + .25)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(right-.1, bottom + .05)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right-.1, bottom + .15)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(left, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(left, bottom + .25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
        elif randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(right-.2, bottom + .15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(left, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(right, bottom + .15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right, bottom + .25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(left, bottom + .05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(left - .1, bottom + .15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(left - .1, bottom + .25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True



## square
def square(x,y,r,g,b):
    glColor(r,g,b)
    glBegin(GL_POLYGON)
    glVertex2d(x-.5,y+.5)
    glVertex2d(x+.5,y+.5)
    glVertex2d(x+.5,y-.5)
    glVertex2d(x-.5,y-.5)
    glEnd()

## shape
def L():
    global name
    name = 'L'
    glScale(0.1,0.1,1)
    square(0, 0, 1, 0, 0)
    square(1, 0, 1, 1, 0)
    square(-1, 0, 0, 1, 0)
    square(1, -1, 0, 0, 1)

## Z shape
def Z():
    global name
    name = 'Z'
    glScale(0.1, 0.1, 1)
    square(0, 0.5, 1, 0, 0)
    square(0, -0.5, 1, 1, 0)
    square(1, -0.5, 0, 1, 0)
    square(-1, 0.5, 0, 0, 1)

## I shape
def I():
    global name
    name = 'I'
    glScale(0.1, 0.1, 1)
    square(0, 0.5, 1, 0, 0)
    square(0, 1.5, 1, 1, 0)
    square(0, -0.5, 0, 1, 0)
    square(0, -1.5, 0, 0, 1)

## T shape
def T():
    global name
    name = 'T'
    glScale(0.1, 0.1, 1)
    square(0, -0.5, 1, 0, 0)
    square(0, 0.5, 1, 1, 0)
    square(1, 0.5, 0, 1, 0)
    square(-1, 0.5, 0, 0, 1)

## O shape
def O():
    global name
    name = 'O'
    glScale(0.1, 0.1, 1)
    square(0.5, 0.5, 1, 0, 0)
    square(0.5, -0.5, 1, 1, 0)
    square(-0.5, .5, 0, 1, 0)
    square(-0.5, -0.5, 0, 0, 1)


def bedge(randx,randi):
    global bedgep,redgep,ledgep
    if randi ==0:
        name = 'Z'
    elif randi == 1:
        name = 'O'
    elif randi == 2:
        name = 'I'
    elif randi == 3:
        name = 'T'
    elif randi == 4:
        name = 'L'

    if name =='O':
        bedgep = .95
        redgep = 0.1
        ledgep = -0.1
        return
    if name == 'I':
        if randx == 0 or randx == 2:
            bedgep = .85
            redgep = 0.05
            ledgep = -0.05
            return
        else:
            bedgep = 1
            redgep = 0.2
            ledgep = -0.2
            return
    if name == 'T':
        if randx == 0 or randx == 2:
            bedgep = .95
            redgep = 0.15
            ledgep = -0.15
            return
        else:
            bedgep = .9
            redgep = 0.1
            ledgep = -0.1
            return
    if name == 'Z':
        if randx == 0 or randx == 2:
            bedgep = .95
            redgep = 0.15
            ledgep = -0.15
            return
        else:
            bedgep = .9
            redgep = 0.1
            ledgep = -0.1
            return

    if name == 'L':
        if randx == 0 or randx == 1 or randx == 3:
            bedgep = 0.9
        elif randx == 2:
            bedgep = 1

        if randx == 0 or randx == 2:
            redgep = 0.15
            ledgep = -0.15
        elif randx == 1 or randx == 3:
            redgep = 0.05
            ledgep = -0.05
def r0():
    glRotate(0,0,0,1)

def r90():
    glRotate(90,0,0,1)

def r180():
    glRotate(180,0,0,1)

def r270():
    glRotate(270,0,0,1)
shapes = [Z,O,I,T,L]
rotations = [r0,r90,r180,r270]



def init():
    glClearColor(.2, .2, .2, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  # l,r,b,t,n,f
    glMatrixMode(GL_MODELVIEW)


def reset():
    print("reset")

## to activate the moveing if the key is pressed
def keyboard(key,x,y):
    global keys,xd,i,started
    if key==b'p' and (started or paused):
        keys['p']=True
    if key==b'\x1b':
        keys["escape"]=True
    if key == b'\r':
        keys["enter"]=True
    if key==b'd':
        keys['d']=True
    if key==b'a':
        keys['a']=True
    if key == b'q':
        sys.exit()
def keyboards(key,x,y):
    global keys
    if key==GLUT_KEY_UP:
        keys["up"]=True
    elif key==GLUT_KEY_DOWN:
        keys["down"]=True
### to deactivate the moving if the key is not pressed
def keyboardup(key,x,y):
    global keys,flagl,flagr
    if key==b'\x1b':
        keys["escape"]=False
    if key==b'd':
        keys['d']=False
        flagr=True
    if key==b'a':
        keys['a']=False
        flagl = True

def draw():
    global flagr,flagl,xtransfer,randx,randi,ytransfer ,started, options, credits, sound
    global p, keys,bedgep,redgep,ledgep,flagt,sright,sleft,sbottom
    global paused, fin
    glDisable(GL_TEXTURE_2D)
    glClear(GL_COLOR_BUFFER_BIT)
    global width, hight
    m = (GLuint * 4)(0)
    glGetIntegerv(GL_VIEWPORT, m)
    width, hight = m[2], m[3]
    w, h = width // 2, hight // 2
    if started:
        ##if sound and started:
          ##  winsound.PlaySound('sounds/success.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_PURGE)
        if keys['p']:
            paused=True
            keys['p']=False
            started=False

        ##right bar
        glLoadIdentity()
        glTranslate(.6,0,0)
        glScale(0.1,2,1)
        square(0,0,.5,.5,.5)
        ##left bar
        glLoadIdentity()
        glTranslate(-.6, 0, 0)
        glScale(0.1, 2, 1)
        square(0, 0, .5, .5, .5)



        ##bottom bar
        glLoadIdentity()
        glRotate(90,0,0,1)
        glScale(0.2, 2, 1)
        square(0, 0, .5, .5, .5)

        ##bottom bar
        glLoadIdentity()
        glTranslate(0, -1, 0)
        glRotate(90,0,0,1)
        glScale(0.2, 2, 1)
        square(0, 0, .5, .5, .5)

        ##lines
        glLoadIdentity()
        glColor(1,1,1)
        glLineWidth(0.1)
        glBegin(GL_LINES)
        for i in range(-9,10):
            glVertex2d(0.55,i/10)
            glVertex2d(0.65,i/10)

            glVertex2d(-0.55, i/10)
            glVertex2d(-0.65, i/10)

        glEnd()

        ## Dead line
        glLoadIdentity()
        glColor(.2, 1, 1)
        glLineWidth(0.1)
        glBegin(GL_LINES)
        glVertex2d(-0.65,.8)
        glVertex2d(0.65, .8)
        glEnd()

        if bedgep > -.9 and not sbottom:
            sright = False
            sleft = False
            sbottom = False
            if bedgep < .75:
                collision()
            glLoadIdentity()
            if flagt :
                xtransfer +=.05
                redgep += .05
                ledgep += .05
                flagt = False
            ytransfer -= .001
            bedgep -= .001


            if keys['d'] and flagr  and not sright:
                xtransfer +=.1
                redgep +=.1
                ledgep +=.1
                flagr = False
            elif keys['a'] and flagl and ledgep > -0.5 and not sleft:
                xtransfer -=.1
                redgep -= .1
                ledgep -= .1
                flagl = False
            glTranslate(xtransfer, ytransfer, 0)
            rotations[randx]()
            shapes[randi]()
        else:
            sright = False
            sleft = False
            sbottom = False
            time.sleep(.5)
            xtransfer = 0
            randx = randint(0, 3)
            randi = randint(0, 4)
            ytransfer = 1.05
            bedge(randx,randi)
            print (name , randx)
            if redgep == 0.1 or redgep == 0.2:
                flagt = True
    elif options:
        DrawT(b"designs/optioninternal.png")
        if keys["up"]:
            if p == 1:
                p = 2
            else:
                p = 1
            keys["up"] = False
        elif keys["down"]:
            if p == 2:
                p = 1
            else:
                p = 2
            keys["down"] = False
        if p == 1:
            xc = -.3
            yc = .4
        elif p == 2:
            xc = -0.3
            yc = -0.2
        glColor(0, 1, 0)
        glScale(1.2, 1.2, 1)
        glTranslate(xc, yc, 0)
        glBegin(GL_POLYGON)
        glVertex(0, 0, .5)
        glVertex(-.1, .1, .5)
        glVertex(-.1, -.1, .5)
        glEnd()
        if keys["enter"]:
            if p == 1:
                reset()
            elif p == 2:
                sound = not sound
            keys["enter"] = False
        if keys["escape"]:
            options = False
            keys["escape"] = False
            p = 1
    elif fin:
        DrawT(b"designs/dexter.png")
    elif credits:
        DrawT(b"designs/aboutus.png")
        if keys["escape"]:
            credits = False
            keys["escape"] = False
            p = 1
    elif paused:
        DrawT(b"designs/pause.png")
        if keys['p']:
            started = True
            paused = False
            keys['p'] = False
        if keys["escape"]:
            paused = False
            p = 1
    else:
        DrawT(b"designs/Startpage.png")
        if keys["up"]:
            if p == 1:
                p = 3
            else:
                p -= 1
            keys["up"] = False
        elif keys["down"]:
            if p == 3:
                p = 1
            else:
                p += 1
            keys["down"] = False
        if p == 1:
            xc = -.25
            yc = .455
        elif p == 2:
            xc = -.25
            yc = .055
        elif p == 3:
            xc = .8
            yc = -.85
        glColor(0, 1, 0)
        glTranslate(xc, yc, 0)
        glBegin(GL_POLYGON)
        glVertex(0, 0, .5)
        glVertex(-.1, .1, .5)
        glVertex(-.1, -.1, .5)
        glEnd()
        if keys["enter"] and p == 1:
            started = True
            options = False
            credits = False
            keys["enter"] = False
        elif keys["enter"] and p == 2:
            options = True
            started = False
            credits = False
            keys["enter"] = False
            p = 1
        elif keys["enter"] and p == 3:
            credits = True
            started = False
            options = False
            keys["enter"] = False
            p = 1

    glFlush()
