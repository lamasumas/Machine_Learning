
public class Perceptron{
  
  float[] weights ;
  
  float learning_rate = 0.005;
  //Constructor
  public Perceptron(int n){
    weights = new float[n];
    //Initialize weights with randmon weights
     for( int i = 0; i<weights.length; i++)
     {
        weights[i] = random(-1,1); 
     }
  }
  
  //This is the sum step
  public int guess(float[] inputs){
    float sum = 0;
    for(int i = 0; i< weights.length ; i++)
    {
      sum += inputs[i] * weights[i];
    }
    
    int output = sign(sum);
    return output;
    
  }
  
  //Activation function
  public int sign(float n){
    if(n > 0)
      return 1;
    else
      return -1;
  }
  
  void train(float[] inputs, int target){
     int guess = guess(inputs);
     int error = target - guess;
      
     //Tune all the weights
     for (int i = 0; i< weights.length; i++)
     {
       weights[i] += error * inputs[i] * learning_rate;
     }
    
    
  }
  
  //Method used to know which line formula the percentron think it is
  float guessY(float x){
   //
   float m = -(weights [0] / weights[1]);
   float b = -(1 * weights[2] /weights[1]);
   return m*x + b;
  }
    
  
}
