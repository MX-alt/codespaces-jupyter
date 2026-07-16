type AnimalRecord = [number, number, number];

class AnimalShelter {
    private cats: AnimalRecord[] = [];
    private dogs: AnimalRecord[] = [];
    private timestamp = 0;

    enqueue(animal: [number, number]): void {
        const [id, type] = animal;
        const record: AnimalRecord = [id, type, this.timestamp];
        this.timestamp += 1;

        if (type === 0) {
            this.cats.push(record);
        } else {
            this.dogs.push(record);
        }
    }

    dequeueAny(): [number, number] {
        if (this.cats.length === 0 && this.dogs.length === 0) {
            return [-1, -1];
        }

        if (this.cats.length === 0) {
            return this.dequeueDog();
        }

        if (this.dogs.length === 0) {
            return this.dequeueCat();
        }

        if (this.cats[0][2] < this.dogs[0][2]) {
            return this.dequeueCat();
        }

        return this.dequeueDog();
    }

    dequeueDog(): [number, number] {
        if (this.dogs.length === 0) {
            return [-1, -1];
        }

        const record = this.dogs.shift();
        if (!record) {
            return [-1, -1];
        }
        return [record[0], record[1]];
    }

    dequeueCat(): [number, number] {
        if (this.cats.length === 0) {
            return [-1, -1];
        }

        const record = this.cats.shift();
        if (!record) {
            return [-1, -1];
        }
        return [record[0], record[1]];
    }
}

const shelter = new AnimalShelter();
shelter.enqueue([1, 0]);
shelter.enqueue([2, 1]);
shelter.enqueue([3, 0]);

console.log(shelter.dequeueAny());
console.log(shelter.dequeueDog());
console.log(shelter.dequeueCat());
