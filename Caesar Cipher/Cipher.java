import java.util.Scanner;

public class Cipher {

	private static Scanner s;

	public static void main(String[] args) {
		s = new Scanner(System.in);
		System.out.println("Enter message to encrypt:");
		String message = s.nextLine().toUpperCase();
		if (isAlpha(message)) {
			String cipher = encryption(message);
			String original = decryption(cipher);
			System.out.println("Encryption: " + cipher);
			System.out.println("Decryption: " + original);
		}

	}

	private static boolean isAlpha(String message) {

		return message.matches("^[ A-Z.]+$");
	}

	private static String encryption(String message) {
		char[] chars = message.toCharArray();
		String cipher = "";
		for (char c : chars) {
			if (c == ' ' || c == '.') {
				cipher = cipher + c;
			} else {
				int val = (int) c + 3;
				if (val > 90) {
					val = 65 + (val - 90);

				}
				cipher = cipher + (char) val;
			}
		}

		return cipher;
	}

	private static String decryption(String message) {
		char[] chars = message.toCharArray();
		String cipher = "";
		for (char c : chars) {
			if (c == ' ' || c == '.') {
				cipher = cipher + c;
			} else {
				int val = (int) c - 3;
				if (val < 65) {
					val = 90 - (65 - val);

				}
				cipher = cipher + (char) val;
			}
		}

		return cipher;
	}

}
