#include <Servo.h> 

Servo m1;
Servo m2;

int incomingByte;

const int r1 = 3;
const int r2 = 2;

int reverse1 = 0;
int reverse2 = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(r1, OUTPUT);
  pinMode(r2, OUTPUT);
  m1.attach(9);
  m2.attach(10);
  m1.write(36);
  m2.write(36);
 
}

void loop()
{
  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();
    while(incomingByte == 'a')
    { 
      incomingByte = Serial.read();  
      m2.write(36);
      break;
    }
    while(incomingByte == 'b')
    {   
        incomingByte = Serial.read(); 
        m2.write(46);
        break;  
    }
    while(incomingByte == 'c')
    {   
        incomingByte = Serial.read(); 
        m2.write(56);
        break;  
    }
    while(incomingByte == 'd')
    {   
        incomingByte = Serial.read(); 
        m2.write(66);
        break;  
    }
    while(incomingByte == 'e')
    {   
        incomingByte = Serial.read(); 
        m2.write(76);
        break;  
    }
    while(incomingByte == 'f')
    {   
        incomingByte = Serial.read(); 
        m2.write(86);
        break;  
    }
    while(incomingByte == 'g')
    {   
        incomingByte = Serial.read(); 
        m2.write(96);
        break;  
    }
    while(incomingByte == 'h')
    {   
        incomingByte = Serial.read(); 
        m2.write(106);
        break;  
    }
    
    
    
    while(incomingByte == 'A')
    { 
      incomingByte = Serial.read();  
      m1.write(36);
      break;
    }
    while(incomingByte == 'B')
    {   
        incomingByte = Serial.read(); 
        m1.write(46);
        break;  
    }
    while(incomingByte == 'C')
    {   
        incomingByte = Serial.read(); 
        m1.write(56);
        break;  
    }
    while(incomingByte == 'D')
    {   
        incomingByte = Serial.read(); 
        m1.write(66);
        break;  
    }
    while(incomingByte == 'E')
    {   
        incomingByte = Serial.read(); 
        m1.write(76);
        break;  
    }
    while(incomingByte == 'F')
    {   
        incomingByte = Serial.read(); 
        m1.write(86);
        break;  
    }
    while(incomingByte == 'G')
    {   
        incomingByte = Serial.read(); 
        m1.write(96);
        break;  
    }
    while(incomingByte == 'H')
    {   
        incomingByte = Serial.read(); 
        m1.write(106);
        break;  
    }
    
    //relay 1 wordt ingeschakeld
    while(incomingByte == '3' && reverse1 == 0)
    {
       incomingByte = Serial.read();
       digitalWrite(r1, HIGH);
       reverse1 = 1;
       break;
    }
    //relay 1 wordt uitgeschakeld
    while(incomingByte == '4' && reverse1 == 1)
    {
        incomingByte = Serial.read();
        digitalWrite(r1, LOW);
        reverse1 = 0;
        break;
    }
    //relay 2 wordt ingeschakeld
    while(incomingByte == '7' && reverse2 == 0)
    {
        incomingByte = Serial.read();
        digitalWrite(r2, HIGH);
        reverse2 = 1;
        break;
    }
    //relay 2 wordt uitgeschakeld
    while(incomingByte == '8' && reverse2 == 1)
    {
        incomingByte = Serial.read();
        digitalWrite(r2, LOW);
        reverse2 = 0;
        break;
    }
  }
}
