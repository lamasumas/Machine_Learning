

float fLine( float x){
  // y = mx + b : line formula
  return 0.7 * x + 0.1;
}

public class Point {
  float x;
  float y;
  float bias;
  int label;
  
  public Point(){
   x = random(-1,1);
   y = random(-1,1);
   bias = 1;
   
   
   if( fLine(x) < y)
     label = 1;
   else
     label = -1;
   
  }
  
public Point(float x,  float y){
   this.x = x;
   this.y= y;
   bias = 1;
   
   if(fLine(x) < y)
     label = 1;
   else
     label = -1;
   
  }
  
  public void show() {
    
    stroke(0);
    if(label ==1)
      fill(255);
    else
      fill(0);
    
    ellipse(getX(),getY(),10,10);
  }
  
  public float getX(){
    return  map(x,-1,1,0,width);
  }
  public float getY(){
    return map(y,-1,1,height,0);
  }
  
}
