
public class Point {
  float x;
  float y;
  int label;
  
  public Point(){
   x = random(width);
   y = random(height);
   
   if(x > y)
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
      
    ellipse(x,y,8,8);
  }
  
}
