import java.util.LinkedList;
import java.util.Queue;

public class _22AnimalShelter {

    private final Queue<int[]> cats = new LinkedList<>();
    private final Queue<int[]> dogs = new LinkedList<>();
    private int timestamp = 0;

    public void enqueue(int[] animal) {
        if (animal == null || animal.length < 2) {
            throw new IllegalArgumentException("Animal record must contain id and type.");
        }

        int[] record = {animal[0], animal[1], timestamp++};
        if (animal[1] == 0) {
            cats.offer(record);
        } else {
            dogs.offer(record);
        }
    }

    public int[] dequeueAny() {
        if (cats.isEmpty() && dogs.isEmpty()) {
            return new int[]{-1, -1};
        }
        if (cats.isEmpty()) {
            return dequeueDog();
        }
        if (dogs.isEmpty()) {
            return dequeueCat();
        }

        return cats.peek()[2] < dogs.peek()[2] ? dequeueCat() : dequeueDog();
    }

    public int[] dequeueDog() {
        if (dogs.isEmpty()) {
            return new int[]{-1, -1};
        }
        int[] record = dogs.poll();
        return new int[]{record[0], record[1]};
    }

    public int[] dequeueCat() {
        if (cats.isEmpty()) {
            return new int[]{-1, -1};
        }
        int[] record = cats.poll();
        return new int[]{record[0], record[1]};
    }

    public static void main(String[] args) {
        _22AnimalShelter shelter = new _22AnimalShelter();
        shelter.enqueue(new int[]{1, 0});
        shelter.enqueue(new int[]{2, 1});
        shelter.enqueue(new int[]{3, 0});

        int[] first = shelter.dequeueAny();
        if (first[0] != 1 || first[1] != 0) {
            throw new AssertionError("First dequeueAny failed");
        }

        int[] second = shelter.dequeueDog();
        if (second[0] != 2 || second[1] != 1) {
            throw new AssertionError("dequeueDog failed");
        }

        int[] third = shelter.dequeueCat();
        if (third[0] != 3 || third[1] != 0) {
            throw new AssertionError("dequeueCat failed");
        }

        System.out.println("All test cases passed ✅");
    }
}
