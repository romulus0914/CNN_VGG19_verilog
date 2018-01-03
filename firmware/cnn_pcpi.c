#include "firmware.h"
#define MAX_INT                 2147483647
#define DATA_LENGTH             150528
#define IMAGE_OFFSET 			0x00010000


void CNN(void)
{
    int test = hard_cnn(0, 0);

    print_str("test: ");
    print_dec(test);
    print_str("\n");
}

