#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>


class  Esp8266X{
 private:
   int state = 0;
   // wifi config
   const char* ssid = "";
   const char* password = "";
   const char* login = "";
   String command[2] = {"start","stop"};
   HTTPClient http;
   String host = "";
 public:
   Esp8266X(){
     WiFi.mode(WIFI_STA);
     WiFi.begin(ssid, password);
     while (WiFi.status() != WL_CONNECTED) {
       delay(100);
     }
     Serial.println("WiFi connected.");
  }

  bool check_mes(){
    return Serial.available();
  }
  void make_request(){
    http.begin(host+"?login="+login+"&command="+command[state]);
    int httpCode = http.GET();
    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println(httpCode);
    }
    http.end();
    if(!state){
      state= 1;
      return;
    }
    state = 0;
    }
 };


Esp8266X esp8266x;

void setup() {
  Serial.begin(9600);
}

void loop() {
 if (!(esp8266x.check_mes())){
  if (Serial.readString()=="send"){
     esp8266x.make_request();
    }
  }
}
