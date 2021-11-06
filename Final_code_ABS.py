import numpy as np
from matplotlib import pyplot as plt
import memberships as mem



# modelling - input - speed--------------------------------------
speed = np.linspace(0,200,400)
slow_speed = np.zeros_like(speed)
med_speed = np.zeros_like(speed)
fast_speed = np.zeros_like(speed)

for i in range(len(speed)):
    slow_speed[i] = mem.dec(speed[i],35,60)
    med_speed[i] = mem.trap(speed[i],50,80,80,100)
    fast_speed[i] = mem.inc(speed[i],90,120)

# modelling - input - distance-----------------------------------
distance = np.linspace(0,20,300)
near = np.zeros_like(distance)
far = np.zeros_like(distance)

for i in range(len(distance)):
    near[i] = mem.dec(distance[i],3,12)
    far[i] = mem.inc(distance[i],10,17)

# modelling - input - dry-asphalt & snow - wheel slip---------------------
slip = np.linspace(-0.75,0.75,500)
dry_opt = np.zeros_like(slip)
dry_non_opt = np.zeros_like(slip)
snow_opt = np.zeros_like(slip)
snow_non_opt = np.zeros_like(slip)

for i in range(len(slip)):
    dry_opt[i] = mem.gaussian(slip[i],0.3,0.08)
    dry_non_opt[i] = mem.sig(slip[i],30,0.4)
    snow_opt[i] = mem.gaussian(slip[i],0.25,0.06)
    snow_non_opt[i] = mem.sig(slip[i],30,0.33)


# modelling - input - surface condition---------------------------
road = np.linspace(0,10,300)
dry = np.zeros_like(road)
snow = np.zeros_like(road)

for i in range(len(road)):
    dry[i] = mem.dec(road[i],2,6)
    snow[i] = mem.inc(road[i],4,9)

# modelling - output - brake---------------------------------------
brake = np.linspace(0,10,300)
Long = np.zeros_like(brake)
med = np.zeros_like(brake)
short = np.zeros_like(brake)

for i in range(len(brake)):
    short[i] = mem.dec(brake[i],1,4)
    med[i] = mem.trap(brake[i],2,4,6,8)
    Long[i] = mem.inc(brake[i],6,8)

# Looping function - user - main menu
def main_menu(menu_option):
    while menu_option == 0:
        try:
            print("please select options what would you like to do?\n\n"
                , "(1)\tFuzzy function.\n"
                , "(2)\tClose program.\n")
            menu_option = int(input("enter option\t: "))
            if menu_option == 1:
                while menu_option == 1:
                    try:
                        inp_speed = int(input("enter Vehicle speed (range within 0 - 200Kmh):\t\t\t"))
                        if inp_speed < 0:
                            print("invalid input, your input speed response must not be negative.\n")
                            continue
                        elif inp_speed > 200:
                            print("invalid input, your input speed must be within speed 0 - 200 Kmh range.\n")
                            continue
                        inp_dist = int(input("enter Distance away from the vehicle (range within 0 - 20m):\t"))
                        if inp_dist < 0:
                            print("invalid input, your input distance response must not be negative.\n")
                            continue
                        elif inp_dist > 20:
                            print("invalid input, your input distance must be within distance 0- 20m range.\n")
                            continue
                        inp_slip = float(input("enter wheel slip (range within 0 - 0.75):\t\t\t"))
                        if inp_slip < 0:
                            print("invalid input, your input wheel slip response must not be negative.\n")
                            continue
                        if inp_slip > 0.5:
                            print("invalid input, your input wheel slip must be within 0 - 0.75 range limit.\n")
                            continue
                        inp_cond = int(input("enter Surface condition (range within 0 - 10 scale):\t\t"))
                        if inp_cond < 0:
                            print("invalid input, your input road condition response must not be negative.\n")
                            continue
                        elif inp_cond > 10:
                            print("invalid input, your input road condition must be within scale of 1 - 10 range.\n")
                            continue
                        else:
                            input_param(inp_speed,inp_dist,inp_slip,inp_cond)
                            break
                    except ValueError:
                        print("Wrong input, please try again.\n")
                        continue
            elif menu_option == 2:
                while menu_option == 2:
                    print("quit program.")
                    quit()
        except ValueError:
            print("Wrong input, please try again.\n")

# Inputs and Evaluation--------------------------------------------
def input_param(inp_speed,inp_dist,inp_slip,inp_cond):
    # input speed 
    inp_slow=mem.dec(inp_speed,35,60)
    inp_med=mem.trap(inp_speed,50,80,80,100)
    inp_fast=mem.inc(inp_speed,90,120)

    # input distance
    inp_near=mem.dec(inp_dist,3,12)
    inp_far=mem.inc(inp_dist,10,17)

    # input slip
    inp_dry_opt=mem.gaussian(inp_slip,0.3,0.08)
    inp_dry_non_opt=mem.sig(inp_slip,30,0.4)
    inp_snow_opt=mem.gaussian(inp_slip,0.25,0.06)
    inp_snow_non_opt=mem.sig(inp_slip,30,0.33)

    # input surface condition
    inp_dry=mem.dec(inp_cond,2,6)
    inp_snow=mem.inc(inp_cond,4,9)

    # Rules---------------------------------------------------------
    # Rule 1: surface condition is dry-asphalt
    #                     speed is fast
    #                  distance is far 
    #                wheel slip is dry-asphalt optimal 
    res1=np.minimum(inp_dry,inp_fast)
    res2=np.minimum(inp_far,res1)
    res3=np.minimum(inp_dry_opt,res2)
    R1 = np.fmin(res3, Long)

    # Rule 2: surface condition is dry-asphalt
    #                     speed is fast
    #                  distance is far 
    #                wheel slip is dry-asphalt non-optimal 
    res1=np.minimum(inp_dry,inp_fast)
    res2=np.minimum(inp_far,res1)
    res3=np.minimum(inp_dry_non_opt,res2)
    R2 = np.fmin(res3, med)

    # Rule 3: surface condition is dry-asphalt
    #                     speed is fast
    #                  distance is near 
    #                wheel slip is dry-asphalt optimal 
    res1=np.minimum(inp_dry,inp_fast)
    res2=np.minimum(inp_near,res1)
    res3=np.minimum(inp_dry_opt,res2)
    R3 = np.fmin(res3, short)

    # Rule 4: surface condition is dry-asphalt
    #                     speed is fast
    #                  distance is near 
    #                wheel slip is dry-asphalt non-optimal 
    res1=np.minimum(inp_dry,inp_fast)
    res2=np.minimum(inp_near,res1)
    res3=np.minimum(inp_dry_non_opt,res2)
    R4 = np.fmin(res3, short)

    # Rule 5: surface condition is snow
    #                     speed is fast
    #                  distance is far 
    #                wheel slip is snow optimal 
    res1=np.minimum(inp_snow,inp_fast)
    res2=np.minimum(inp_far,res1)
    res3=np.minimum(inp_snow_opt,res2)
    R5 = np.fmin(res3, short)

    # Rule 6: surface condition is snow
    #                     speed is fast
    #                  distance is far 
    #                wheel slip is snow non-optimal 
    res1=np.minimum(inp_snow,inp_fast)
    res2=np.minimum(inp_far,res1)
    res3=np.minimum(inp_snow_non_opt,res2)
    R6 = np.fmin(res3, med)

    # Rule 7: surface condition is snow
    #                     speed is fast
    #                  distance is near 
    #                wheel slip is snow optimal 
    res1=np.minimum(inp_snow,inp_fast)
    res2=np.minimum(inp_near,res1)
    res3=np.minimum(inp_snow_opt,res2)
    R7 = np.fmin(res3, short)

    # Rule 8: surface condition is snow
    #                     speed is fast
    #                  distance is near 
    #                wheel slip is snow non-optimal 
    res1=np.minimum(inp_snow,inp_fast)
    res2=np.minimum(inp_near,res1)
    res3=np.minimum(inp_snow_non_opt,res2)
    R8 = np.fmin(res3, short)

    # Rule 9: surface condition is dry-asphalt
    #                     speed is medium
    #                  distance is far 
    #                wheel slip is optimal 
    res1=np.minimum(inp_dry,inp_med)
    res2=np.minimum(inp_far,res1)
    res3=np.minimum(inp_dry_opt,res2)
    R9 = np.fmin(res3, Long)

    # Rule 10: surface condition is dry-asphalt
    #                     speed is med
    #                  distance is far 
    #                wheel slip is non-optimal 
    res1=np.minimum(inp_dry,inp_med)
    res2=np.minimum(inp_far,res1)
    res3=np.minimum(inp_dry_non_opt,res2)
    R10 = np.fmin(res3, med)

    # Rule 11: surface condition is dry-asphalt
    #                     speed is med
    #                  distance is near 
    #                wheel slip is optimal 
    res1=np.minimum(inp_dry,inp_med)
    res2=np.minimum(inp_near,res1)
    res3=np.minimum(inp_dry_opt,res2)
    R11 = np.fmin(res3, med)

    # Rule 12: surface condition is dry-asphalt
    #                     speed is med
    #                  distance is near 
    #                wheel slip is non-optimal 
    res1=np.minimum(inp_dry,inp_med)
    res2=np.minimum(inp_near,res1)
    res3=np.minimum(inp_dry_non_opt,res2)
    R12 = np.fmin(res3, med)

    # Rule 13: surface condition is snow
    #                     speed is med
    #                  distance is far 
    #                wheel slip is optimal 
    res1 = np.minimum(inp_snow,inp_med)
    res2 = np.minimum(inp_far, res1)
    res3 = np.minimum(inp_snow_opt, res2)
    R13 = np.fmin(res3, short)

    
    # Rule 14: surface condition is snow
    #                     speed is med
    #                  distance is far 
    #                wheel slip is non optimal 
    res1 = np.minimum(inp_snow,inp_med)
    res2 = np.minimum(inp_far, res1)
    res3 = np.minimum(inp_snow_non_opt, res2)
    R14 = np.fmin(res3, med)

    
    # Rule 15: surface condition is snow
    #                     speed is med
    #                  distance is near 
    #                wheel slip is optimal 
    res1 = np.minimum(inp_snow,inp_med)
    res2 = np.minimum(inp_near, res1)
    res3 = np.minimum(inp_snow_opt, res2)
    R15 = np.fmin(res3, med)


    # Rule 16: surface condition is snow
    #                     speed is med
    #                  distance is near 
    #                wheel slip is non optimal 
    res1 = np.minimum(inp_snow,inp_med)
    res2 = np.minimum(inp_near, res1)
    res3 = np.minimum(inp_snow_non_opt, res2)
    R16 = np.fmin(res3, short)

    
    # Rule 17: surface condition is dry
    #                     speed is slow
    #                  distance is far 
    #                wheel slip is optimal 
    res1 = np.minimum(inp_dry,inp_slow)
    res2 = np.minimum(inp_far, res1)
    res3 = np.minimum(inp_dry_opt, res2)
    R17 = np.fmin(res3, Long)

    
    # Rule 18: surface condition is dry
    #                     speed is slow
    #                  distance is far 
    #                wheel slip is non optimal  
    res1 = np.minimum(inp_dry,inp_slow)
    res2 = np.minimum(inp_far, res1)
    res3 = np.minimum(inp_dry_non_opt, res2)
    R18 = np.fmin(res3, Long)

    
    # Rule 19: surface condition is dry
    #                     speed is slow
    #                  distance is near 
    #                wheel slip is optimal  
    res1 = np.minimum(inp_dry,inp_slow)
    res2 = np.minimum(inp_near, res1)
    res3 = np.minimum(inp_dry_opt, res2)
    R19 = np.fmin(res3, med)

    
    # Rule 20: surface condition is dry
    #                     speed is slow
    #                  distance is near 
    #                wheel slip is non optimal 
    res1 = np.minimum(inp_dry,inp_slow)
    res2 = np.minimum(inp_near, res1)
    res3 = np.minimum(inp_dry_non_opt, res2)
    R20 = np.fmin(res3, short)


    # Rule 21: surface condition is snow
    #                     speed is slow
    #                  distance is far 
    #                wheel slip is optimal 
    res1 = np.minimum(inp_snow,inp_slow)
    res2 = np.minimum(inp_far, res1)
    res3 = np.minimum(inp_snow_opt, res2)
    R21 = np.fmin(res3, med)


    # Rule 22: surface condition is snow
    #                     speed is slow
    #                  distance is far 
    #                wheel slip is non optimal 
    res1 = np.minimum(inp_snow,inp_slow)
    res2 = np.minimum(inp_far, res1)
    res3 = np.minimum(inp_snow_non_opt, res2)
    R22 = np.fmin(res3, Long)

    
    # Rule 23: surface condition is snow
    #                     speed is slow
    #                  distance is near 
    #                wheel slip is optimal 
    res1 = np.minimum(inp_snow,inp_slow)
    res2 = np.minimum(inp_near, res1)
    res3 = np.minimum(inp_snow_opt, res2)
    R23 = np.fmin(res3, med)


    # Rule 24: surface condition is snow
    #                     speed is slow
    #                  distance is near 
    #                wheel slip is non optimal  
    res1 = np.minimum(inp_snow,inp_slow)
    res2 = np.minimum(inp_near, res1)
    res3 = np.minimum(inp_snow_non_opt, res2)
    R24 = np.fmin(res3, short)

    # Summarization of rules
    Rules = np.maximum(R1,np.maximum(R2,np.maximum
                    (R3,np.maximum(R4,np.maximum
                    (R5,np.maximum(R6,np.maximum
                    (R7,np.maximum(R8,np.maximum
                    (R9,np.maximum(R10,np.maximum
                    (R11,np.maximum(R12,np.maximum
                    (R13,np.maximum(R14,np.maximum
                    (R15,np.maximum(R16,np.maximum
                    (R17,np.maximum(R18,np.maximum
                    (R19,np.maximum(R20,np.maximum
                    (R21,np.maximum(R22,np.maximum
                    (R23,R24)))))))))))))))))))))))

    # Defuzzification 
    expected_ABS = np.trapz(Rules*brake,brake)/np.trapz(Rules,brake)
    
    print("\nSpeed =\t",inp_speed,"\nSlow  =\t",inp_slow, "\nMedium =",inp_med, "\nFast =\t",inp_fast)
    print("\n\nDistance =", inp_dist, "\nNear =\t",inp_near,"\nFar =\t",inp_far)
    print("\n\nDry-asphalt wheel slip =",inp_slip,"\nOptimal =\t\t\t",inp_dry_opt,"\nNon-optimal =\t\t\t",inp_dry_non_opt)
    print("\n\nSnow wheel slip =\t",inp_slip,"\nOptimal =\t",inp_snow_opt,"\nNon-optimal =\t",inp_snow_non_opt)
    print("\n\nSurface Condition =", inp_cond,"\nDry-asphalt =\t\t", inp_dry,"\nSnow = \t\t\t", inp_snow)
    print("\nABS output = ", expected_ABS)
    #8print("Rules= ", Rules)
    plots(inp_speed,inp_slow,inp_med,inp_fast,inp_dist,inp_near,inp_far,inp_slip,inp_dry_non_opt,inp_dry_opt,inp_snow_opt,inp_snow_non_opt,inp_cond,inp_dry,inp_snow,Rules)


def plots(inp_speed,inp_slow,inp_med,inp_fast,inp_dist,inp_near,inp_far,inp_slip,inp_dry_non_opt,inp_dry_opt,inp_snow_opt,inp_snow_non_opt,inp_cond,inp_dry,inp_snow,Rules):
    plt.figure(0)
    plt.subplot(2,1,1)
    plt.plot(speed,slow_speed,label= "Slow speed")
    plt.plot(speed,med_speed,label= "Medium speed")
    plt.plot(speed,fast_speed,label= "Fast speed")
    plt.xlabel("Measure of speed")
    plt.title("Speed of vehicle")
    plt.scatter([inp_speed,inp_speed],[inp_slow,inp_med])
    plt.scatter([inp_speed,inp_speed],[inp_med,inp_fast])
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(distance,near,label= "Near distance away from object")
    plt.plot(distance,far,label= "Far distance away from object")
    plt.xlabel("Measure of distance")
    plt.title("Distance away from object")
    plt.scatter([inp_dist,inp_dist],[inp_near,inp_far])
    plt.legend()

    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(slip,dry_opt,label= "Dry - asphalt optimal wheel slip")
    plt.plot(slip,dry_non_opt,label="Dry - asphalt Non-optimal wheel slip")
    plt.xlabel("Wheel slip ratio")
    plt.title("Ratio of dry-asphalt condition wheel slip")
    plt.scatter([inp_slip,inp_slip],[inp_dry_non_opt,inp_dry_opt])
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(slip,snow_opt,label= "Snow optimal wheel slip")
    plt.plot(slip,snow_non_opt,label="Snow Non-optimal wheel slip")
    plt.xlabel("Wheel slip ratio")
    plt.title("Ratio of snow condition wheel slip")
    plt.scatter([inp_slip,inp_slip],[inp_snow_non_opt,inp_snow_opt])
    plt.legend()

    plt.figure(2)
    plt.plot(road,dry,label= "Dry road condition")
    plt.plot(road,snow,label= "Snow road condition")
    plt.xlabel("Surface Condition")
    plt.title("Measure of dry or snow")
    plt.scatter([inp_cond,inp_cond],[inp_dry,inp_snow])
    plt.legend()

    plt.figure(3)
    plt.plot(brake,short,label= "Short duration intermitten brake")
    plt.plot(brake,med,label= "Medium duration intermitten brake")
    plt.plot(brake,Long,label= "Long duration intermitten brake")
    plt.fill_between(brake,Rules,color=(1,0,0))
    plt.xlabel("ABS output intermittent duration")
    plt.title("ABS output")
    plt.legend()
    plt.show()
    main_menu(menu_option)
menu_option = 0; 


# -----------------------------FRONT END DISPLAY -------------------------
print("\n\n#######################################"
      , "\n#   Welcome to ABS Fuzzy Application  # "
      , "\n#######################################"
      , "\n\n -----------------------------------"
      , "\n         please select Menu       \n"
      , "-----------------------------------")
# the whole program runs over a main function to start.
main_menu(menu_option)
