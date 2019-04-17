package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;
import java.util.List;

public class MainL { public static void main(String[] args) {
    List< Integer > lst = new ArrayList <> ();
    List< Integer > lst2 = new ArrayList <> ();
    lst.add(1);
    lst.add(2);
    lst.add(5);
    List < Integer > result = Nostalgia.rotate(lst);
    List < Integer > result2 = Nostalgia.rotate(lst2);
    System.out.println(result);
    System.out.println(result2);
}
}
