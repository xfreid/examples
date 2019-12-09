import java.util.Scanner;  // keyboard input

public class EnemyShipTest {

    public static void main(String[] args) {
        // old way of construting the EnemyShip objects
        // EnemyShip ufoShip = new UfoEnemyShip();
        // doStuffEnemy(ufoShip);

        Scanner userInput = new Scanner(System.in);
        String enemyShipOption = "";
        System.out.println("What type of ship (U / R)?");
        if (userInput.hasNextLine()) {
            enemyShipOption = userInput.nextLine();
        }

        EnemyShip enemyShip = null;
        if (enemyShipOption.equals("U")) {
            enemyShip = new UfoEnemyShip();
        } else if (enemyShipOption.equals("R")) {
            enemyShip = new RocketEnemyShip();
        } 
        doStuffEnemy(enemyShip);
    }

    public static void doStuffEnemy(EnemyShip anEnemyShip) {
        anEnemyShip.display();
        anEnemyShip.shoot();
    }

}