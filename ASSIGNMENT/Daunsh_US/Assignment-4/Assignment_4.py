#define trigPin 8
#define echoPin 9
#define buzzer 10
long duration;
float distanceInch;
int timer; 
void setup() {
pinMode(trigPin, OUTPUT); 
pinMode(echoPin, INPUT); 
pinMode(buzzer, OUTPUT); 
}
void loop() {
digitalWrite(trigPin, LOW); 
delayMicroseconds(2); 
digitalWrite(trigPin, HIGH); 
delayMicroseconds(10); 
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH); 
distanceInch = duration * 0.0133 /2; 
digitalWrite(buzzer, HIGH); 
delay(50); 
digitalWrite(buzzer, LOW); 
timer = distanceInch * 10; 
delay(timer); 
}