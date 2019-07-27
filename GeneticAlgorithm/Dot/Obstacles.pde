

class Obstacle{
  private PVector pos; 
  private int theWidth;
  private int theHeight;
  
  public Obstacle(int x, int y, int theWidth, int theHeight, ArrayList<Obstacle> obstacles){
    pos = new PVector(x,y);
    this.theWidth = theWidth;
    this.theHeight = theHeight;
    obstacles.add(this);
    
  }
  
  
  void show(){
    fill(0, 0, 255);
    rect(pos.x, pos.y, theWidth, theHeight); 
  }
  
}
