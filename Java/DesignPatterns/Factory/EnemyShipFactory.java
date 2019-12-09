import javax.lang.model.util.ElementScanner6;

// What is a factory pattern
// when a method returns one of serveral possible classes that share a common
// super class

/* example
   create a new enemy ship in the game
   random number generator picks a number associated with a specific enemy ship
   the factory returns the enemy ship associatd with that number
 */

// Fei: basically delegate the object creation to a separate factory class
// so that client doesn't need to change the code if we decide to 
// add/remove any EnemyShip sub-classes

public class EnemyShipFactory {

    public EnemyShip makeEnemyShip(String enemyShipType) {
        EnemyShip enemyShip = null;

        if (enemyShipType.equals("U")) {
            enemyShip = new UfoEnemyShip();
        } else if (enemyShipType.equals("R")) {
            enemyShip = new RocketEnemyShip();
        } else if (enemyShipType.equals("B")) {
            enemyShip = new BigUfoEnemyShip();
        } else return null;

        return enemyShip;
    }

}
