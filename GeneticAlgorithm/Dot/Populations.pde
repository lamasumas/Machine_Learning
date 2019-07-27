class Population {
  Dott[] dots;
  int gen;
  float fitnessSum;
  int bestDot = 0; 
  int minSteps = 400;

  Population(int size) {
    gen = 1;
    dots = new Dott[size]; 
    for (int i = 0; i< dots.length; i++)
      dots[i] = new Dott();
  }

  //----------------------------------------------------------
  void show() {
    for (int i = 1; i< dots.length; i++)
      dots[i].show();
    //Show the best Dot "Beta" (The one with the biggest amount of fitness points)
    dots[0].show();
  }


  //----------------------------------------------------------
  void update() {
    for (int i = 0; i< dots.length; i++)
      if (dots[i].brain.step > minSteps)
        dots[i].dead = true;
      else
        dots[i].update();
  }

  //----------------------------------------------------------

  void calculateFitness() {   
    for (int i = 0; i< dots.length; i++)
      dots[i].calculateFitnessFunction();
  }


  //----------------------------------------------------------

  boolean allDotsDead() {
    for (int i = 0; i< dots.length; i++) {
      if (!dots[i].dead && !dots[i].reachedGoal)
        return false;
    }
    return true;
  }


  //----------------------------------------------------------

  void naturalSelection() {
    Dott[] newDots = new Dott[dots.length]; 
    //Select the best dot, so the generation dont go stupid again
    setBestDot();
    calculateFitnessSum();
    //Put the best dot baby in the new genereation
    newDots[0] = dots[bestDot].birthOfBaby();
    newDots[0].isBest= true;
    for ( int i = 1; i<newDots.length; i++)
    {

      //Select parent based on fitness
      Dott parent = selectParent();

      //get babys
      newDots[i] = parent.birthOfBaby();
    }
    dots = newDots.clone();
    gen++;
  }

  //----------------------------------------------------------
  void calculateFitnessSum() {
    fitnessSum= 0;
    for (int i = 0; i< dots.length; i++) {
      fitnessSum+= dots[i].fitness;
    }
  }


  Dott selectParent() {
    float rand = random(fitnessSum);

    float runningSum = 0; 

    for (int i = 0; i< dots.length; i++) {
      runningSum += dots[i].fitness;
      //Chose the first parent who pass the random( between 0 and the total sum of fitness points ) stupidness minimum level, 
      //This is called "Fitness proportional selection" in which the dots with biggest ammount of fitness point has more probability of being selected
      if (runningSum > rand) {
        return dots[i];
      }
    }
    //Should never get to this point
    return null;
  }


  //Create a new generation based on the last one 
  void mutateTheBabies() {
    for (int i = 1; i< dots.length; i++) {
      dots[i].brain.mutate();
    }
  }

  //Select the dot with the best fitness, to insert it into the next generation
  //Also, safe the ammount of steps, if that dots arrive to the goal point.
  void setBestDot() {
    float max = 0;
    int maxIndex = 0;
    for (int i = 0; i < dots.length; i++) {
      if (dots[i].fitness> max) {
        max = dots[i].fitness;
        maxIndex = i;
      }
    }
    bestDot  = maxIndex;
    if (dots[bestDot].reachedGoal)
      minSteps= dots[bestDot].brain.step;
  }
}
