
// Parent class
class Animal {
    // Properties
    private String name;
    private int age;

    // Constructor
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Methods
    public void makeSound() {
        System.out.println("The animal makes a sound");
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Subclass inheriting from Animal
class Dog extends Animal {
    // Constructor
    public Dog(String name, int age) {
        super(name, age);
    }

    // Overriding method
    @Override
    public void makeSound() {
        System.out.println("The dog barks");
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        // Creating objects of Animal and Dog
        Animal animal = new Animal("Generi

