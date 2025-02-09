#include <stdio.h> 
#include "pico/stdio.h" 
const unit led_pin_red =12;
int main() {
    unit a=100;

    gpio_init(led_pin_red);
    gpio_set_dir(led_pin_red, GPIO_OUT);
    stdio_init_all();
    while (true) {
        a++;
        if (a % 2)
        printf("Blinking!\r\n");
        gpio_put(led_pin_red, 1);
        sleep_ms(a);
        gpio_put(led_pin_red, 0);
        sleep_ms(a);
    }
}