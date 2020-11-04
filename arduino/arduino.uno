#include <SoftwareSerial.h>

#define button 2


SoftwareSerial esp8266(4,5);

class ProjectX{
private:
String send_ms = "send";

public:
 bool check_button(){
   const int button_state = digitalRead(button);
   return button_state;
 }

inline void serial_send(){
  esp8266.println(this->send_ms);
}

};

ProjectX prod;

void setup(){
  pinMode(4, INPUT);
  pinMode(5, OUTPUT);
  pinMode(button,INPUT_PULLUP);
  Serial.begin(115200);
  esp8266.begin(9600);
}

void loop(){
  if (prod.check_button()){
    prod.serial_send();
  }

}