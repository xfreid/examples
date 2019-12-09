public class Animal {
    // class contains fields or instance variables
    // functions in class are methods
    private String name;
    private int weight;
    private String sound;

    // core of the Strategy Pattern
    // public so that sub-class can access
    public Fly flyBehaivor;

    public String getName() { return name; }
    public void setName(String newName) {  name = newName; }

    public int getWeight() {  return weight; }
    public void setWeight(int newWeight) {
        if (newWeight > 0) {
            weight = newWeight; 
        } else {
            System.out.println("Weigh must be bigger than 0");
        }
    }

    public String getSound() {  return sound; }
    public void setSound(String newSound) {  sound = newSound; }

    // delegate the fly behavior
    public String doFly() {
        return flyBehaivor.fly(); 
    }

    public void setFlyBehavior (Fly newFlyBehaivor) {
        flyBehaivor = newFlyBehaivor;
    }
}