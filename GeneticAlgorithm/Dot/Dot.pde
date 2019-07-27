
class Dott {
  PVector pos;
  PVector vel;
  PVector acc;
  boolean dead;
  Brain  brain;
  float fitness =0;
  boolean reachedGoal;
  boolean isBest;

  Dott() {
    isBest = false;

    dead = false;
    reachedGoal=false;
    pos = new  PVector(width/2, height-10);
    vel = new PVector(0, 0);
    acc = new PVector(0, 0); 
    brain = new Brain(400);
  }


  //----------------------------------------------------------
  void show() {
    if (isBest) {
      fill(0, 255, 0);
      ellipse(pos.x, pos.y, 8, 8);
    } else {
      fill(0);
      ellipse(pos.x, pos.y, 4, 4);
    }
  }



  //----------------------------------------------------------
  /*
    Move the dot folling the directions
   */
  void move() {
    if (brain.directions.length > brain.step) {
      acc = brain.directions[brain.step];
      brain.step++;
    } else {
      dead= true;
    }

    vel.add(acc);
    vel.limit(5);
    pos.add(vel);
  }


  //----------------------------------------------------------
  /*
    Set the dot to dead or to a dot "alpha" if it reach the goal (More fitness points)
   */
  void update() {
    if (!dead && !reachedGoal) {
      move();
      if (pos.x<2 || pos.y<2 || pos.x> width-2 || pos.y> height-2)
        dead = true;
      else if (dist(pos.x, pos.y, goal.x, goal.y) < 5 )
        reachedGoal=true;
      
      for(Obstacle x: obstacles){
         if ( pos.x > x.pos.x && pos.y >x.pos.y && pos.x<(x.pos.x+ x.theWidth) && 
        pos.y< (x.pos.y + x.theHeight)){
        
        dead= true;
        break;
        }
        
        
      }
     
    }
  }



  //----------------------------------------------------------

  /**
   This will give more or less "points"  to the dots depending on how close is the dot to the goal
   */
  void calculateFitnessFunction() {
    if (reachedGoal) {
      fitness = 1/16 +100000.0/(brain.step * brain.step);
    } else {
      float distanceGoal = dist(pos.x, pos.y, goal.x, goal.y);
      fitness = 1/(distanceGoal * distanceGoal);
    }
  }

  //----------------------------------------------------------

  /**
   Copy the brain of each dote (the movements)
   */
  Dott birthOfBaby() {
    //this is for having a fake crossover
    // Real crossover is having two parents and mix the gens
    Dott baby = new Dott();
    baby.brain = brain.clone();
    return baby;
  }
}
