public class Bird extends Animal {

    // constructor
    public Bird() {
        super();

        setSound("tweet");

        // set the fly behaior
        flyBehaivor = new canFly();
    }
} 