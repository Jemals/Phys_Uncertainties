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

cented_reading_T = percented_list(raw_average_T,
                                  get_reading_unc(raw_average_T, 0.01))
cented_calibration_T = percented_list(raw_average_T,
                                     get_calibration_unc(raw_average_T))
print(get_calibration_unc(raw_average_T))

cented_random_T = percented_list(raw_average_T,
                                 get_random_unc(raw_repeated_T))
overall_unc_T = combo_list( cented_reading_T,
                          cented_calibration_T,
                          cented_random_T
                        )

print("""T values:
         {0}
         Percent Reading:
         {1}
         Percent Calibration:
         {2}
         Percent Random:
         {3}
         Percent Overall:
         {4}""".format(cented_reading_T,
                       cented_calibration_T,
                       cented_random_T,
                       overall_unc_T
                      ))
