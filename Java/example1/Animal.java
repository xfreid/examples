public class Animal {
    // class contains fields or instance variables
    // functions in class are methods
    private String name;
    private int weight;
    private String sound;

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

    // note:
    // local variables are used in function
    // for non-object data type, pass by value
    // for object, pass by reference
}