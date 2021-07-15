#ifndef __SILICON_LABS_CSLIB_HWCONFIG_H
#define __SILICON_LABS_CSLIB_HWCONFIG_H
// Defines the size of the sensor node array, as well as other non-volatile and
// volatile arrays that have a one-to-one correspondence to the number of
// sensors in the project.
#define DEF_NUM_SENSORS 3

// Removing the last sensor, P1.4 is grounded by default on the SLSTK2010A
// $[mux values]
#define MUX_VALUE_ARRAY \
  0x06,     /* CS0.6 */ \
  0x07,     /* CS0.7 */ \
  0x08,     /* CS1.0 */ \
  0x09,     /* CS1.1 */ \
  0x0A,     /* CS1.2 */ \
  0x0B,     /* CS1.3 */ \
  0x0C,     /* CS1.4 */ \
// [mux values]$

// $[gain values]
#define GAIN_VALUE_ARRAY \
  0x07,     /* CS0.6 */ \
  0x07,     /* CS0.7 */ \
  0x07,     /* CS1.0 */ \
  0x07,     /* CS1.1 */ \
  0x07,     /* CS1.2 */ \
  0x07,     /* CS1.3 */ \
  0x07,     /* CS1.4 */ \
// [gain values]$

// $[accumulation values]
#define ACCUMULATION_VALUE_ARRAY \
  0x05,     /* CS0.6 */ \
  0x05,     /* CS0.7 */ \
  0x05,     /* CS1.0 */ \
  0x05,     /* CS1.1 */ \
  0x05,     /* CS1.2 */ \
  0x05,     /* CS1.3 */ \
  0x05,     /* CS1.4 */ \
// [accumulation values]$

#define ACTIVE_THRESHOLD_ARRAY 70, 70, 70  //, 70
#define INACTIVE_THRESHOLD_ARRAY 30, 30, 30  //, 30

// No overlay average touch delta
#define AVERAGE_TOUCH_DELTA_ARRAY 4080>>4, 4080>>4, 4080>>4  //, 4080>>4
// 1/16" overlay average touch delta
//#define AVERAGE_TOUCH_DELTA_ARRAY 400>>4, 400>>4, 400>>4  //, 200>>4
// 1/8" overlay average touch delta
//#define AVERAGE_TOUCH_DELTA_ARRAY 200>>4, 200>>4, 200>>4  //, 200>>4

// Pin mask used for port register config in sleep mode
// $[Active mode mask]
#define ACTIVE_MODE_MASK_P0   0xC0
#define ACTIVE_MODE_MASK_P1   0x1F
// [Active mode mask]$

// $[Sleep mode mask]
#define SLEEP_MODE_MASK_P0    0xC0
#define SLEEP_MODE_MASK_P1    0x1F
// [Sleep mode mask]$
#endif // __SILICON_LABS_CSLIB_HWCONFIG_H
// $[active threshold values]
#define ACTIVE_THRESHOLD_ARRAY \
  70,       /* CS0.6 */ \
  70,       /* CS0.7 */ \
  70,       /* CS1.0 */ \
  70,       /* CS1.1 */ \
  70,       /* CS1.2 */ \
  70,       /* CS1.3 */ \
  70,       /* CS1.4 */ \
// [active threshold values]$

// $[inactive threshold values]
#define INACTIVE_THRESHOLD_ARRAY \
  30,       /* CS0.6 */ \
  30,       /* CS0.7 */ \
  30,       /* CS1.0 */ \
  30,       /* CS1.1 */ \
  30,       /* CS1.2 */ \
  30,       /* CS1.3 */ \
  30,       /* CS1.4 */ \
// [inactive threshold values]$

// $[average touch delta values]
#define AVERAGE_TOUCH_DELTA_ARRAY \
  1000>>4,  /* CS0.6 */ \
  1000>>4,  /* CS0.7 */ \
  1000>>4,  /* CS1.0 */ \
  1000>>4,  /* CS1.1 */ \
  1000>>4,  /* CS1.2 */ \
  1000>>4,  /* CS1.3 */ \
  1000>>4,  /* CS1.4 */ \
// [average touch delta values]$

