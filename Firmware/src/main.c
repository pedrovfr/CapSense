
//-----------------------------------------------------------------------------
// Includes
//-----------------------------------------------------------------------------
#include <SI_EFM8SB1_Register_Enums.h>                  // SFR declarations
#include "InitDevice.h"
// $[Generated Includes]
#include "cslib_config.h"
#include "cslib.h"
#include "cslib_hwconfig.h"
#include "profiler_interface.h"
#include "comm_routines.h"

SI_SBIT (LED0, SFR_P0, 0);          // '1' means ON, '0' means OFF//
//SI_SBIT (BC_ENABLE, SFR_P0, 0);
SI_SBIT (LED1, SFR_P0, 1);

uint8_t sensor_index;
uint16_t sensor_data;
uint16_t baseline[6];
uint16_t filtered_data;
SI_UU32_t expVal;
uint8_t byte = 0;
uint8_t serial_flag = 0;

//-----------------------------------------------------------------------------
// main() Routine
// ----------------------------------------------------------------------------
int main (void){
	//	BC_ENABLE = 0;
	// Call hardware initialization routine
	enter_DefaultMode_from_RESET();
	P0 |= 0x01;
	P0 &= 0xFE;
	P2MDOUT |= 0x80;
	P2 &= ~0x80;
	TCON_TF0 = 0;

	// Initializes the UART interface
	CSLIB_commInit();

	// Configures all peripherals controlled by capsense, including
	// the sensing block and port pins
	CSLIB_initHardware();

	// Initializes the capsense variables and performs some scans to
	// initialize the baselines
	CSLIB_initLibrary();
	serial_flag = 0;
	SCON0_RI = 0;
	while (1){
		LED1 = 0;
		// -----------------------------------------------------------------------------
		// Performs all scanning and data structure updates
		// -----------------------------------------------------------------------------
		CSLIB_update();
 		// -----------------------------------------------------------------------------
		// If low power features are enabled, this will either put the device into a low
		// power state until it is time to take another scan, or put the device into a
		// low-power sleep mode if no touches are active
		// -----------------------------------------------------------------------------
		//CSLIB_lowPowerUpdate();
		if(SCON0_RI){
			if(SBUF0 == 'a'){
				printHeader();
				//LED0 = 1;
			}
			CSLIB_commUpdate();
			LED0 = 1;
			serial_flag = 0;
			SCON0_RI = 0;
		}
		else{
			LED0 = 0;
		}
   }                             
}


