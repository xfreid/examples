// Monkey implements the Living interface
public class Monkey implements Living {
    private String name;
    // what is "final" keyword?

    // @Override annotation informs the compiler that the element is meant to 
    // override an element declared in a superclass. While it is not required 
    // to use this annotation when overriding a method, it helps to prevent errors.
    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(final String newName) {
        name = newName;
    }

    @Override
    public double getWeight() {
        return 0;
    }

    @Override
    public void setWeight(final double newWeight) {

    }

    @Override
    public String getFavFood() {
        return null;
    }

    @Override
    public void setFavFood(final String newFavFood) {

    }

    @Override
    public double getSpeed() {
        return 0;
    }

    @Override
    public void setSpeed(final double newSpeed) {

    }

    @Override
    public String getSound() {
        return null;
    }

    @Override
    public void setSound(final String newSound) {

    }

}