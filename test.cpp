#include "mbed.h"
#include "platform/mbed_thread.h"

#define BLINKING_RATE_MS 1000

RawSerial pc(USBTX, USBRX);

int main()
{
    pc.baud(115200);

    while (true)
    {
        pc.printf("@150#\n");
        thread_sleep_for(BLINKING_RATE_MS);
        pc.printf("@200\n");
        thread_sleep_for(BLINKING_RATE_MS);
        pc.printf("300#\n");
        thread_sleep_for(BLINKING_RATE_MS);
        pc.printf("400\n");
        thread_sleep_for(BLINKING_RATE_MS);
        pc.printf("@@500#\n");
        thread_sleep_for(BLINKING_RATE_MS);
    }
}