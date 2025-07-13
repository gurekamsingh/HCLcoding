// Prime Number Generator / Checker
// “Generate all prime numbers up to N, or check if a number is prime.”
// Basic loops and math. Difficulty: Easy.


public class PrimeUtils {

    // Part A: Generate all prime numbers up to N
    public static void generatePrimes(int n) {
        System.out.println("Prime numbers up to " + n + ":");
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

    // Part B: Check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        generatePrimes(20);
        System.out.println("Is 29 prime? " + isPrime(29));
        System.out.println("Is 30 prime? " + isPrime(30));
    }
}
