
class Brain {

  PVector[] directions;
  int step = 0;

  Brain(int size) {
    directions = new PVector[size];
    randomize();
  }
  //----------------------------------------------------------
  /**
  Create random directions for the dot movement
  **/
  void randomize() {
    for (int i = 0; i<directions.length; i++)
    {
      float randomAngle = random(2*PI);
      directions[i] = PVector.fromAngle(randomAngle);
    }
  }
  //----------------------------------------------------------
  /**
    Copy the direction of the dot
  **/
  Brain clone() {
    Brain clone = new Brain(directions.length);
    for (int i = 0; i<directions.length; i++)
    {
      clone.directions[i] = directions[i].copy();
    }
    return clone;
  }

  //----------------------------------------------------------
  
  /**
    Modify the directions randomly only a few of them (statistically 1 out of 100, as the mutation rate is 0.01)
  **/
  void mutate() {
    float mutationRate = 0.01;
    for (int i= 0; i<directions.length; i++)
    {
      float rand = random(1);
      if (rand < mutationRate) {
        float randomAngle = random(2*PI);
        directions[i] = PVector.fromAngle(randomAngle);
      }
    }
  }
}
