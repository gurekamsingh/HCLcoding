// Second Largest Element
// “Find the second largest element in an unsorted array without sorting it.”

import java.util.*;

public class SecondLargestFinder {

    public static int findSecondLargest(int[] arr) {
        if (arr.length < 2) {
            throw new IllegalArgumentException("Array must have at least 2 elements.");
        }

        int max = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;

        for (int num : arr) {
            if (num > max) {
                secondMax = max;
                max = num;
            } else if (num > secondMax && num != max) {
                secondMax = num;
            }
        }

        if (secondMax == Integer.MIN_VALUE) {
            throw new RuntimeException("No second largest element found (e.g., all elements equal).");
        }

        return secondMax;
    }

    public static void main(String[] args) {
        int[] arr = {10, 5, 20, 8, 20};
        System.out.println("Second Largest: " + findSecondLargest(arr));
    }
}
