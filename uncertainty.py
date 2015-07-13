#! /usr/bin/env python

import math

# Simplicity is the best course of action, also: I'm too tired to mess around with classes right now

# General %uncertainty functions
def percented_list(value_list, uncertainty_list):
    out_list = []
    for i in range(0, len(value_list) - 1):
        out_list.append((uncertainty_list[i] / value_list[i])*100)
    return out_list


def combo_list(cented_read, cented_rand, cented_calib):
    combo_list = []

    # try to find the shortest list so to avoid errors.
    if len(cented_read) < len(cented_rand) < len(cented_calib):
        yarr = len(cented_read)
    elif len(cented_rand) < len(cented_read) < len(cented_calib):
        yarr = len(cented_rand)
    else:
        yarr = len(cented_calib)

    for i in range(0, yarr-1):
        combo_list.append(sqrt(cented_unc1[i]**2 + cented_unc2[i]**2 + cented_unc3[i]**2))

    return combo_list

def powerFix(combo_list, term_power):		# If functions are first-order and variables are passed by reference,
    for i in range(0, len(combo_list)-1):   # no new value need be assigned so the function can be called
        combo_list[i] *= term_power         # merely to update the combined list.

       ''' combo_list is updated and so just using powerFix(combined_unc, 3) changes the original list to suit the
           power uncertainty '''

# Specific %uncertainty functions
def get_reading_unc(value_list, scale_unc):
    read_unc_list = []
    for i in range(0, len(value_list) - 1):
        read_unc_list.append(scale_unc / value_list[i])
    return read_unc_list

#def getLeastSF(dec_value): # Potentially unsafe as I don't check if it's actually a decimal value
'''GET TO THIS!!!'''


def get_calibration_unc(value_list):
    calib_list = []
    for i in range(0, len(value_list)-1):
        if value_list[i] == 0:
            print("Empty entry!")
        elif value_list[i] in range(0.001, 0.01):
            calib_list.append(0.005*value_list[i])
        elif value_list[i] in range(0.0001, 0.001):
            calib_list.append(0.005*value_list[i] + 0.0001)
        elif value_list[i] in range(0.00001, 0.0001):
            calib_list.append(0.005*value_list[i] + 0.00001)
        elif value_list[i] in range(0.000001, 0.00001):
            calib_list.append(0.005*value_list[i] + 0.000001)
        else:
            print("Error! Entry {0} within unknown range!".format(i))
            calib_list.append("Exceptional value")
    return calib_list

def get_random_unc(repeated_results):
    #number_values = len(repeated_results[0])
    sorted_list = qSort(repeated_results)

    random_uns = []
    for i in range(0, len(repeated_results)-1):
        random_uncs.append((sorted_list[i][-1] - sorted_list[i][0]) / len(repeated_values[i]))

    return ( (sorted_list[-1] - sorted_list[0]) / len(repeated_values[0]) )

# General
def qSort(repeated_list):
    if repeated_list == []:
        return []
    else:
        for i in range(0, len(repeated_list[0])-1):
            pivot = repeated_list[i][0]
            lesser = qSort([x for x in repeated_list[1:] if x < pivot])
            greater = qSort([x for x in repeated_list[1:] if x >= pivot])
            sorted_list.append(lesser + [pivot] + greater)
        return sorted_list
