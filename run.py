import numpy as np
import matplotlib.pyplot as plt
import time
import math
from mpl_toolkits.mplot3d import Axes3D
import ball_physics as bp

def show_help():
    help_message = (
        "         //////  //////  //  //////          ",
        "             //  //  //  //  //  //          ",
        "         //////  //  //  //  //////          ",
        "         //      //  //  //  //  //          ",
        "         //////  //////  //  //////          ",
        "\n\n\n",
        "# gravity trail program by CJK \n",
        "# all inputs should be divided by space\n",
        """# type 'draw' 'axes of x y z' 'speed of x y z' 'gravity power acceleration' in order
          it will show you the trail of thrown ball.
          {the scale of position is (m), scale of velocity is (m/s) and accleration is (m/s^2)}
          
          ex) draw 20 20 20 10 10 20 9.8\n""",
        """# type 'where''axes of x y z' 'speed of x y z' 'gravity power acceleration' 'time' in order
          it will show where your ball is.
          {the scale of position is (m), scale of velocity is (m/s) and accleration is (m/s^2)}
          
          ex) where 10 10 10 20 20 20 9.8 7\n""",
        """# type 'contributor'
             it will show lists of contributor\n\n\n"""
    )

    for i in help_message:
        print(i)
        time.sleep(0.2)

    return 0


# Program will start here!!

print(
    """
    ==================================================
    --------------------------------------------------
    ------------Throw Trail trace program!------------
    --------------------------------------------------
    ==================================================
    
                : Made by Chang Jang Kim : 
    
                  # type help for info #
    
    """
)


while True:

    cmds = input(">> ").split(" ")

    cmd = cmds[0]
    args = tuple(cmds[1:])

    if cmd == "":
        pass

    elif cmd == "draw":
        bp.draw(args)

    elif cmd == "help":
        show_help()

    elif cmd == "where":
        bp.where(args)

    elif cmd == "contributor":
        print("      Chris Yunbin Chang")
        print("      Hoyeon Jang")
        print("      Dongjae Kim")
        print("      BO KYUNG <3")

    else:
        print("Wrong Command!")