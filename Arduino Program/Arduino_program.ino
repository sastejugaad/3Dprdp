
//int IN1 = 3; 
//int IN2 = 6; 
//int IN3 = 4;
//int IN4 = 5;


int IN1 = 3; 
int IN2 = 6; 
int IN3 = 4;
int IN4 = 5;

int IN5 = 7; 
int IN6 = 8; 
int IN7 = 9;
int IN8 = 10;

int Speed=130;

//char InData=' ';
void setup()
{

  Serial.begin(9600);
  //back motors 
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
 //front motors
  pinMode(IN5, OUTPUT);
  pinMode(IN6, OUTPUT);
  pinMode(IN7,OUTPUT);
  pinMode(IN8, OUTPUT);


  //Serial.print("intialize");
}

void loop() {

char InData=Serial.read();

if(InData=='f')
{
 Forward(Speed,0); 
 Serial.print("forward");
}
if(InData=='b')
{
 Back(Speed,0); 
 //Serial.print("back");
}
if(InData=='l')
{
 Left(Speed,0); 
 Serial.print("left");
}
if(InData=='r')
{
 Right(Speed,0); 
 //Serial.print("right");
}

if(InData=='c')
{
 Stop(); 
 //Serial.print("stop");
}

}

void Forward(int speedA,int speedB)
{ 
  //back
  analogWrite(IN1, speedA);
  analogWrite(IN2, speedB);  
  analogWrite(IN3, speedA);
  analogWrite(IN4, speedB);  
  //front
  analogWrite(IN5, speedA);
  analogWrite(IN6, speedB);  
  analogWrite(IN7, speedB);
  analogWrite(IN8, speedA);


}
void Back(int speedA,int speedB)
{ 
  //back
  analogWrite(IN1, speedB);
  analogWrite(IN2, speedA);  
  analogWrite(IN3, speedB);
  analogWrite(IN4, speedA);  
  //front
  analogWrite(IN5, speedB);
  analogWrite(IN6, speedA);  
  analogWrite(IN7, speedA);
  analogWrite(IN8, speedB);
}

void Left(int speedA,int speedB)
{ 
  //back
  analogWrite(IN1, speedA);
  analogWrite(IN2, speedB);  
  analogWrite(IN3, speedB);
  analogWrite(IN4, speedA);  
  //front
  analogWrite(IN5, speedA);
  analogWrite(IN6, speedB);  
  analogWrite(IN7, speedA);
  analogWrite(IN8, speedB);
}
void Right(int speedA,int speedB)
{
  //back
  analogWrite(IN1, speedB);
  analogWrite(IN2, speedA);  
  analogWrite(IN3, speedA);
  analogWrite(IN4, speedB);  
  //front
  analogWrite(IN5, speedB);
  analogWrite(IN6, speedA);  
  analogWrite(IN7, speedB);
  analogWrite(IN8, speedA);
}

void Stop()
{ 
  //back
  analogWrite(IN1, 0); 
  analogWrite(IN2, 0); 
  analogWrite(IN3, 0); 
  analogWrite(IN4, 0);
  //front
  analogWrite(IN5, 0);
  analogWrite(IN6, 0);  
  analogWrite(IN7, 0);
  analogWrite(IN8, 0);

  
}