void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int i;
    int DN[8];
    char buffer[100];
    
    // Read digital number from sensors
    for(i=0;i<8;i++)
    {
        DN[i] = analogRead(i);
    }
    
    // Print data to the serial port
    sprintf(buffer, "%5d, %5d, %5d, %5d, %5d, %5d, %5d, %5d",  DN[0], DN[1], DN[2], DN[3], DN[4], DN[5], DN[6], DN[7]);
    Serial.println(buffer);
}
