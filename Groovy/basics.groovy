// https://www.youtube.com/watch?v=B98jc8hdu9g
// Like java, the class name must match the file name
class basics {
  static void main(String[] args) {
    println("Hello World");

    // define a variable
    def age = "Dog";
    age = 40;
 
    // basic math int operations
    println("5 + 4 = " + (5 + 4));
    // -, *, %, .intdiv (e.g. 5.intdiv(4))

    // floating point operations
    println("5.2 + 4.4 = " + (5.2.plus(4.4)));
    // .minus, .multiply, /

    // increment, decrement
    println("age++ = " + (age++));
    // this prints age as is, then age = age + 1
    // ++age: age = age + 1, then prints age
    println("age-- = " + (age--));
    // --age

    // In groovy, the biggest interger value is Interger.MAX_VALUE
    // similarly, Integer.MIN_VALUE, Float.MAX_VALUE
    // Float.MIN_VALUE, Double.MAX_VALUE, Double.MIN_VALUE
    println("Integer.MAX_VAlUE = " + Integer.MAX_VALUE);

    def randNum = 2.0;
    println("Math.abs(-2.45) = " + (Math.abs(-2.45)));
    // Math.round(), randNum.pow(3), 3.0.equals(2.0) 
    // randNum.equals(Float.NaN), Math.sqrt(9), Math.cbrt(27)
    // Math.ceil(2.45), Math.floor(2.45), Math.min(2, 3)
    // Math.max(2, 3), Math.log(2), Math.log10(2)
    // Math.toDegrees(Math.PI), Math.toRadians(90)
    // Math.sin(0.5 * Math.PI)
    // cos, tan, asin, acos, atan, sinh ...

    // random number between 1 and 100
    println("Math.abs(new Random().nextInt() % 100) + 1 = " + (Math.abs(new Random().nextInt() % 100) + 1));

    // string
    def name = "Derek";
    // '' literally
    println('I am ${name}\n');
    // ${name} or $name is expanded in ""
    println("I am ${name}\n");
    // multi-line string
    def multiString = '''I am
    a string that goes on 
    for many lines''';
    println("multiString = " + multiString);

    println("4th character of Name " + name[3]);
    println("Index of r " + name.indexOf('r'));

    println("first 3 characters " + name[0..2]);
    println("every other characters " + name[0,2,4]);
    println("substring starting 1 " + name.substring(1));
    println("substring at 1 to 4 " + name.substring(1,4));
    println("My name is " + name);
    println("My name is ".concat(name));
    // repeat twice
    println("What I said is " * 2);
    // equality check
    println("Derek == Derek " + ("Derek".equals("Derek")));
    println("Derek == derek " + ("Derek".equalsIgnoreCase("derek")));

    // string length
    println("length " + name.length());

    def repeatStr = "What I said is " * 2;
    // remove the leading "What"
    println(repeatStr - "What");
    // split by space, return [What, I, said, is,...]
    println(repeatStr.split(' '));
    // split by each character, returns [W, h, a, t,  , I,  , s, ...]
    println(repeatStr.toList());

    // replace "I" with "she"
    println(repeatStr.replaceAll('I', 'she'));

    // upper case and lower case
    println("name upper case " + name.toUpperCase());
    println("name lower case" + name.toLowerCase());

    // string comparison
    // alphabetic order, return 0 if equal; -1 if "ant" < "banana"; 1 if "ant" > "banana"
    println("ant <=> banana" + 'ant' <=> 'banana');

    // input and ouput
    def randString = "Random";
    println("a $randString string");
    printf("a %s string\n", randString);

    // "%-10s" put padding on the right side, "%10s" put the padding on the left side
    printf("%-10s %d %.2f %10s\n", ['Stuff', 10, 1.234, 'Random']);

    // print doesn't have ending \n
    print("What is your name: ");
    // get input from stdin
    def fName = System.console().readLine();
    println("Hell " + fName);

    print("Enter a number: ");
    def num1 = System.console().readLine().toDouble();
    print("Enter a number: ");
    def num2 = System.console().readLine().toDouble();
    printf("%.2f + %.2f = %.2f\n", [num1, num2, (num1 + num2)]);

    // list
    def primes = [2, 3, 5, 7, 11, 13];
    // access the element in list
    println("2nd prime number is " + primes[1]);
    println("3nd prime number is " + primes.get(2));

    // list can be mixture of string, int ...
    def employee = ['Derek', 40, 6.25, [1, 2, 3]];
    println("2nd internal number is " + employee[3][1]);

    // print the number of elements
    println("length of primes is " + primes.size());

    // append to a list
    primes.add(17);
    primes << 19;

    // concat another list
    primes + [21, 23];
    primes - [23];

    println("is primes empty " + primes.isEmpty());
    println("the first three prime numbers are " + primes[0..2]);
    println("the final primes are " + primes);


    println("matches " + primes.intersect([2, 5, 7]));
    println("reverse " + primes.reverse());
    println("sort " + primes.sort());
    println("last number " + primes.pop());

    // maps
    def paulMap = [
      'name' : 'Paul',
      'age' : 34,
      'addresss' : '123 Main Street',
      'list' : [1, 2, 3]
    ];

    // different ways of access map item
    println("name " + paulMap.name);
    println("name " + paulMap['name']);
    println("age " + paulMap.get('age'));
    println("2nd list item " + paulMap['list'][1]);

    // add a key in the map
    paulMap.put('city', 'Boulder');
    println("has city " + paulMap.containsKey('city'));
    println("map size " + paulMap.size());

    // range: range of values
    def oneToTen = 1..10;
    def aToZ = 'a'..'z';
    def zToA = 'z'..'a';

    println("oneToTen " + oneToTen);
    println("aToZ " + aToZ);
    println("zToA " + zToA);

    println("oneToTen size " + oneToTen.size());
    println("oneToTen 2nd item " + oneToTen.get(1));
    println("oneToTen contains 11 " + oneToTen.contains(11));
    println("oneToTen first item " + oneToTen.getFrom());
    println("oneToTen last item " + oneToTen.getTo());

    // Conditionals
    // == != < > <= >=
    // && || !
    def ageOld = 6;
    if (ageOld == 5) {
      println("go to kindergarten");
    } else if ((ageOld) > 5 && (ageOld < 18)) {
      printf("go to grade %d \n", (ageOld - 5));
    } else {
      println("go to college");
    }

    def canVote = true;
    println(canVote? "can vote" : "can't vote");

    // switch statement
    switch(ageOld) {
      case 0..6: 
        println("you are a child");
        break;
      case 7..12: println("you are a teenager"); break;
      case 16: println("you can drive"); break;
      case 18: 
        println("you can vote");
        break;
      default:
        println("have fun");
    }

    // looping
    def i = 0;

    // print the even numbers which is less than 8
    while (i < 10) {
      if (i % 2) {
        i++;
        continue;
      }

      if (i == 8) {
        break;
      }

      println(i);
      i++;
    }

    for (i = 0; i < 5; i++) {
      println(i);
    }

    // for with range
    for (j in 2..6) {
      println(j);
    }

    // for with list
    def randList = [1, 3, 6, 9, 11];
    for (j in randList) {
      println(j);
    }

    // for with map
    def custMap = [
      100 : 'Paul',
      101 : 'Sally',
      102 : 'Sue'
    ];
    for (cust in custMap) {
      println("$cust.value : $cust.key");
    }

    // Functions
    // call a funciton
    sayHello();

    println("5 + 4 = " + getSum(5, 4));

    def myName = "Derek";
    passByValue(myName);
    println("in Main myName " + myName);

    // in groovy, you can call a funciton without ()
    // in groovy, even the ending ; is not mandatory
    println("another way of calling function");
    passByValue myName

    def listToDouble = [1, 2, 3, 4];
    listToDouble = doubleList(listToDouble);
    println("new list " + listToDouble);

    def nums = sumAll(1, 2, 3, 4);
    println("sum  " + nums);

    def fact4 = factorial(4);
    println("factorial 4  " + fact4);

    // closure
    // similar to lambda concept in C++
    // it is basically a code block that can take parameters
    // parameter and code are separated by ->
    // closure: https://groovy-lang.org/closures.html
    // each, collect: http://docs.groovy-lang.org/next/html/documentation/working-with-collections.html
    def getFactorial = {num -> (num <= 1 ? 1 : num * call(num - 1)) };
    println ("factorial 4 with closure " + getFactorial(4));

    def greeting = "GoodBye";
    // closure can access variable outside
    def sayGoodBye = {theName -> println("$greeting $theName")};
    sayGoodBye("Derek");

    // closure can work with list
    def numList = [2, 3, 4, 5];
    numList.each {println(it)}

    // closure can work with map
    def employees = [
      'Derek' : 34,
      'Sally' : 45,
      'Sam'   : 26
    ]
    // each item in a map is a "pair"
    employees.each {println ("$it.key's age is $it.value")}

    def randNums = [1, 2, 3, 4, 5, 6];
    // in groovy, calling function can be 
    // func(parameters...) or
    // func parameters ...
    // each is function, which takes cloure as parameter
    // so you can write ranNums.each({num -> if (num % 2 == 0) println(num)})
    randNums.each {num -> if(num % 2 == 0)
    println(num)}

    def nameList = ['Derek', 'Sally', 'Sam'];
    def matchEle = nameList.find {item -> item == 'Sally'}
    println(matchEle)

    def numMatches = randNums.findAll {item -> item > 4}
    println(numMatches)

    // any item in the list > 5, returns boolean
    println("> 5 " + randNums.any {item -> item > 5});

    // every item in the list > 1, returns boolean
    println("> 1 " + randNums.every {item -> item > 1});

    // collect returns a new list based on each item in the old list
    println("double " + randNums.collect {item -> item * 2});

    // pass closure to a function
    def getEven = {num -> return (num % 2 == 0)}
    def evenNums = listEdit(randNums, getEven); 
    println("even numbers " + evenNums);

    // File io
    // read a file
    new File("test.txt").eachLine {
      line -> println(line);
    } 

    // overwrite to a file
    // the existing content will be removed
    new File("test.txt").withWriter('utf-8') {
      writer -> writer.writeLine("This line is written by the writer")  
    }

    // append to a file
    File file = new File("test.txt");
    file.append("This line is appended");

    // print the whole file
    println(file.text);

    // get the file size
    // file.length() needs to be quoted with {}, otherwise
    // groovy will try to find property file.length, instead of
    // calling file.length()
    println("file size : ${file.length()} bytes");
    println("is file : ${file.isFile()}");
    println("is dir : ${file.isDirectory()}");

    // copy a file
    def newFile = new File("test2.txt");
    newFile << file.text;

    // delete a file
    newFile.delete();

    def dirFiles = new File("").listRoots();
    dirFiles.each {
      item -> println item.absolutePath;
    }

    // object oriented programming
    // attributes are called fields

    // create an Animal object
    // if Animal has no constructor, the following will
    // create two fields - "name" and "sound"
    // def king = new Animal(name : 'King', sound : 'Growl')
    // since our Animal class does have constructor
    def king = new Animal('King', 'Growl');
    // we can access the object fields
    println("$king.name says $king.sound");

    // there is a default setter function for each field
    king.setSound('Grrrr'); 
    println("$king.name says $king.sound");

    // we can access 
    king.run();
    king.makeSound();
    println(king.toString());

    // create a Dog object
    def grover = new Dog ('Grover', 'Meow', 'Derek');
    grover.makeSound();

  }

  // define functions
  static def sayHello() {
    println("Hello");
  }

  // parameters with default value
  static def getSum(num1=0, num2=0) {
    return num1 + num2;
  }

  static def passByValue(name) {
    name = "Sally";
    println("in Function name " + name);
  }

  static def doubleList(list) {
    // for each item in the list, double it
    def newList = list.collect { it * 2};
    return newList;
  }

  // non-fixed integer type parameters
  static def sumAll(int... nums) {
    def sum = 0;
    nums.each { sum += it }
    return sum;
  }

  // recuseive
  static def factorial(num) {
    if (num <=1) {
      return 1;
    } else {
      return num * factorial(num - 1);
    }
  }

  static def listEdit (list, clo) {
    // alternatively, you can say "return list.findAll clo"
    return list.findAll(clo)
  }
  // the ending ; doesn't seem to be mandatory

}

// to support toString() on Animal object
import groovy.transform.ToString;

// this automatically create a toString() for Animal
@ToString(includeNames=true, includeFields=true)
class Animal {
  // defined the fields
  def name;
  def sound;

  def run() {
    println("$name runs");
  }

  def makeSound() {
    println("$name says $sound");
  }

  // constructor
  def Animal(name, sound) {
    this.name = name;
    this.sound = sound;
  } 
}

// class inheritance
class Dog extends Animal {
  def owner;

  def Dog (name, sound, owner) {
    super(name, sound);
    this.owner = owner;
  }

  // overwrite the method in parent
  def makeSound () {
    println("$name says bark and $sound")
  }
}

