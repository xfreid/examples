public class Giraffe extends Creature {
    @Override
    public void setName(String newName) {
        name = newName;
    }
    
    @Override
    public String getName() {
        return name;
    }

    @Override
    public int getWeight(){
        return 0;
    }

    @Override
    public void setWeight(int newWeight){
    }


}