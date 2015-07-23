#! /usr/bin/env python
from uncertainty import *

raw_average_T = [1.238, 1.284, 1.394, 1.42, 1.488]
raw_repeated_T = [
                    [1.247, 1.229],
                    [1.305, 1.263],
                    [1.416, 1.372],
                    [1.415, 1.425],
                    [1.465, 1.495]
                 ]

cented_reading_T = get_centReading_unc(raw_average_T, 0.01)  # returns a list of percentages of scale/value
cented_calibration_T = percented_list(raw_average_T,         # returns a percentage of the uncertainty over value
                                     get_calibration_unc(raw_average_T))

cented_random_T = percented_list(raw_average_T,
                                 get_random_unc(raw_repeated_T))  # returns a list of greatest value - smallest value / number of lists
overall_unc_T = combo_list( cented_reading_T,
                          cented_calibration_T,
                          cented_random_T
                        )                                         # returns a list of the combined %uncertainties of three %uncertainty lists
                                                                  # it doesn't matter if a value is 1/3 of another: they are
overall_Tsqr = powerFix( overall_unc_T , 2)                       # negligible and don't affect the value

print("""
         Average T values:
         {0}
         +--------------------------+
         Percent Reading:
         {1}
         Percent Calibration:
         {2}
         Percent Random:
         {3}
         +--------------------------+
         Percent Overall (T):
         {4}
         +--------------------------+
         Percent Overall (T^2):
         {5}""".format(raw_average_T,
                       cented_reading_T,
                       cented_calibration_T,
                       cented_random_T,
                       overall_unc_T,
                       overall_Tsqr
                      ))

raw_l = [0.3, 0.35, 0.4, 0.45, 0.5]
cented_l_read = get_centReading_unc(raw_l, 0.0005)
null_l = [0, 0, 0, 0, 0]                                      # null lists are used for combining two %uncertainty lists,
overall_l = combo_list(cented_l_read, cented_l_read, null_l)  # here these lists have equal values
print("""
         l values:
         {0}
         +--------------------------+
         Percent Reading:
         {1}
         Percent Calibration:
         {1}
         +--------------------------+
         Percent Overall (l):
         {2}""".format(raw_l,
                       cented_l_read,
                       overall_l))

input("Press enter to continue... ")

raw_s = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
cented_s_read = get_centReading_unc(raw_s, 0.0005)
null_s = [0, 0, 0, 0, 0, 0, 0, 0]
overall_s = combo_list(cented_s_read, cented_s_read, null_s)

print("""
         s values:
         {0}
         +==========================+
         Percent Reading:
         {1}
         Percent Calibration:
         {1}
         +==========================+
         Percent Overall (s):
         {2}""".format(raw_s,
                       cented_s_read,
                       overall_s))

input("Press enter to continue... ")

raw_avg_t = [0.35, 0.40, 0.62, 0.75 , 0.74, 0.86, 0.93, 1.02 ]

raw_repeated_t = [
                    [0.35, 0.36, 0.35],
                    [0.51, 0.47, 0.49],
                    [0.59, 0.68, 0.58],
                    [0.71, 0.73, 0.38],
                    [0.74, 0.75, 0.74],
                    [0.81, 0.87, 0.90],
                    [0.93, 0.91, 0.95],
                    [1.09, 0.97, 1.00]
                 ]

cented_reading_t = get_centReading_unc(raw_avg_t, 0.01)
cented_calibration_t = percented_list(raw_avg_t,
                                     get_calibration_unc(raw_avg_t))

cented_random_t = percented_list(raw_avg_t,
                                 get_random_unc(raw_repeated_t))  # a caveat here: the function identifies the divisor for
overall_unc_t = combo_list( cented_reading_t,                     # random uncertainty
                          cented_calibration_t,
                          cented_random_t
                        )
overall_tsqr = powerFix(overall_unc_t, 2)

print("""
         Average t values:
         {0}
         +=========================+
         Percent Reading:
         {1}
         Percent Calibration:
         {2}
         Percent Random:
         {3}
         +=========================+
         PercentOverall (t^2):
         {4}""".format(raw_avg_t,
                       cented_reading_t,
                       cented_calibration_t,
                       cented_random_t,
                       overall_tsqr))

overall_unc_g = combo_list(overall_tsqr, overall_s, null_s)
print("""Overall s/t^2 Uncertainty:
         {0}""".format(overall_unc_g))
