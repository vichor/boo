"""
boo - Boooooohhhh module
"""

import app.boo


minmovetime=1
maxmovetime=5
minwaittime=3
maxwaittime=10
pin1=20
pin2=21

def main():
    # todo: read cfg from xml
    boo=app.boo.boo(minmovetime, maxmovetime, minwaittime, maxwaittime, pin1, pin2)
    exit = False
    while not exit:
        exit = boo.loop()


if __name__ == "__main__":
    main()
