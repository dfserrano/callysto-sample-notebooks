//COMMENTS
//Comments are used to add in text that you do not want your program to run.
//Commenting can be used in order to make your program ignore lines of code you have already written. 
//To start a comment either use "//" or "/*". In order to end a comment with "/*", add in a "*/" at the end of the comment.


//VARIABLES
//Variables are names for different types of data that you can use in your code.
//INTEGERS
int potato;

int carrot = 7;
//BAD VERY BAD - INTEGERS CANNOT HAVE DECIMALS
//int onion = 7.5;

//EXAMPLE
int l = 100;
int h = 100;

//Variables are used to change things. They are used to store values. 
//BOOLEANS
boolean isMale = false;

//STRINGS
String myString = "apple";
String name = "Krystal";

//FLOATS
float myFloat = 2.5;

//DOUBLES
double myDouble = 2000000000.75;




//METHODS
//Methods are just a way to call upon a chunk of code.
//sort -->> 100 lines of code.
//100 lines every time, methods allow you to call one line of code, sort, in order to activate all those 100 lines of code without having to retype it all.
void setup(){
  size(1000,1000);
  background(0);
  carrot += 1;
}

void draw(){

  rect(0, l, 20, h);
  
}

void sort(){
  
}