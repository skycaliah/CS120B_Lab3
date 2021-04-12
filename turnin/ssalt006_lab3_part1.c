/*	Author: Skyler Saltos 
 *  Partner(s) Name: 
 *	Lab Section:22
 *	Assignment: Lab #3  Exercise #1
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
	//inputs A & B
	DDRA = 0x00;
	DDRB = 0x00;
	PORTA = 0xFF;
	PORTB = 0xFF;

	//outputs C
	DDRC = 0xFF;
	PORTC = 0x00;
	
    /* Insert your solution below */


	unsigned char i;
	unsigned char j;
	unsigned char count;
	unsigned char currBit;


    while (1) {
	
	    count = 0;
	    for(i=0;i<8;++i){
		currBit = ( PINA >> i ) & 0x01;
		count = count + currBit;

	    }//first for loop to iterate through A inputs 
	    	

	

	    for(j=0;j<8;++j){

		currBit = (PINB >> j) & 0x01;
		count = count + currBit;

	    }//end for loop to iterate throug B inputs 



	    PORTC = count;
    }
    return 1;
}
