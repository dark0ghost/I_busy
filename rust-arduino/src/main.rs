#[warn(unused_imports)]
use arduino::{
    PORTB, DDRB
}; // Register
use arduino::PORTB7;
use arduino::prelude::without_interrupts;
use std::ptr::write_volatile; // Pin

fn main() {
    without_interrupts(|| { //Disable interrupts.
        unsafe {
            write_volatile(DDRB, 0xFF)
        }
    });
    println!("Hello, world!");
}
