package com.ccvalidator.validator;

import java.util.ArrayList;
import java.util.List;

public class Validator {

	public static void main(String[] args) {
		if (checkSum("4320-9800-7010-4862")) {
			System.out.println("Valid Card Number");
		} else {
			System.out.println("Invalid Card Number");
		}
	}

	private static boolean checkSum(String ccnum) {

		if (ccnum != null) {
			String[] cc_nums = ccnum.trim().split("-");
			List<String> l = new ArrayList<>();

			for (String c : cc_nums) {
				for (char digit : c.toCharArray()) {
					l.add(String.valueOf(digit));
				}
			}

			if (l.size() == 16) {

				int[] intCcNum = new int[16];
				for (int i = 0; i < intCcNum.length; i++) {
					intCcNum[i] = Integer.parseInt(l.get(i));
				}

				// checksum algorithm
				int check_sum = 0;
				for (int i = 0; i < 15; i += 2) {
					intCcNum[i] = intCcNum[i] * 2;
					while (intCcNum[i] > 9) {
						int sumOfDigits = 0;
						sumOfDigits = sumOfDigits + intCcNum[i] % 10 + intCcNum[i] / 10;
						intCcNum[i] = sumOfDigits;
					}
					check_sum = check_sum + intCcNum[i] + intCcNum[i + 1];
				}
				System.out.println(check_sum);
				if (check_sum % 10 == 0) {
					return true;
				}
			}
			return false;
		}
		return false;
	}

}
