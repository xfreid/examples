public class Dog extends Animal {
    public void digHole () {
        System.out.println("Dog digs a hole");
    }

    // constructor
    public Dog() {
        super();

        setSound("bark");
    }

    // to demonstrate pass by value
    public  void changeVar(int number) {
        number = 12;
        System.out.println("in changeVar method, number is " + number);
    }

    // private method can't be access outside the class
    private void bePrivate() {
        System.out.println("in private method");
    }

    public void accessPrivate() {
        // private method can be called inside the class
        bePrivate();
    }
} 