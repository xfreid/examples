// install JDK
// install "Java Extension Pack" in VS Code
// make sure javac is in the PATH
// optional: make sure JAVA_HOME env variable is set

// package name reflects the directory structure
// package: com.fei.javacourse.basics

// the public class name in the .java file MUST match the file name
// Hello World
public class basics{
    // not staic variable
    int justANum = 10;
    public static void main(String[] args) {
        System.out.println("Hello World");

        // Design Pattern: https://www.youtube.com/playlist?list=PLF206E906175C7E07
        // Dog extends Animal
        // basic OOP
        Dog fido= new Dog();
        fido.setName("Fido");
        System.out.println(fido.getName());

        fido.digHole();
        fido.setWeight(-1);

        // non-object data is passed by value
        // to demonstrate pass by value
        int number = 10;
        fido.changeVar(number);
        System.out.println("after method call, number is " + number);

        // object is passed by reference
        changeObject(fido);
        System.out.println("after method call, dog name is " + fido.getName());

        // polymorphism
        // instead of "Dog doggy"
        Animal doggy = new Dog();
        Animal kitty = new Cat();
        System.out.println("doggy says " + doggy.getSound());
        System.out.println("kitty says " + kitty.getSound());

        Animal [] animals = new Animal[4];
        animals[0] = doggy;
        animals[1] = kitty;

        System.out.println("doggy says " + animals[0].getSound());
        System.out.println("kitty says " + animals[1].getSound());

        animalSpeak(doggy);

        // Note object with Animal type can ONLY access Animal methods
        // the following call would not work
        // doggy.digHole();
        // error: cannot find symbol
        //   symbol:   method digHole()
        // but you can cast doggy to be Dog
        ((Dog)doggy).digHole(); // this works

        // this method "main" is a statci method
        // it can't access a non static variable
        //  error: non-static variable justANum cannot be referenced from a static context
        // System.out.println(justANum);
        
        // you can't call a private method outside the class
        // error: bePrivate() has private access in Dog
        // fido.bePrivate();
        // this works
        fido.accessPrivate();

        Giraffe giraffe = new Giraffe();
        giraffe.setName("Frank");
        System.out.println("Giraffe name is " + giraffe.getName());

        Monkey monkey = new Monkey();
        monkey.setName("Glant");
        System.out.println("Monkey name is " + monkey.getName());
    }

    public static void changeObject(Dog fido) {
        fido.setName("Marcus");
    }

    // Note the parameter type is "Animal"
    public static void animalSpeak(Animal animal) {
        System.out.println("animal says " + animal.getSound());
    }
}