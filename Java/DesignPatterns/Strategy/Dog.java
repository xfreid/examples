public class Dog extends Animal {
    public void digHole () {
        System.out.println("Dog digs a hole");
    }

    // constructor
    public Dog() {
        super();

        setSound("bark");

        // set the fly behaior
        flyBehaivor = new cantFly();
    }
} 