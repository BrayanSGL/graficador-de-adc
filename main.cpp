#include "mbed.h"
#include "platform/mbed_thread.h"

#define measurementTime 50

RawSerial pc(USBTX, USBRX);
DigitalOut green(D7);
DigitalOut red(D6);
AnalogIn pot(A5);

float value = 0;

void dataReceived();

int main()
{
    pc.attach(&dataReceived);
    pc.baud(115200);

    while (true)
    {
        value = ((pot.read_u16()) / (65535 / 500)) - 250;
        pc.printf("@%.0f#\n", value);
        thread_sleep_for(measurementTime);
    }
}

void dataReceived()
{
    int received = pc.getc();
    switch (received)
    {
    case 'a':
        red = 1;
        break;
    case 'b':
        green = 1;
        ;
        break;
    case 'c':
        green = 0;
        red = 0;
        break;
    default:
        pc.printf("Comando no reconocido");
        break;
    }
}