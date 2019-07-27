Population test;
PVector goal = new PVector(400, 10);
ArrayList<Obstacle> obstacles;
void settings()
{
  size(800, 800);
}
void setup()
{  
  
  test = new Population(800);
  obstacles = new ArrayList();
  new Obstacle(0, 200, 400, 30, obstacles);    
  new Obstacle(width/5, height/2, 500, 10, obstacles);
  new Obstacle(width-200, height-300, 300, 30, obstacles);
}


void draw() {
  background(255);
  fill(255, 0, 0);
  ellipse(goal.x, goal.y, 10, 10);
  fill(255,0 ,255);
  text("Generation: " + test.gen,100,100);

  for(Obstacle x : obstacles)
    x.show();

  
 


  if ( test.allDotsDead()) {
     //Call the evolution 
    test.calculateFitness();
    test.naturalSelection();
    test.mutateTheBabies();
  } else {
    
    //Continue the game
    test.update();
    test.show();
  }
}
