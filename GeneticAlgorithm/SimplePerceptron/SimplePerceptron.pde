Perceptron brain;
Point[] points = new Point[100];
int trainingIndex = 0;
void setup(){
  size(500,500);
  float[] inputs = {-1,0.5};
  for( int i = 0; i< points.length; i++){
    points[i] = new Point(); 
  }
  brain =  new Perceptron();
  int output = brain.guess(inputs);
  
}
void draw(){
  background(255);
  stroke(0);
  line(0,0,width,height);
  for( Point pt: points){
    //paint the points
     pt.show();
    float[]inputs = {pt.x,pt.y};
     int guess = brain.guess(inputs);
     if(guess == pt.label)
       fill(0,255,0);
      else
        fill(255,0,0);
      noStroke();
      ellipse(pt.x,pt.y,4,4);
  }
  
    Point trainingPoint = points[trainingIndex];
    float[]inputTraning = {trainingPoint.x,trainingPoint.y};
    brain.train(inputTraning, trainingPoint.label);
    trainingIndex++;
     if(trainingIndex == points.length)
     {
       trainingIndex =0;
     }
  
  
}

void mouseReleased(){
  
    println("Pressed");
}
