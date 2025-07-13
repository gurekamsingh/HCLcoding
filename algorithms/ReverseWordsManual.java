// Reverse Words in a Sentence
// “Reverse the words in a sentence without using built-in reverse/ split functions.”

// import java.util.*;

public class ReverseWordsManual {

    public static String reverseWords(String sentence) {
        StringBuilder result = new StringBuilder();
        int i = sentence.length() - 1;

        while (i >= 0) {
            // Skip trailing spaces
            while (i >= 0 && sentence.charAt(i) == ' ') {
                i--;
            }

            if (i < 0) break;

            // Find end of the current word
            int end = i;

            // Find start of the word
            while (i >= 0 && sentence.charAt(i) != ' ') {
                i--;
            }

            int start = i + 1;

            // Append the word to result
            for (int j = start; j <= end; j++) {
                result.append(sentence.charAt(j));
            }

            result.append(' ');  // Add space after the word
        }

        // Remove the last added space if any
        if (result.length() > 0) {
            result.setLength(result.length() - 1);
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String input = "I love Java";
        String output = reverseWords(input);
        System.out.println("Reversed: " + output);
    }
}
