Perceptron brain;
Point[] points = new Point[100];
int trainingIndex = 0;

void setup(){
  size(500,500);
  float[] inputs = {-1,0.5};
  for( int i = 0; i< points.length; i++){
    points[i] = new Point(); 
  }
  brain =  new Perceptron(3);
  
}

void draw(){
  background(255);
  stroke(0);
  
  //line(0,height,width,0);
  Point p1 = new Point(-1, fLine(-1));
  Point p2 = new Point(1, fLine(1));
  line(p1.getX(), p1.getY(),p2.getX(), p2.getY());
  
  Point p3 = new Point(-1, brain.guessY(-1));
  Point p4 = new Point(1, brain.guessY(1));
  line(p3.getX(), p3.getY(),p4.getX(), p4.getY());
  
  for( Point pt: points){
    //paint the points
     pt.show();
    float[]inputs = {pt.x,pt.y,1 };
     int guess = brain.guess(inputs);
     if(guess == pt.label)
       fill(0,255,0);
      else
        fill(255,0,0);
      noStroke();
      ellipse(pt.getX(),pt.getY(),4,4);
  }
  
    Point trainingPoint = points[trainingIndex];
    float[]inputTraning = {trainingPoint.x,trainingPoint.y,1};
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
