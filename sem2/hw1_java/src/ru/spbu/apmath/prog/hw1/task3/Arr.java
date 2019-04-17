package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;
import java.util.List;

public class Arr {
    public  static List<Integer> rotate(List<Integer> arr){
        if (arr.isEmpty()){
            List<Integer> new_lst = new ArrayList<>();
            return new_lst;
        }
        List<Integer> cope_lst = new ArrayList<>();
        for (int i=0; i< arr.size(); i++){
            cope_lst.add(arr.get(i));
        }

        cope_lst.add(0,cope_lst.get(cope_lst.size()-1));
        cope_lst.remove(cope_lst.size()-1);
        return cope_lst;
    }
} 
