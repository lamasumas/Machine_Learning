
public class Perceptron{
  
  float[] weight = new float[2];
  float learning_rate = 0.01;
  //Constructor
  public Perceptron(){
    //Initialize weights with randmon weights
     for( int i = 0; i<weight.length; i++)
     {
        weight[i] = random(-1,1); 
     }
  }
  
  //This is the sum step
  public int guess(float[] inputs){
    float sum = 0;
    for(int i = 0; i< weight.length ; i++)
    {
      sum += inputs[i] * weight[i];
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
     for (int i = 0; i< weight.length; i++)
     {
       weight[i] += error * inputs[i] * learning_rate;
     }
    
    
  }
    
  
}
