//  **Zero-Sum Subarray Detection**
// # “Given an integer array, find a subarray whose sum is zero.
// # Return start and end indices, and the longest such subarray.”

import java.util.*;

public class ZeroSumSubarray {
    public static int[] findLongestZeroSumSubarray(int[] arr) {
        // Map to store (prefixSum -> earliest index where this sum occurred)
        Map<Integer, Integer> sumToIndex = new HashMap<>();
        sumToIndex.put(0, -1);  // Important: handles sum from start

        int currentSum = 0;
        int maxLength = 0;
        int startIdx = -1, endIdx = -1;

        for (int i = 0; i < arr.length; i++) {
            currentSum += arr[i];

            if (sumToIndex.containsKey(currentSum)) {
                int prevIndex = sumToIndex.get(currentSum);
                int length = i - prevIndex;
                if (length > maxLength) {
                    maxLength = length;
                    startIdx = prevIndex + 1;
                    endIdx = i;
                }
            } else {
                sumToIndex.put(currentSum, i);
            }
        }

        if (maxLength == 0) {
            return new int[]{}; // No zero-sum subarray found
        }

        return new int[]{startIdx, endIdx};
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, -3, 4, -4, 6};
        int[] result = findLongestZeroSumSubarray(arr);

        if (result.length == 0) {
            System.out.println("No zero-sum subarray found.");
        } else {
            System.out.println("Longest zero-sum subarray is from index " +
                               result[0] + " to " + result[1]);
        }
    }
}
