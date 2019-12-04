
/*

IF YOU DON'T UNDERSTAND WHAT'S GOING ON:

1.) the goal is to train a machine learning model that can classify two different images, one that is called the 'blue' image and the other that is the 'red' image
2.) you choose what image is the 'blue' image (ex you raising your right hand) and the 'red' image (ex you raising your left hand)
3.) once you collect as many images as you can (the more images means a better model), the model is trained. this means that a bunch of math happens to alter the model
so that it can tell the difference between the blue and red image
4.) finally, the model can predict the blue or red image

vocab

- loss - tells you how well the model is doing; you want this as low as possible
- model - think of it as a highly complex mathematical model
- features - sample red and blue images that you train the model with

*/

// Declare Variables
var featureExtractor, classifier, video, loss, redCount, blueCount, yellowCount, greenCount;

// `red` and `blue` are where we're storing the count of how many images we have for each.
redCount = blueCount = yellowCount = greenCount = 0;



function setup() {
	// Tells p5 to not automatically create a canvas element.
  noCanvas();

	// Starts capturing a video feed from the webcam
  video = createCapture(VIDEO);

	// Puts the video stream into the div in our html, with ID `video`
  video.parent('video');

	// Initializes a feature extractor, yet to be trained - from ml5
  featureExtractor = ml5.featureExtractor('MobileNet');
  featureExtractor.numLabels = 4;
  classifier = featureExtractor.classification(video, { numLabels: 4 });


	// Go to line 27
  setupButtons();
}

// A function to add event listeners to buttons
function setupButtons() {

  buttonA = select('#red');
	buttonB = select('#blue');
  buttonC = select('#green');
  buttonD = select("#yellow");


  buttonA.mousePressed(function() {
		redCount++;
    classifier.addImage('red');
    select('#redCount').html(redCount);
  });


  buttonB.mousePressed(function() {
		blueCount++;
    classifier.addImage('blue');
    select('#blueCount').html(blueCount);
  });

  buttonC.mousePressed(function() {
		greenCount++;
    classifier.addImage('green');
    select('#greenCount').html(greenCount);
  });

  buttonD.mousePressed(function() {
		yellowCount++;
    classifier.addImage('yellow');
    select('#yellowCount').html(yellowCount);
  });

  train = select('#train');
  train.mousePressed(function() {
    classifier.train(function(lossValue) {

			// This is where we're actually training our model

      if (lossValue) {
        loss = lossValue;
        select('#info').html('Loss: ' + loss);
      } else {
        select('#info').html('Done Training! Final Loss: ' + loss);
				select('#train').style("display", "none");
				select('#predict').style("display", "inline");
      }
    });
  });

  // Predict Button
  buttonPredict = select('#predict');
  buttonPredict.mousePressed(classify);
}

// Classify the current frame.
function classify() {
  classifier.classify(gotResults);
}

// Show the results
function gotResults(err, result) {
  if (err) {
    console.log(err);
  }

  var answer = Math.max(result[0].confidence, result[1].confidence, result[2].confidence, result[3].confidence);
  if(answer == result[0].confidence){
	  select("body").style("background", result[0].label);
  }
  else if (answer == result[1].confidence){
	  select("body").style("background", result[1].label);
  } else if(answer == result[2].confidence) {
	  select("body").style("background", result[2].label);
  } else if(answer == result[3].confidence) {
    	  select("body").style("background", result[3].label);

  }
  classify();
}
