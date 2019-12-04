//random orientation for every HTML element
​
Array.prototype.slice.call(
  document.querySelectorAll(
    'div,p,span,img,a,body')).map(function(tag){
	tag.style['transform'] = 'rotate(' + (
    Math.floor(Math.random() * 3) - 1) + 'deg)';
});
​
​
//hacker colors
​
var allDivs = document.querySelectorAll('div');
​
for(var i = 0; i < allDivs.length; i++){
  // allDivs[i].style['background-color'] = 'black';
  allDivs[i].style['color'] = 'green';
  allDivs[i].style['font-family'] = 'Monospace';
}
​
​
//rotates 180 degrees
​
setTimeout(function(){
 document.onmousemove = document.onkeypress =
 function(){
     document.body.style['transition'] = 'transform 3s';
     document.body.style['transform'] = 'rotate(180deg)';
 }
}, 5000);
​
//make every word "hack"
​
Array.prototype.slice.call(
  document.querySelectorAll(
    'p,h1,h2,h3,h4,h5')).map(function(tag){
	tag.innerHTML = "hacked";
});
​
​
//change all images to have a picture of the cougar
​
Array.prototype.slice.call(
  document.querySelectorAll('img')).map(function(tag){
    tag.src = 'https://adc.d211.org/cms/lib/IL49000007/Centricity/Domain/177/chs-cougar-mascot.png';
});
