#! /usr/bin/env python

# Jemals 2015
# Version 1.0
#
# THERE IS NO WARRANTY FOR THIS SOFTWARE
# THERE IS NO LICENSE

import math


# General %uncertainty functions
def percented_list(value_list, uncertainty_list):
    out_list = []
    for i in range(0, len(value_list) ):
        out_list.append(round( (float(uncertainty_list[i]) / float(value_list[i])*100.0), 2))
    return out_list


def combo_list(cented_read, cented_rand, cented_calib):
    combo_list = []

    # try to find the shortest list so to avoid errors. Shouldn't matter here
    if len(cented_read) < len(cented_rand) < len(cented_calib):
        shortest = len(cented_read)
    elif len(cented_rand) < len(cented_read) < len(cented_calib):
        shortest = len(cented_rand)
    else:
        shortest = len(cented_calib)

    for i in range(0, shortest):
        combo_list.append(round(math.sqrt(cented_read[i]**2 + cented_rand[i]**2 + cented_calib[i]**2), 2))

    return combo_list

def powerFix(combo_list, term_power):
    combo_sqr = []
    for i in range(0, len(combo_list)):
        combo_sqr.append(combo_list[i] * term_power)
    return combo_sqr



# %uncertainty functions
def get_centReading_unc(value_list, scale_unc):
    read_unc_list = []
    for i in range(0, len(value_list)):
        read_unc_list.append(round((scale_unc / value_list[i])*100, 2))
    return read_unc_list



def get_calibration_unc(value_list):
    calib_list = []
    for i in range(0, len(value_list)):
        if value_list[i] == 0:
            print("Empty entry @ {0}, resorting to 0 val".format(value_list[i]))
            calib_list.append(0.0)
        else:
            calib_list.append(round(round(value_list[i]*0.005, 4) + float("0."+ ( len(str(round(value_list[i]*0.005, 4)))-3) *"0" +"1"),4))

    return calib_list



def get_random_unc(repeated_results):
    sorted_list = []
    for i in range(0, len(repeated_results)):
        sorted_list.append(sorted(repeated_results[i]))

    random_uns = []
    for i in range(0, len(sorted_list)):
        random_uns.append(round((sorted_list[i][-1] - sorted_list[i][0]) / len(sorted_list[i]), 4))

    return random_uns
