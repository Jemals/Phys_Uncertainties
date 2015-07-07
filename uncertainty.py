#! /usr/bin/env python

import math

#simplicity is the best course of action, also: I'm too tired to mess around with classes right now

def percented_list(value_list, uncertainty_list):
    out_list = []
    for i in range(0, len(value_list) - 1):
        out_list.append((uncertainty_list[i] / value_list[i])*100)
    return out_list


def combo_list(cented_read, cented_rand, cented_calib):
    combo_list = []

    #try to find the shortest list so to avoid errors.
    if len(cented_read) < len(cented_rand) < len(cented_calib):
        yarr = len(cented_read)
    elif len(cented_rand) < len(cented_read) < len(cented_calib):
        yarr = len(cented_rand)
    else:
        yarr = len(cented_calib)

    for i in range(0, yarr-1):
        combo_list.append(sqrt(cented_unc1[i]**2 + cented_unc2[i]**2 + cented_unc3[i]**2))

    return combo_list


def reading_unc_list(value_list ,scale_unc):
    read_unc_list = []
    for i in range(0, len(value_list) - 1):
        read_unc_list.append(scale_unc / value_list[i])
    return read_unc_list

def powerFix(combo_list, term_power):		#If functions are first-order and variables are passed by reference, no new value need be assigned
    for i in range(0, len(combo_list)-1):   #so the function can be called merely to update the combined list.
        combo_list[i] *= term_power
       #combo_list is updated and so just using powerFix(combined_unc, 3) changes the original list to suit the power uncertainty
