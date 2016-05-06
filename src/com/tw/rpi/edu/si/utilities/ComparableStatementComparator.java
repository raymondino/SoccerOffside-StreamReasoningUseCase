package com.tw.rpi.edu.si.utilities;

import java.util.Comparator;

public class ComparableStatementComparator implements Comparator<ComparableStatement>{

    @Override
	public int compare(ComparableStatement a, ComparableStatement b) {
		return a.compareTo(b);
	}
}
