//Creating animations

//animations like p5 images should be stored in variables
//in order to be displayed during the draw cycle

//it's advisable (but not necessary) to load the images in the preload function
//of your sketch otherwise they may appear with a little delay


var platforms; //platforms

var character;

var isTouching;

var frames; //used to keep score

//set up the scene
function setup() {

  createCanvas(1500, 500);

  isTouching = false;
  platforms = [];
  frames = 0;

  platforms.push(new Platform(0, 500, 200));

  platforms.push(new Platform(700, randomInt(200, 400), randomInt(100, 300)));

  platforms.push(new Platform(1300, randomInt(200, 400), randomInt(100, 300)));

  character = new Mover(2, 50, 250);



}

//platform object
function Platform(x, w, h) {
  this.x = x;
  this.w = w;
  this.h = h;
  this.c = color(randomInt(0, 255), randomInt(0, 255), randomInt(0, 255)); // Define color 'c'

}


Platform.prototype.display = function() {
  stroke(0);
  strokeWeight(2);
  fill(this.c); //set a color
  rect(this.x, 500-this.h, this.w, this.h); // Draw rectangle
}

Platform.prototype.move = function() {
      //move each platform across the screen
      this.x -= 3;
}

//person/character object

function Mover(m, x, y) {
  this.mass = m;
  this.position = createVector(x, y);
  this.velocity = createVector(0, 0);
  this.acceleration = createVector(0, 0);
  this.c = color(randomInt(0, 255), randomInt(0, 255), randomInt(0, 255)); // Define color 'c'
}

// Newton's 2nd law: F = M * A
// or A = F / M
Mover.prototype.applyForce = function(force) {
  let f = p5.Vector.div(force, this.mass);
  this.acceleration.add(f);

};

Mover.prototype.update = function() {
  // Velocity changes according to acceleration
  this.velocity.add(this.acceleration);
  // position changes by velocity
  this.position.add(this.velocity);
  // We must clear acceleration each frame
  this.acceleration.mult(0);
};

//display the character
Mover.prototype.display = function() {
  stroke(0);
  strokeWeight(2);
  fill(this.c);
  ellipse(this.position.x, this.position.y, this.mass * 16, this.mass * 16);
};


//called every frame
function draw() {

  frames++;

  document.getElementById("score").innerHTML = "SCORE: " + Math.round(frames / 10);

  background(255, 255, 255);


//check collision

isTouching = false;

if(character.position.x - 16 <= platforms[0].x + platforms[0].w && character.position.x + 16 >= platforms[0].x && character.position.y - 16 <= 500 && character.position.y + 17.25 >= 500 - platforms[0].h) {
  //apply normal force
  character.applyForce(createVector(0, -0.1 * character.mass));
  character.velocity = createVector(0, 0); //make velocity 0
  isTouching = true;
}


  // Gravity is scaled by mass here!
    let gravity = createVector(0, 0.1 * character.mass);

    // Apply gravity
    character.applyForce(gravity);


    // Update and display
    character.update();
    character.display();


    //update platforms
  for(i = 0; i < platforms.length; i++) {

    platforms[i].display();
    platforms[i].move();

    //check if the platform is off the screen

    if(platforms[i].x + platforms[i].w <= 0) { //off the screen
      platforms.splice(0, 1); //remove platform
      i--;
    }
  }

  //add a new platforms

  if(platforms[platforms.length-1].x + platforms[platforms.length-1].w < 1600) { //last platform is a little ahead, and a new platform should be added

    if(Math.random() < 0.2) { //randomness factor
      platforms.push(new Platform(1800, randomInt(300, 700), randomInt(50, 300)));
    }
  }

  //check game Mover

//too low

if(character.position.y + 17 > 500) {
  reset();
}

//hit the edge of the platform

if(isTouching && character.position.y > 500 - platforms[0].h) {
  reset();
}


}


function reset() {

  platforms = [];

  platforms.push(new Platform(0, 500, 200));

  platforms.push(new Platform(700, randomInt(200, 400), randomInt(100, 300)));

  platforms.push(new Platform(1300, randomInt(200, 400), randomInt(100, 300)));


  character = new Mover(2, 50, 250);

  isTouching = false;

  frames = 0;

  background(255, 255, 255);

}

//key press event handler
function keyPressed() {
  if (keyCode === 32 && isTouching) {
    character.applyForce(createVector(0, -12));
  }
  return false; // prevent default
}

function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}
