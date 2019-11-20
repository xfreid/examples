// the public class name has to match the file name
// you can declare more classes, but they can't be public
public interface Fly {

    public String fly();    
}

// the concrete classes which implement "Fly" interface
// define different fly behavior
class canFly implements Fly {

    public String fly() {
        return "I can fly";
    }
}

class cantFly implements Fly {

    public String fly() {
        return "I can't fly";
    }
}