let image;

function setup() { //set up function, called when the page is loaded
  createCanvas(1500, 1000);
}


function draw() { //called every frame
  if (mouseIsPressed) { //if the mouse is pressed, the circle will be blac
    fill(0);
  } else { //circle is random color
    fill(color(randomInteger(0, 255), randomInteger(0, 255), randomInteger(0, 255))); //random rgb color
  }
  ellipse(mouseX, mouseY, 80, 80); //create circle
}


function randomInteger(min, max) { //returns a random integer from min to max, inclusive of both
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}
