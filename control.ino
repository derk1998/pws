//Deze code is gemaakt door: Derk Wiegerinck

#include <Servo.h>

Servo m1;
Servo m2;

int incomingByte; 
const int r1 = 2;
const int r2 = 13;

int reverse1 = 0;
int reverse2 = 0;

void setup()
{
  Serial.begin(9600);
  m1.attach(9); //motor 1 op pin 9
  m2.attach(10); //motor 2 op pin 10 
  pinMode(r1, OUTPUT);
  pinMode(r2, OUTPUT);
  m1.write(0);
  m2.write(0);
}
  
  void loop()
  {
  //zoeken naar seriële data
  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();
    
    //joystick 1
    while(incomingByte == 'a')
    {   
        incomingByte = Serial.read(); 
        m1.write(0);
        break;  
    }
    while(incomingByte == 'b')
    {      
        incomingByte = Serial.read(); 
        m1.write(20);
        break;  
    }
    while(incomingByte == 'c')
    {   
        incomingByte = Serial.read(); 
        m1.write(40);
        break;  
    }
    while(incomingByte == 'd')
    {   
        incomingByte = Serial.read(); 
        m1.write(60);
        break;  
    }
    while(incomingByte == 'e')
    {   
        incomingByte = Serial.read(); 
        m1.write(80);
        break;  
    }
    while(incomingByte == 'f')
    {   
        incomingByte = Serial.read(); 
        m1.write(100);
        break;  
    } 
     while(incomingByte == 'g')
    {   
        incomingByte = Serial.read(); 
        m1.write(120);
        break;  
    }
     while(incomingByte == 'h')
    {   
        incomingByte = Serial.read(); 
        m1.write(140);
        break;  
    }
     while(incomingByte == 'i')
    {   
        incomingByte = Serial.read(); 
        m1.write(160);
        break;  
    }
     while(incomingByte == 'j')
    {   
        incomingByte = Serial.read(); 
        m1.write(180);
        break;  
    }
     //vooruit joystick 2
     while(incomingByte == 'k')
    {   
        incomingByte = Serial.read(); 
        m2.write(0);
        break;  
    }
    while(incomingByte == 'l')
    {   
        incomingByte = Serial.read(); 
       m2.write(20);
        break;  
    }
    while(incomingByte == 'm')
    {   
        incomingByte = Serial.read(); 
        m2.write(40);
        break;  
    }
    while(incomingByte == 'n')
    {   
        incomingByte = Serial.read(); 
        m2.write(60);
        break;  
    }
    while(incomingByte == 'o')
    {   
        incomingByte = Serial.read(); 
        m2.write(80);
        break;  
    }
    while(incomingByte == 'p')
    {   
        incomingByte = Serial.read(); 
        m2.write(100);
        break;  
    } 
    while(incomingByte == 'q')
    {   
        incomingByte = Serial.read(); 
        m2.write(120);
        break;  
    }
    while(incomingByte == 'r')
    {   
        incomingByte = Serial.read(); 
        m2.write(140);
        break;  
    }
    while(incomingByte == 's')
    {   
        incomingByte = Serial.read(); 
        m2.write(160);
        break;  
    }
    while(incomingByte == 't')
    {   
        incomingByte = Serial.read(); 
        m2.write(180);
        break;  
    } 
    
    //relay 1 wordt ingeschakeld
    while(incomingByte == '9' && reverse1 == 0)
    {
       incomingByte = Serial.read();
       digitalWrite(r1, HIGH);
       reverse1 = 1;
       break;
    }
    
    //relay 2 wordt ingeschakeld
    while(incomingByte == '8' && reverse2 == 0)
    {
        incomingByte = Serial.read();
        digitalWrite(r2, HIGH);
        reverse2 = 1;
        break;
    }
  
    //relay 1 wordt uitgeschakeld
    while(incomingByte == '6' && reverse1 == 1)
    {
        incomingByte = Serial.read();
        digitalWrite(r1, LOW);
        reverse1 = 0;
        break;
    }
 
    //relay 2 wordt uitgeschakeld
    while(incomingByte == '7' && reverse2 == 1)
    {
        incomingByte = Serial.read();
        digitalWrite(r2, LOW);
        reverse2 = 0;
        break;
    }   
  }
}
