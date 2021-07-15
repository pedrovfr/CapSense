################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/hardware_config.c \
C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/hardware_routines.c \
C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/low_power_config.c 

OBJS += \
./lib/efm8sb1/cslib/device_layer/hardware_config.OBJ \
./lib/efm8sb1/cslib/device_layer/hardware_routines.OBJ \
./lib/efm8sb1/cslib/device_layer/low_power_config.OBJ 


# Each subdirectory must supply rules for building sources it contributes
lib/efm8sb1/cslib/device_layer/hardware_config.OBJ: C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/hardware_config.c
	@echo 'Building file: $<'
	@echo 'Invoking: Keil 8051 Compiler'
	C51 "@$(patsubst %.OBJ,%.__i,$@)" || $(RC)
	@echo 'Finished building: $<'
	@echo ' '

lib/efm8sb1/cslib/device_layer/hardware_config.OBJ: C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_hwconfig.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/hardware_routines.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_config.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/si_toolchain.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdbool.h

lib/efm8sb1/cslib/device_layer/hardware_routines.OBJ: C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/hardware_routines.c
	@echo 'Building file: $<'
	@echo 'Invoking: Keil 8051 Compiler'
	C51 "@$(patsubst %.OBJ,%.__i,$@)" || $(RC)
	@echo 'Finished building: $<'
	@echo ' '

lib/efm8sb1/cslib/device_layer/hardware_routines.OBJ: C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_hwconfig.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_config.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/low_power_config.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Lib/efm8_capsense/cslib.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/hardware_routines.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/inc/SI_EFM8SB1_Defs.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/si_toolchain.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Lib/efm8_capsense/si_toolchain_select.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdbool.h

lib/efm8sb1/cslib/device_layer/low_power_config.OBJ: C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/low_power_config.c
	@echo 'Building file: $<'
	@echo 'Invoking: Keil 8051 Compiler'
	C51 "@$(patsubst %.OBJ,%.__i,$@)" || $(RC)
	@echo 'Finished building: $<'
	@echo ' '

lib/efm8sb1/cslib/device_layer/low_power_config.OBJ: C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/si_toolchain.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_hwconfig.h C:/Users/Pedro/Google\ Drive/UNICAMP/Mestrado/Firmware/inc/config/cslib_config.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Lib/efm8_capsense/cslib.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/low_power_hardware.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/hardware_routines.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/inc/SI_EFM8SB1_Defs.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/EFM8SB1/efm8_capsense/device_layer/low_power_config.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Device/shared/si8051Base/stdbool.h C:/SiliconLabs/SimplicityStudio/v4/developer/sdks/8051/v4.1.7/Lib/efm8_capsense/si_toolchain_select.h


