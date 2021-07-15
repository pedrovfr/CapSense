################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../lib/efm8sb1/cslib/serial_interface/comm_routines.c \
../lib/efm8sb1/cslib/serial_interface/profiler_interface.c \
C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/serial_interface/sensor_descriptors.c 

OBJS += \
./lib/efm8sb1/cslib/serial_interface/comm_routines.OBJ \
./lib/efm8sb1/cslib/serial_interface/profiler_interface.OBJ \
./lib/efm8sb1/cslib/serial_interface/sensor_descriptors.OBJ 


# Each subdirectory must supply rules for building sources it contributes
lib/efm8sb1/cslib/serial_interface/%.OBJ: ../lib/efm8sb1/cslib/serial_interface/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Keil 8051 Compiler'
	C51 "@$(patsubst %.OBJ,%.__i,$@)" || $(RC)
	@echo 'Finished building: $<'
	@echo ' '

lib/efm8sb1/cslib/serial_interface/comm_routines.OBJ: C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/lib/efm8sb1/cslib/serial_interface/comm_routines.h C:/SiliconLabs/SimplicityStudio/v4/developer/toolchains/keil_8051/9.60/INC/STDIO.H C:/SiliconLabs/SimplicityStudio/v4/developer/toolchains/keil_8051/9.60/INC/STDLIB.H C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/inc/SI_EFM8SB1_Defs.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/si_toolchain.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdbool.h

lib/efm8sb1/cslib/serial_interface/profiler_interface.OBJ: C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_hwconfig.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/lib/efm8sb1/cslib/serial_interface/profiler_interface.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Lib/efm8_capsense/cslib.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/lib/efm8sb1/cslib/serial_interface/comm_routines.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_sensor_descriptors.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Lib/efm8_capsense/si_toolchain_select.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/si_toolchain.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdbool.h

lib/efm8sb1/cslib/serial_interface/sensor_descriptors.OBJ: C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/serial_interface/sensor_descriptors.c
	@echo 'Building file: $<'
	@echo 'Invoking: Keil 8051 Compiler'
	C51 "@$(patsubst %.OBJ,%.__i,$@)" || $(RC)
	@echo 'Finished building: $<'
	@echo ' '

lib/efm8sb1/cslib/serial_interface/sensor_descriptors.OBJ: C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_hwconfig.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/si_toolchain.h C:/SiliconLabs/SimplicityStudio/v4/developer/toolchains/keil_8051/9.60/INC/STDIO.H C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_sensor_descriptors.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_config.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdbool.h


