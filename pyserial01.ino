String InByte;
int saida = A1;
int entrada = A7;
int i = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
  pinMode(LED_BUILTIN, OUTPUT);




}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    InByte = Serial.readStringUntil('\n'); //python manda um um "pula
    //linha" depois de cada
    //comando.
    if (InByte == "are you there?") {
      Serial.write("YES! Lt.Arduino,reporting for duty!");
      Serial.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce a mattis velit, in lacinia lectus."
                   "Cras consectetur sed felis eget venenatis. Vestibulum facilisis lorem vel commodo semper. In ornare, orci eu"
                   "vehicula finibus,dui risus cursus dui, ac accumsan mauris ligula nec magna. Suspendisse potenti. Etiam scelerisque"
                   "diam id libero congue sagittis. In hac habitasse platea dictumst.");
    }
    else {
      Serial.write("OOOPS");
    }



  }
}
