package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;

public class list {
    public  static ArrayList<Integer> rotate(ArrayList<Integer> arr){
        arr.add(0,arr.size());
        arr.remove(arr.size()-1);
        return arr;
    }
}
